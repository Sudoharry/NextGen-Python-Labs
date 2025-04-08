import speech_recognition as sr

# Path to your WAV file
audio_file = r"C:\Users\Nilesh\Downloads\words-phrases-are-we-having-fun-tonight-pretties.wav"

# Initialize recognizer
recognizer = sr.Recognizer()

# Set chunk duration (in seconds)
chunk_duration = 10
full_transcription = ""

# Load the audio file and get total duration
with sr.AudioFile(audio_file) as source:
    print("Calibrating for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    total_duration = int(source.DURATION)  # Get duration in seconds
    print(f"Total duration: {total_duration} seconds")

    for offset in range(0, total_duration, chunk_duration):
        print(f"\n🔹 Processing chunk from +{offset}s to +{offset + chunk_duration}s...")
        try:
            with sr.AudioFile(audio_file) as chunk_source:
                audio_data = recognizer.record(chunk_source, offset=offset, duration=chunk_duration)
                text = recognizer.recognize_google(audio_data)
                print("📝 Chunk Text:", text)
                full_transcription += text + " "
        except sr.UnknownValueError:
            print("❌ Could not understand this chunk.")
        except sr.RequestError as e:
            print("❌ API Error:", e)
            break

print("\n✅ Final Transcription:")
print(full_transcription.strip())
