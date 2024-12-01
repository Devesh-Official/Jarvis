import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, QTimer, QTime, QDate
from PyQt5.QtGui import QMovie
from PyQt5 import QtGui, QtWidgets
from JarvisUI import Ui_MainWindow  
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
from playsound import playsound
import wikipedia
from pywikihow import search_wikihow
import webbrowser
import pywhatkit
from googletrans import Translator
import pyautogui as pi
import keyboard
from gtts import gTTS
import requests
import time as t
import speedtest
from bs4 import BeautifulSoup
import random
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[2].id)
engine.setProperty('rate', 170)


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        TaskExe()


startExe = MainThread()


class Gui_Start(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.Quit_btn = QPushButton('', self)
        self.Quit_btn.clicked.connect(self.closeEvent)
        self.Quit_btn.setGeometry(1500, 340, 371, 81)
        self.Quit_btn.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        

        self.gui.Start_btn.clicked.connect(self.startTask)
        self.gui.chrome_btn.clicked.connect(self.chrome_app)
        self.gui.insta_btn.clicked.connect(self.insta_app)
        self.gui.youtube_btn.clicked.connect(self.yt_app)

    def chrome_app(self):
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")

    def yt_app(self):
        webbrowser.open("https://www.youtube.com/")

    def insta_app(self):
        webbrowser.open("https://www.instagram.com/")

    def startTask(self):
        self.gui.label1 = QtGui.QMovie("G.U.I Material//B.G//Iron_Template_1.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("G.U.I Material//ExtraGui//live.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("G.U.I Material//ExtraGui//Earth.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("G.U.I Material//ExtraGui//initial.gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()
        
        self.gui.label5 = QtGui.QMovie("G.U.I Material//ExtraGui//Health_Template.gif")
        self.gui.Health_gif.setMovie(self.gui.label5)
        self.gui.label5.start()
        
        self.gui.label6 = QtGui.QMovie("G.U.I Material//ExtraGui//Code_Template.gif")
        self.gui.Code_gif.setMovie(self.gui.label6)
        self.gui.label6.start()
        
        self.gui.label7 = QtGui.QMovie("G.U.I Material//VoiceReg//__1.gif")
        self.gui.Voice.setMovie(self.gui.label7)  
        self.gui.label7.start()

        startExe.start()



        

    


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            pass

  


def Speak(Text):
    print("   ")
    print(f": {Text}")
    engine.say(Text)
    print("    ")
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        Speak("Good morning Sir!")

    elif hour >= 12 and hour <= 17:
        Speak("Good afternoon Sir!")

    else:
        Speak("Good evening Sir!")

    Speak("Ready to help, what can i do for you ?")

def Music():
        Speak("Tell me the name of the song")
        MusicName = takecommand()

        if 'desi haan ji' in MusicName:
         os.startfile("D:\\Devesh\\songs mp3\\Desi Haan Ji.mp3")   

        elif 'dabya koni karde' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Dabya Ni Karde.mp3")
        
        elif 'jai veeroo' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Jai Veeru - Slow Version.mp3")
        
        elif 'jhotte' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Jhotte.mp3")
        
        elif 'yaar badmash' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Yaar Badmash.mp3")
        
        elif 'yadav brand 2' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Yadav Brand 2.mp3")
        
        elif 'yaar harayana te' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Yaar Haryane Te.mp3")
        
        elif 'harayanan hood' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Haryana Hood Slow + Reverb.mp3")

        else:
            pywhatkit.playonyt(MusicName)
            Speak("Enjoy sir!")

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

def TaskExe():

    wishMe()

    def Music(): 
        Speak("Tell me the name of the song")
        MusicName = takecommand()

        if 'desi haan ji' in MusicName:
         os.startfile("D:\\Devesh\\songs mp3\\Desi Haan Ji.mp3")   

        elif 'dabya koni karde' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Dabya Ni Karde.mp3")
        
        elif 'jai veeroo' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Jai Veeru - Slow Version.mp3")
        
        elif 'jhotte' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Jhotte.mp3")
        
        elif 'yaar badmash' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Yaar Badmash.mp3")
        
        elif 'yadav brand 2' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Yadav Brand 2.mp3")
        
        elif 'yaar harayana te' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Yaar Haryane Te.mp3")
        
        elif 'harayanan hood' in MusicName:
            os.startfile("D:\\Devesh\\songs mp3\\Haryana Hood Slow + Reverb.mp3")

        else:
            pywhatkit.playonyt(MusicName)
            Speak("Enjoy sir!")

    def OpenApps():
        Speak("Ok Sir , Wait A Second!")

        if 'code' in query:
            os.startfile("C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your Command Has Been Completed Sir!")

    def SpeedTest():
        import speedtest
        Speak("Checking...")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUpload = int(uploading/800000)

        if 'uploading' in query:
            Speak(f"The uploading speed is: {correctUpload} mb per second")

        elif 'downloading' in query:
            Speak(f"The downloading speed is: {correctDown} mb per second")

        else:
            Speak(f"The speed downloading is {correctDown} mb per second and uploading speed is {correctUpload} mb per second")

    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        Speak("Your Command Has Been Succesfully Completed!")

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'resume' in comm:
            keyboard.press('space bar')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")

    def ChromeAuto():
        Speak("Chrome Automation started!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')

    def screenshot():
        Speak("Ok sir, what should i name the file?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "C:\\Users\\opdev\\OneDrive\\Pictures\\Screenshots" + path1name
        ss = pi.screenshot()
        ss.save(path1)
        os.startfile("C:\\Users\\opdev\\OneDrive\\Pictures\\Screenshots")
        Speak("Done! Here is your screenshot.")

    def temp():
        search = "temperature in jaipur"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The temperature outside is {temperature} celcius")


    while True:
        query = takecommand().lower()

        if 'jarvis' in query:
            Speak("yes Sir")

        elif 'bye bro' in query:
            Speak("Bye Sir, you can call me any time")
            Speak("Just say, Wake up Jarvis")
            break

        elif 'who are you' in query:
            Speak("My name is jarvis.")
            Speak("I can do everything that my creator programmed me.")

        elif 'who created you' in query:
            Speak("I was created by Devesh Kumar and Yanshu Saini.")

        elif 'what is' in query:
            Speak("Searching Wikipedia...")
            query = query.replace("what is", "")
            result = wikipedia.summary(query, sentences = 2)
            Speak(f"According to Wikipedia {result}")

        elif 'who is' in query:
            Speak("Searching Wikipedia...")
            query = query.replace("who is", "")
            result = wikipedia.summary(query, sentences = 2)
            Speak(f"According to Wikipedia {result}")

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'search google' in query:
            Speak("What should i search?")
            qry = takecommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences = 1)
            Speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'open paint' in query:
            pi.press('win')
            t.sleep(1)
            pi.typewrite('paint')
            t.sleep(1)
            pi.press('enter')

        elif 'close paint' in query:
            os.system("taskkill /f /im mspaint.exe")

        elif 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")

        elif 'open cmd' in query:
            os.system("start cmd")

        elif 'launch devesh folder' in query:
            path = "D:\Devesh"
            path = os.path.realpath(path)
            os.startfile(path)

        elif 'close cmd' in query:
            os.system("taskkill /f /im cmd.exe")

        elif 'music' in query:
            Music()

        elif 'tell me the time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M')
            Speak(f"Sir, the time is {strtime} minutes")

        elif 'shutdown laptop' in query:
            Speak("Ok Sir!")
            os.system("shutdown /s /t 5")

        elif 'lock laptop' in query:
            Speak("Ok Sir!")
            os.system("rundll32.exe prowprof.dll, SetSuspendState 0, 1, 0")

        elif 'take screenshot' in query:
            screenshot()

        elif 'my ip address' in query:
            Speak("Checking...")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                Speak(f"Your ip address is {ipAdd}")
            except Exception as e:
                Speak("due to some issue i am not able to find your ip address")

        elif 'volume plus' in query:
            pi.press("volumeup")
            pi.press("volumeup")

        elif 'volume down' in query:
            pi.press("volumedown")
            pi.press("volumedown")

        elif 'mute' in query:
            pi.press("volumemute")

        elif 'unmute' in query:
            pi.press("volumemute")

        elif 'type' in query:
            query = query.replace("type", "")
            pi.typewrite(f"{query}", 0.1)

        elif 'youtube search' in query:
            pi.hotkey('win')
            t.sleep(0.5)
            pi.typewrite('google chrome', 0.2)
            t.sleep(3)
            pi.press('enter')
            t.sleep(2)
            pi.hotkey('alt', 'd')
            t.sleep(0.5)
            pi.typewrite('youtube.com', 0.2)
            pi.press('enter')
            t.sleep(7)
            pi.press('tab')
            pi.press('tab')
            pi.press('tab')
            pi.press('tab')
            Speak("What should i search")
            qrey = takecommand().lower()
            pi.typewrite(qrey, 0.1)
            pi.press('enter')

        elif 'open venom tech' in query:
            pi.hotkey('ctrl', 't')
            t.sleep(0.5)
            pi.hotkey('alt', 'd')
            t.sleep(0.5)
            pi.typewrite('youtube.com', 0.1)
            pi.press('enter')
            t.sleep(5)
            pi.press('tab')
            pi.press('tab')
            pi.press('tab')
            pi.press('tab')
            pi.typewrite('venom tech', 0.1)
            pi.press('enter')
            t.sleep(3)
            pi.click(941, 284)
            t.sleep(3)
            pi.click(624, 615)

        elif 'open hungry birds' in query:
            pi.hotkey('ctrl', 't')
            t.sleep(0.5)
            pi.hotkey('alt', 'd')
            t.sleep(0.5)
            pi.typewrite('youtube.com', 0.1)
            pi.press('enter')
            t.sleep(5)
            pi.press('tab')
            pi.press('tab')
            pi.press('tab')
            pi.press('tab')
            pi.typewrite('hungry birds', 0.1)
            pi.press('enter')
            t.sleep(3)
            pi.click(941, 284)
            t.sleep(3)
            pi.click(624, 615)

        elif 'open byjus xcel' in query:
            pi.hotkey('ctrl', 't')
            t.sleep(0.5)
            pi.hotkey('alt', 'd')
            t.sleep(0.5)
            pi.typewrite('https://byjus.com/byjus-xcel/', 0.1)
            pi.press('enter')

        elif 'open web store' in query:
            pi.hotkey('ctrl', 't')
            t.sleep(0.5)
            pi.hotkey('alt', 'd')
            t.sleep(0.5)
            pi.typewrite('https://chrome.google.com/webstore', 0.2)
            pi.press('enter')

        elif 'tell me internet downloading speed' in query:
            SpeedTest()

        elif 'tell me internet uploading speed' in query:
            SpeedTest()

        elif 'tell me the internet speed' in query:
            SpeedTest()

        elif 'chrome automation' in query:
            ChromeAuto()
            
        elif "open" in query:   
                query = query.replace("open","")
                query = query.replace("jarvis","")
                pi.press("super")
                pi.typewrite(query)
                pi.sleep(5)
                pi.press("enter")  

        elif 'pause' in query:
            keyboard.press('k')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'resume' in query:
            keyboard.press('k')

        elif 'open code with harry' in query:
            pi.hotkey('ctrl', 't')
            time.sleep(0.5)
            pi.hotkey('alt', 'd')
            time.sleep(0.5)
            pi.typewrite('youtube.com', 0.1)
            pi.press('enter')
            time.sleep(5)
            pi.press('tab')
            pi.press('tab')
            pi.press('tab')
            pi.press('tab')
            pi.typewrite('CodeWithHarry', 0.1)
            pi.press('enter')
            time.sleep(5)
            pi.click(941, 284)
            time.sleep(3)
            pi.click(624, 615)

        elif 'youtube automation' in query:
            YoutubeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'histry' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'start web clock' in query:
            os.startfile('index1.html')

        elif 'alarm' in query:
            Speak("Enter the time!")
            time = input("Enter the time: ")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up sir!")
                    playsound('ring.mp3')
                    Speak("Alarm Stopped!")

                elif now > time:
                    break

        elif 'remember that' in query:
            rememberMsg = query.replace("remember that", "")
            rememberMsg = query.replace("jarvis", "")
            Speak("You tell me to remind you that: "+ rememberMsg)
            remember = open('data.txt', 'w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query:
            remember = open('data.txt', 'r')
            Speak("You tell that"+remember.read())

        elif 'google scrap search' in query:
            import wikipedia as googleScrape
            query = query.replace("jarvis", "")
            query = query.replace("google scrape search", "")
            query = query.replace("google", "")
            Speak("This is what i found on the web")
            pywhatkit.search(query)

            try:
                pywhatkit.search(query)
                result = googleScrape.summary(query, 3)
                Speak(result)

            except:
                Speak("No speakable data available")

        elif 'temperature' in query:
            temp()

        elif 'how to' in query:
            Speak("Getting data from the internet...")
            op = query.replace("jarvis", "")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)



def main():
    GuiApp = QApplication(sys.argv)
    jarvis_gui = Gui_Start()
    jarvis_gui.show()
    sys.exit(GuiApp.exec_())


if __name__ == "__main__":
    main()

