import pyttsx3

from textblob import TextBlob
import speech_recognition as sr
import pyaudio
import time

engine= pyttsx3.init()


def say(audio):
	engine.say(audio)
	engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
	while True:
	    say("Say Something for Sentiment Analysis")
	    audio= r.listen(source)
	    try:
	    	voice_data= r.recognize_google(audio, language='en-in')
	    	userword= TextBlob(voice_data)
	    	if userword.sentiment.polarity >=  0.17:
	        	say("It is a positive comment")
	    	elif userword.sentiment.polarity <= -0.17:
	        	say("It is a negative Comment")
	    	elif voice_data=='stop it':
	    		say("ok thank you sir")
	    		break
	    	else:
	        	say("It is a neutral Comment")
	    	time.sleep(0.1)
	    except:
	    	say("Voice not Recognized Say again")
