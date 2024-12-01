import os
import speech_recognition as sr

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:
        return "None"

    return query.lower() #type: ignore



while True:

    wake_up = takecommand()


    if 'wake up jarvis' in wake_up:
        os.startfile('D:\\Devesh\\Coding\\Main Projects\\Jarvis\\jarvis.py')

    else:
        print("Not able to start!")