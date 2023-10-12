# This file will handle the integration with Minstral 7B LLM.
# More code will be added here as we progress.

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_sphinx(audio)
    return text