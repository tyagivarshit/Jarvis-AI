import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import webbrowser


def init_engine():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 175)
    return engine


def speak(audio):
    engine = init_engine()
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    engine.stop()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=5)
    try:
        print("Recogninzing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis AI. Please tell me how may I help you?")


if __name__ == "__main__":
    wish()
    if 1:
        query = takeCommand().lower()
        #Logic building begins here
        if("jarvis open windows explorer" in query):
            npath = "C:\\Windows\\explorer.exe"
            os.startfile(npath)
        elif("jarvis open google" in query):
            speak("sir , what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")
        elif("jarvis open brave" in query):
            bravepath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravepath)
        elif("jarvis open vs code" in query):
            vspath = "C:\\Users\\tyagi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)
        elif("Jarvis open camera" in query):
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("Webcam", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif("jarvis open spotify" in query):
            songpath = "C:\\Users\\tyagi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
            os.startfile(songpath)
        elif("jarvis open youtube" in query):
            speak("sir , what content do you want to search in youtube")
            cm = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query= {cm}")
        elif "jarvis tell me my ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your IP is: {ip} ")
        elif("jarvis open gpt" in query):
            cpath = "https:www.chatgpt.com/"
            os.startfile(cpath)
        elif("jarvis open facebook" in query):
            facebookurl = "https://www.facebook.com/"
            os.startfile(facebookurl)
        elif("jarvis open stack overflow" in query):
            stackoverflowurl = "https://www.stackoverflow.com/questions/"
            os.startfile(stackoverflowurl)
        elif("jarvis open instagram" in query):
            instagramurl = "https://www.instagram.com/"
            os.startfile(instagramurl)
