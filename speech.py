from flask import Flask, render_template, request, redirect, url_for, session
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
import speech_recognition as sr
import gtts
from playsound import playsound
import os


#engine = pyttsx3.init('sapi5')
#voices = engine.getProperty('voices')
#engine.setProperty('voices', voices[1].id)


def speaker(text):
    tts = gtts.gTTS(text, lang='en')
    tts.save('hello.mp3')
    playsound('hello.mp3')
    os.remove('hello.mp3')


"""
def speak(text):
    engine.say(text)
    engine.runAndWait()
"""


def new_spk(src):
    speaker('I am listening. Please say something')
    r = sr.Recognizer()
    sr.Microphone.list_microphone_names()
    mic = sr.Microphone()
    with mic as source:
        #audio = r.record(source, duration=5)

        r.adjust_for_ambient_noise(source, duration=0.2)

        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        # to recognize it in a particular language.
        voice = r.recognize_google(audio, language="en-NG")

        # translated = GoogleTranslator(source=src, target=targ).translate(
        #   voice)

        return voice


"""
 translator = Translator()
        result = translator.translate(
            text=voice, src=src, dest='en')
        res = result.text

        speaker(res)
        return res
"""


def spk(source, destination, texting):

    if source == 'Yoruba' and destination == 'English':
        translator = Translator()
        result = translator.translate(
            text=texting, src='yo', dest='en')

        speaker(result.text)
        return render_template("home.html")

    elif source == 'Yoruba' and destination == 'Igbo':

        translator = Translator()
        result = translator.translate(
            text=texting, src='yo', dest='ig')

        speaker(result.text)

        return render_template("home.html")

    elif source == 'Yoruba' and destination == 'Hausa':
        translator = Translator()
        result = translator.translate(
            text=texting, src='yo', dest='ha')

        speaker(result.text)

        return render_template("home.html")

    elif source == 'English' and destination == 'Yoruba':
        translator = Translator()
        result = translator.translate(
            text=texting, src='en', dest='yo')

        speaker(result.text)

        return render_template("home.html")

    elif source == 'English' and destination == 'Hausa':
        translator = Translator()
        result = translator.translate(
            text=texting, src='en', dest='ha')

        speaker(result.text)

        return render_template("home.html")

    elif source == 'English' and destination == 'Igbo':
        translator = Translator()
        result = translator.translate(
            text=texting, src='en', dest='ig')

        speaker(result.text)

        return render_template("home.html")

    elif source == 'Hausa' and destination == 'Yoruba':
        translator = Translator()
        result = translator.translate(
            text=texting, src='ha', dest='yo')

        speaker(result.text)

        return render_template("home.html")

    elif source == 'Hausa' and destination == 'English':
        translator = Translator()
        result = translator.translate(
            text=texting, src='ha', dest='en')

        speaker(result.text)

        return render_template("home.html")

    elif source == 'Hausa' and destination == 'Igbo':
        translator = Translator()
        result = translator.translate(
            text=texting, src='ha', dest='ig')

        speaker(result.text)

        return render_template("home.html")

    elif source == 'Igbo' and destination == 'Hausa':
        translator = Translator()
        result = translator.translate(
            text=texting, src='ig', dest='ha')

        speaker(result.text)

        return render_template("home.html")

    elif source == 'Igbo' and destination == 'Yoruba':
        translator = Translator()
        result = translator.translate(
            text=texting, src='ig', dest='yo')

        speaker(result.text)

        return render_template("home.html")

    elif source == 'Igbo' and destination == 'English':
        translator = Translator()
        result = translator.translate(
            text=texting, src='ig', dest='en')

        speaker(result.text)

        return render_template("home.html")

    else:
        error = 'kindly go back to the home page and pick the correct language'
        return render_template("home.html", result=error)
