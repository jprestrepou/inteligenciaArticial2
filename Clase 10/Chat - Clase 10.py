# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:52:10 2023

@author: jupa_
"""

"""
# for speech to text
pip install SpeechRecognition #(3.8.1)
# for text to speech
pip install gTTS #(2.2.3)
# for language model
pip install transformers #(4.11.3)
pip install tensorflow #(2.6.0, or pytorch)

"""

import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os

class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name
        # Run the AI
    def speech_to_text(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
            try:

                self.text = recognizer.recognize_google(audio)
                print("me --> ", self.text)

            except:
                
                print("me --> ERROR")     
    
    def wake_up(self, text):
        
        return True if self.name in text.lower() else False

    @staticmethod
    def text_to_speech(text):
        
        print("ai --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("afplay res.mp3") #macbook->afplay | windows->start
        os.remove("res.mp3")


    
if __name__ == "__main__":

    ai = ChatBot(name="maya")

    while True:
        ai.speech_to_text()
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Maya the AI, what can I do for you?"
            ai.text_to_speech(res)
    
    

