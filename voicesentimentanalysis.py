from textblob import TextBlob
import speech_recognition as sr
import pyaudio
import time

r = sr.Recognizer()
with sr.Microphone() as source:
	while True:
	    print("Say Something for Sentiment Analysis")
	    audio= r.listen(source)
	    try:
	    	voice_data= r.recognize_google(audio)
	    	userword= TextBlob(voice_data)
	    	if userword.sentiment.polarity >=  0.17:
	        	print("It is a Positive Comment")
	    	elif userword.sentiment.polarity <= -0.17:
	        	print("It is a Negative Comment")
	    	elif voice_data=='stop':
	    		break
	    	else:
	        	print("It is a Neutral Comment")
	    	time.sleep(0.2)
	    except:
	    	print("Voice not Recognized Say again")


	        