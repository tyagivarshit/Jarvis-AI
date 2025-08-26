import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty( 'voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout = 10,phrase_time_limit = 5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again please")
            return "None"
        return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour <= 12):
        speak("Good morning.\nI am Jarvis AI. How may I help you?")
    elif(hour > 12 and hour < 18):
        speak("Good Afternoon.\nI am Jarvis AI. How may I help you?")
    else:
        speak("Good Evening.\nI am Jarvis AI. How may I help you?")

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        
    takecommand()
