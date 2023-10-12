import speech_recognition as speech_recognition

def listen():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = recognizer.listen(source)
        text = recognizer.recognize_sphinx(audio)
    return text