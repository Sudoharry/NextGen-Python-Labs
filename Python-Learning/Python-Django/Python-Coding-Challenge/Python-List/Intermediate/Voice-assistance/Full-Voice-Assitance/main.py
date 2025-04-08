from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import speech_recognition as sr
from speech_recognition import RequestError, UnknownValueError
import pyttsx3
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Set Ollama URL from env or default
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Enable CORS for frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Text-to-Speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text: str):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
        except RequestError:
            speak("Speech service is unavailable.")
        except UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except Exception as e:
            print(f"[ERROR] {e}")
            speak("An error occurred.")
        return None

def ask_ollama(prompt: str) -> str:
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json().get("response", "No response from Ollama.")
    except Exception as e:
        error_msg = f"Error connecting to Ollama: {e}"
        print(error_msg)
        return error_msg

def respond(command: str) -> str:
    command = command.lower()
    if "hello" in command:
        response = "Hello! How can I assist you today?"
    elif "your name" in command:
        response = "I am your voice assistant."
    elif "time" in command:
        response = f"The current time is {datetime.now().strftime('%I:%M %p')}."
    elif "exit" in command or "stop" in command:
        response = "Goodbye!"
    else:
        response = ask_ollama(command)

    speak(response)
    return response

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask(query: str = Form(...)):
    if not query:
        return JSONResponse(status_code=400, content={"error": "No input received"})
    response = ask_ollama(query)
    speak(response)
    return JSONResponse(content={"response": response})

@app.post("/listen")
async def listen_route():
    command = listen()
    if not command:
        return JSONResponse(content={"response": "Sorry, I didn’t catch that."})
    response = respond(command)
    return JSONResponse(content={"response": response})
