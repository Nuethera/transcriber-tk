import time
from tkinter import *
from googletrans import Translator
import speech_recognition as sr


class Transcriber:

    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.stopper = None
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source, duration=1)

    def start_rec(self, ln):
        print("recording")

        with self.mic as source:
            audio = self.r.listen(source, phrase_time_limit=10)

        print('processing')
        # Process label

        t = self.r.recognize_google(audio, language=ln)
        print(t)
        return t

    def audio_transcribe(self, path, ln):
        audio_file = sr.AudioFile(path)
        with audio_file as source:
            self.r.adjust_for_ambient_noise(source, duration=1)
            audio = self.r.record(source)
        t = self.r.recognize_google(audio, language=ln)
        print(t)
        return t

trans = Transcriber()
translator = Translator()