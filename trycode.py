import sys
import webbrowser
import os
import time
import pyttsx3
import datetime
import json
import requests
import speech_recognition as sr
import wikipedia
import cv2
import random
from requests import get
import pywhatkit as kit
import smtplib
import pyjokes
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTime, QDate, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QMovie
from anksG import Ui_MainWindow
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class MainThread(QtCore.QThread):
    def __init__(self, output_box):
        super(MainThread, self).__init__()
        self.output_box = output_box

    def run(self):
        self.taskExecution()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # print("Listening..............")
            speak('listening ')
            r.energy_threshold = 4000
            audio = r.listen(source, timeout=5, phrase_time_limit=8)

        try:
            #print("................... ")
            speak('working on it  ')
            self.query = r.recognize_google(audio, language='en-in')
            user_input1 = self.query
            output_text = f"User said : {user_input1} \n"
            self.output_box.append(output_text)

        except sr.UnknownValueError:
            #print("Google Speech Recognition could not understand audio")
            speak("Sorry, I couldn't understand that. Please repeat.")
            return 'None'
        except sr.RequestError as e:
            #print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, I'm having trouble accessing the Google Speech Recognition service.")
            return 'None'
        except Exception as e:
            #print(f"An error occurred: {e}")
            speak("Sorry, an error occurred. Please try again.")
            return 'None'

        return self.query

    def sendEmail(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        eId = 'your_email@gmail.com'  # Replace with your email
        pswrd = 'your_password'  # Replace with your email password
        server.login(eId, pswrd)
        server.sendmail(eId, to, content)
        server.close()

    def news(self):
        main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'
        main_page = get(main_url).json()
        articles = main_page["articles"]
        head = []
        day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range(len(day)):
            speak(f"today,s {day[i]} news is: {head[i]}")

    def greet(self):
        hour = int(datetime.datetime.now().hour)
        tt = time.strftime("%I:%M %p")
        if hour >= 16:
            speak(f"good evening  sir  it's {tt}")
        elif hour >= 12:
            speak(f"good afternoon  sir  it's {tt}")
        else:
            speak(f"good morning  sir  it's {tt}")
        speak('please tell me how may i help you sir')

    def taskExecution(self):
        self.greet()
        while True:
            if 'seven':
                self.query = self.takecommand().lower()
                # intent = self.intent_recognition(self.query)
                # if intent == 'open_app':
                #     app_name = self.query.split()[-1]
                #     self.open_application(app_name)

                if 'search' in self.query and 'on google' in self.query:
                    query = ' '.join(self.query.split()[1:])
                    webbrowser.open(f"https://www.google.com/search?q={self.query}")

                sites = [['youtube', "https://www.youtube.com/"], ['spotify', "https://open.spotify.com/"],
                         ['erp', "https://student.gehu.ac.in/Account/Login"]]
                for site in sites:
                    if f'open {site[0]}' in self.query.lower():
                        self.speak(f'opening {site[0]} for you sir')
                        webbrowser.open(site[1])
                        exit()

                files = [['gallery', "C:\\Users\\ASUS\\Pictures"]]
                for file in files:
                    if f'open {file[0]}' in self.query.lower():
                        self.speak(f'opening {file[0]} for you sir')
                        os.startfile(file[1])
                        exit()
                if 'wikipedia' in self.query:
                    #print("searching wikipedia.........")
                    self.speak('searching wikipedia ')
                    self.query = self.query.replace("wikipedia", ' ')
                    results = wikipedia.summary(self.query, sentences=2)
                    self.speak("According to wikipedia ")
                    #print(results)
                    self.speak(results)
                elif "made you" in self.query or "created you" in self.query or "designed you" in self.query or "programmed you" in self.query:
                    self.speak("i was designed by Mr. Ankit wariyal ,Mr. Karan Yadav , Mr. Jagpreet Singh and Mr. Brijnath Mandal with the great technology of PYTHON")
                elif 'open youtube' in self.query:
                    self.speak('opening youtube for you sir')
                    webbrowser.open("https://www.youtube.com/")
                    exit()
                elif 'open spotify' in self.query:
                    self.speak('opening spotify for you sir')
                    webbrowser.open("https://open.spotify.com/")
                    exit()
                elif 'open erp' in self.query:
                    self.speak('opening erp portal for you sir')
                    webbrowser.open("https://student.gehu.ac.in/Account/Login")
                    exit()

                elif 'open google' in self.query:
                    self.speak("What would you like to search sir ")
                    qr = self.takecommand().lower()
                    webbrowser.open(f"{qr}")
                    exit()

                elif 'play music' in self.query or 'play song' in self.query:
                    music_dir = 'C:\\Users\\ASUS\\Music'
                    songs = os.listdir(music_dir)

                    self.speak('playing for you sir')
                    #print(songs)
                    rs = random.choice(songs)
                    os.startfile(os.path.join(music_dir, rs))
                    exit()

                elif 'open notepad' in self.query:
                    npath = "C:\\Windows\\System32\\notepad.exe"
                    os.startfile(npath)

                elif 'open command prompt' in self.query:
                    os.system("start cmd")

                elif 'open camera' in self.query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(10)
                        if k == 2:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                elif "weather" in self.query:
                    self.speak("say the city for which you want the weather information sir ")
                    city = self.takecommand()
                    ukey = '5d86f3bed97c496aaf841251232611'
                    url = f'https://api.weatherapi.com/v1/current.json?key={ukey}&q={city}'
                    r = requests.get(url)
                    # print(r.text)
                    wdict = json.loads(r.text)
                    # print(wdict)
                    temp_c = wdict['current']['temp_c']
                    humidity = wdict['current']['humidity']
                    # print(f"There is {temp_c} degree celcious temperature in {city} with humidity {humidity}")
                    self.speak(f"there is {temp_c} degree celcious temperature in {city} with humidity {humidity}")

                elif "ip address" in self.query:
                    ip = get("https://api.ipify.org").text
                    self.speak(f" your ip address is {ip}")
                    #print(f"IP address : {ip}")

                # elif "switch the window" in self.query or "switch window" in self.query:
                #     pyautogui.hotkey('alt', 'tab')

                # elif "copilot" in self.query:
                #     pyautogui.hotkey("win", 'c')

                elif "tell me news" in self.query:
                    self.speak("please wait sir, fetching the latest news")
                    self.news()

                elif "send message" in self.query:
                    self.speak("please speak out the number ")
                    nm = self.takecommand().lower()
                    self.speak("Please speak out the message sir")
                    msg = self.takecommand().lower()
                    hr = str(datetime.datetime.now().time())[:2]
                    hr = int(hr)
                    mn = str(datetime.datetime.now().time())[3:5]
                    mn = int(mn) + 1
                    kit.sendwhatmsg(f"+91{nm}", msg, hr, mn)

                elif "play" in self.query and "youtube" in self.query:
                    self.speak("What would you like to play on youtube sir ")
                    ttl = self.takecommand().lower()
                    kit.playonyt(ttl)

                elif "close notepad" in self.query:
                    self.speak("okay sir, closing notepad")
                    os.system("taskkill /f /im notepad.exe")

                elif "set alarm" in self.query:
                    nn = int(datetime.datetime.now().hour)
                    if nn == 22:
                        music_dir = "E:\\music"
                        songs = os.listdir(music_dir)
                        os.startfile(os.path.join(music_dir, songs[0]))

                elif "tell me a joke" in self.query:
                    joke = pyjokes.get_joke()
                    self.speak(joke)

                elif "shut down the system" in self.query:
                    os.system("shutdown /s /t 5")

                elif "restart the system" in self.query:
                    os.system("shutdown /r /t 5")

                elif "sleep the system" in self.query:
                    os.system("rundll32.exe powprof.dll,SetSuspendedState 0,1,0")

                elif 'time' in self.query:
                    hour = str(datetime.datetime.now().time())[:8]
                    #print(hour)
                    self.speak(hour)

                elif 'quit' in self.query or 'exit' in self.query or 'stop' in self.query:
                    self.speak('thank you for using me sir ')
                    self.speak('bye   bye')
                    exit()

                else:
                    url = "http://api.brainshop.ai/get?bid=157984&key=3S0hhLXZ5GS2KYs4&uid=[uid]&msg=[{}]".format(
                        self.query)
                    response = requests.get(url).json()['cnt']
                    #print(response)
                    self.speak(response)

    def speak(self, text):  # New method to handle speaking and displaying in output_box
        self.output_box.append(f"JAKUB : {text}")
        speak(text)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.speak_button.clicked.connect(self.startTask)
        self.ui.movie = QtGui.QMovie(r"C:\Users\ASUS\Downloads\YcsK.gif")
        self.ui.output_box.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.stop_button.clicked.connect(self.close)


    def startTask(self):
        self.thread = MainThread(output_box=self.ui.output_box)
        self.thread.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.thread.start()



    def showTime(self):
        cur_time = QTime.currentTime()
        cur_date = QDate.currentDate()
        label_time = cur_time.toString('hh:mm:ss')
        label_date = cur_date.toString(Qt.ISODate)
        self.ui.input_box1.setText(label_date)
        self.ui.input_box2.setText(label_time)


app = QApplication(sys.argv)
jakub = Main()
jakub.show()
sys.exit(app.exec_())