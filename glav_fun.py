import random
import time
import keyboard
import os
import datetime
from main import recognize_speech
import sys
from selenium import webdriver
import pyttsx3

engine = pyttsx3.init()

#приветствие
def greeting():
    x = ('здравствуй','здравствуйте', 'приветствую', 'добрый день')
    z = random.choice(x)
    engine.say(z)
    engine.runAndWait()

#соклько время
def what_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    engine.say(current_time)
    engine.runAndWait()
    
#нажатие клафиш
def combo():
    x = recognize_speech()
    if x == "комбо 1":
        for i in "op":
            keyboard.send(str(i))



#закрыть помошникаop
def exit_program():
    sys.exit('Программа закрыта.')

#ответ на как дела
def dela():
    x = ('отлично', 'неплохо', 'легко', 'идеально', 'превосходно')
    z = random.choice(x)
    engine.say(z)
    engine.runAndWait()
    
#создание списка дел    
def create_task():
    engine.say('что добавим в список дел ?')
    engine.runAndWait()
    query = recognize_speech()

    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')

#гуглит
def googletime():
   print("Тыкаю")
   driver = webdriver.Chrome()
   driver.get("https://www.google.com/search?q=" + recognize_speech())
   time.sleep(2)
   print("Натыкал")
   
#откроет рабочий стол   
def open_desktop():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    os.startfile(desktop_path)
