from django.shortcuts import render, redirect
import speedtest
from geopy.geocoders import Nominatim
from gtts import gTTS
import os
from googletrans import Translator
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
# Create your views here.


def index(request):

    st = speedtest.Speedtest()
    x = st.download() * 9.537 * 0.0000001
    y = st.upload() * 9.537 * 0.0000001
    servernames = []

    z = st.get_servers(servernames)
    return render(request, 'index.html', {'d': x, 'u': y, 'ser': z})

def location(request):
        return render(request, 'location.html')


def go(request):
        loc = Nominatim(user_agent="GetLoc")
        getLoc = loc.geocode(request.GET['city'])

        return render(request, 'location.html', {"a": getLoc.address, "b": getLoc.latitude, "c": getLoc.longitude})

def home(request):
    return render(request, 'home.html')


def speech(request):
    return render(request, 'speech.html')

def conver(request):
        mytext =request.GET['text']
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("wel.mp3")
        os.system("wel.mp3")

        return render(request, 'speech.html')

def trans(request):
    language = request.GET['main']
    translator = Translator()
    result = translator.translate(request.GET['trans'], src='en', dest=request.GET['main'])

    print(result.src)
    print(result.dest)
    print(result.text)
    myobj = gTTS(text=result.text, lang=language, slow=False)
    myobj.save("we.mp3")
    os.system("we.mp3")
    print(request.GET['main'])
    return render(request, 'speech.html')


def chatbot(request):
    return render(request, 'chatbot.html')


def chat(request):
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)

    # Create a new chat bot named Charlie
    chatbot = ChatBot('Charlie')

    trainer = ListTrainer(chatbot)

    trainer.train([
        "Hi, can I help you?",
        "Sure, I'd like to book a flight to Iceland.",
        "Your flight has been booked."
        "i love you"
    ])

    # Get a response to the input text 'I would like to book a flight.'

    response = chatbot.get_response(input(request.GET['text']))


    return render(request, 'robo.html', {'chat':response})
