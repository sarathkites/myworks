import speech_recognition as sr

import os
import time

class SpeechHandler:
    def __init__(self):
        print("Speech Handler")
        
    def wavparser(self,file_path):
    
        print(sr.__version__)
        r = sr.Recognizer()
        audio_file = sr.AudioFile(file_path)
        with audio_file as source:
            audio = r.record(source)
            #print(type(audio))
            
        res = r.recognize_google(audio)
        return res
            
