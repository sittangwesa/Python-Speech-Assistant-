from email.mime import audio
from random import random
from re import search
import time
import playsound
import os
import random
from gtts import gTTS
import speech_recognition as sr
from time import ctime
import webbrowser


r= sr.Recognizer()

def record_audio(ask=False):
    if ask:
        any_speak(ask)
        
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice_data= ''
        try:
            voice_data = r.recognize_google(audio)
            any_speak(voice_data)
        except sr.UnknownValueError:
            any_speak('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, My speech service is down')
        return voice_data
    
def any_speak(audio_string):
    gtts = gTTS(text= audio_string, lang='en')
    r= random.randtint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    gtts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
            
def respond():
    if 'What is your name:' in voice_data:
        any_speak('My name is Magie')
    if 'What time is it' in voice_data:
        any_speak(ctime())
    if 'Search' in voice_data:
        search= record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        any_speak('Here is what I found for you' + search)
        
    if 'Find Location' in voice_data:
        location= record_audio('What is location?')
        url = 'https://google.nl/maps/place/=' + location + '/&amp;'
        webbrowser.get().open(url)
        any_speak('Here is location of ' + location)
    if 'exit' in voice_data:
        exit
 
time.sleep(1)          
any_speak('How ca I help you')
while 1:
    voice_data=record_audio()
    respond(voice_data)