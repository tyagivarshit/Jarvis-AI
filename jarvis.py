import sys
import time
from sys import exception

import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import webbrowser
import pywhatkit
import smtplib
import sys
import pyjokes

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tyagivarshit98@gmail.com','rsdt unbf qzge cokz')
    server.sendmail('tyagivarshit98@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower()
        #Logic building begins here
        if("jarvis open windows explorer" in query):
            npath = "C:\\Windows\\explorer.exe"
            os.startfile(npath)
        elif("jarvis close windows explorer" in query):
            speak("Closing windows explorer")
            os.system("taskkill /f /im explorer.exe")
        elif("jarvis open google" in query):
            speak("sir , what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")
        elif("jarvis close the google" in query):
            speak("closing google sir")
            os.system("taskkill /f /im chrome.exe")
        elif("jarvis open brave" in query):
            bravepath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravepath)
        elif("jarvis close brave" in query):
            speak("closing brave sir")
            os.system("taskkill /f /im brave.exe")
        elif("jarvis open vs code" in query):
            vspath = "C:\\Users\\tyagi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)
        elif("jarvis close vs code" in query):
            speak("closing vs code sir")
            os.system("taskkill /f /im vscode.exe")
        elif("jarvis open camera" in query):
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
        elif("jarvis close spotify" in query):
            speak("Closing spotify sir")
            os.system("taskkill /f /im spotify.exe")
        elif("jarvis open youtube" in query):
            speak("sir , what content do you want to search in youtube")
            cm = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query= {cm}")
        elif("jarvis close youtube" in query):
            speak("Closing youtube")
            os.system("taskkill /f /im chrome.exe")
        elif "jarvis tell me my ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your IP is: {ip} ")
        elif("jarvis open gpt" in query):
            cpath = "https:www.chatgpt.com/"
            os.startfile(cpath)
        elif("jarvis close gpt" in query):
            speak("Closing gpt")
            os.system("taskkill /f /im chrome.exe")
        elif("jarvis open facebook" in query):
            facebookurl = "https://www.facebook.com/"
            os.startfile(facebookurl)
        elif("jarvis close facebook" in query):
            speak("Closing facebook")
            os.system("taskkill /f /im chrome.exe")
        elif("jarvis open stack overflow" in query):
            stackoverflowurl = "https://www.stackoverflow.com/questions/"
            os.startfile(stackoverflowurl)
        elif("jarvis close stack overflow" in query):
            speak("Closing stack overflow")
            os.system("taskkill /f /im chrome.exe")
        elif("jarvis open instagram" in query):
            instagramurl = "https://www.instagram.com/"
            os.startfile(instagramurl)
        elif("jarvis close instagram" in query):
            speak("Closing instagram")
            os.system("taskkill /f /im chrome.exe")
        elif("jarvis send message" in query):
            pywhatkit.sendwhatmsg("+919389999437" ,"hehehehehe kya krre  " ,1,5)
        elif("jarvis close whatsapp" in query):
            speak("Closing whatsapp")
            os.system("taskkill /f /im chrome.exe")
        elif("jarvis play songs on youtube" in query):
            pywhatkit.playonyt("dhakka")
        elif("jarvis close youtube" in query):
            speak("Closing youtube")
            os.system("taskkill /f /im chrome.exe")
        elif("send email to tyagi" in query):
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "tyagivarshit76@gmail.com"
                sendEmail(to, content)
                speak("email has sent to varshit tyagi.")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to do that")
        elif("no thanks" in query):
            speak("Thank you for using Jarvis AI , have a nice day")
            sys.exit()
        elif("jarvis shut down the system" in query):
            os.system("shutdown /s /t /c")
        elif("jarvis restart the system" in query):
            os.system("shutdown /r /t /c")
        elif("jarvis sleep the system" in query):
            os.system("rundl132.exe powrprof.dl1,SetSuspendState 0,1,0")
        elif("jarvis tell me a joke" in query):
            joke = pyjokes.get_joke()
            speak(joke)
        elif "jarvis set alarm" in query:
            speak("Sir, please tell me the time for the alarm in HH:MM format")
            alarm_time = takeCommand().lower()  # example: "07:30" ya "22:00"

            try:
                hour, minute = map(int, alarm_time.split(":"))
                speak(f"Alarm set in {hour}:{minute:02d}")

                while True:
                    now = datetime.datetime.now()
                    if now.hour == hour and now.minute == minute:
                        speak("Sir, alarm ringing now!")
                        music_file = r"C:\Users\Knife Brows.mp3"
                        os.startfile(music_file)
                        break
                    time.sleep(10)
            except:
                speak("Sorry sir, I could not understand the time format. Please say again.")
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        speak("sir do you have any other work?")
