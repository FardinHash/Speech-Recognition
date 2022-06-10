import os
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            audio = r.listen(mic)

            text= r.recognize_google(audio)
            text= text.lower()

            print(f'Recognized Speech: {text}')

            if text=='stop joking':
                break
    except sr.UnknownValueError:
        r = sr.Recognizer()
        continue

