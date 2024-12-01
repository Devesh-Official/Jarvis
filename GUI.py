from jarvisGUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import Main
import os
import webbrowser as web
import sys



class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        Main.TaskExe()

startExe = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.Start_btn.clicked.connect(self.startTask)
        self.gui.Quit_btn.clicked.connect(self.close)
        self.gui.chrome_btn.clicked.connect(self.chrome_app)
        self.gui.insta_btn.clicked.connect(self.insta_app)
        self.gui.youtube_btn.clicked.connect(self.yt_app)

    def chrome_app(self):
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")

    def yt_app(self):
        web.open("https://www.youtube.com/")

    def insta_app(self):
        web.open("https://www.instagram.com/")

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

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()

    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        label_time = "Time :" + time
        label_date = "Date :" + date

        self.gui.Time.setText(label_time)
        self.gui.Date.setText(label_date)



GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())