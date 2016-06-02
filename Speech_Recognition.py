## -*- coding: utf-8 -*-
"""
Created on Wed June 01 12:26:10 2016
@author: keyur
"""


# Install sox tool

# Speech to Text
from pygsr import Pygsr
speech = Pygsr()
speech.record(5)
phrase, complete_response = speech.speech_to_text('en_US')
print phrase

# Text to Speech
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 100)

voices = engine.getProperty('voices')
for voice in voices:
    print "Using voice:", repr(voice)
    engine.setProperty('voice', voice.id)
    engine.say("Hi there, how's you ?")
#    engine.say("A B C D E F G H I J K L M")
#    engine.say("N O P Q R S T U V W X Y Z")
#    engine.say("0 1 2 3 4 5 6 7 8 9")
#    engine.say("Sunday Monday Tuesday Wednesday Thursday Friday Saturday")
#    engine.say("Violet Indigo Blue Green Yellow Orange Red")
#    engine.say("Apple Banana Cherry Date Guava")
engine.runAndWait()