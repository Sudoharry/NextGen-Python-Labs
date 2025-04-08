import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set TTS voice properties
engine.setProperty('rate', 150)  # Speech speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # You can change voice index

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce noise
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Speech service is unavailable.")
        return ""

def respond(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "your name" in command:
        speak("I am your voice assistant.")
    elif "time" in command:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

# Main loop
if __name__ == "__main__":
    speak("Voice assistant initialized. How can I help?")
    while True:
        command = listen()
        if command:
            respond(command)
