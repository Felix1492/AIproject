# This file will include "Offline TTS Audiobook Maker".
# More code will be added here as we progress.

import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()