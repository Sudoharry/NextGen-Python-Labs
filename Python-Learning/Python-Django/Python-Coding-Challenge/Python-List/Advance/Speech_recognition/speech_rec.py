import speech_recognition as sr
from pydub import AudioSegment

# Path to your audio file (can be MP3 or WAV)
input_file = r"C:\Users\Nilesh\Downloads\words-phrases-are-we-having-fun-tonight-pretties.wav"
converted_file = "converted.wav"

# Step 1: Convert MP3 to WAV
print("Converting MP3 to WAV...")
sound = AudioSegment.from_mp3(input_file)
sound.export(converted_file, format="wav")

# Step 2: Initialize recognizer
recognizer = sr.Recognizer()

# Step 3: Load the audio file
with sr.AudioFile(converted_file) as source:
    print("Reading audio file...")
    audio_data = recognizer.record(source)

# Step 4: Recognize using Google Speech API
try:
    print("Transcribing audio...")
    text = recognizer.recognize_google(audio_data)
    print("✅ Extracted Text:\n", text)

except sr.UnknownValueError:
    print("❌ Could not understand the audio.")

except sr.RequestError as e:
    print("❌ API Error:", e)
