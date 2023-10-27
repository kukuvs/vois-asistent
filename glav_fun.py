import random
import mouse
import time
import keyboard
import subprocess
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
def telegram():
    mouse.move(150, 63)
    mouse.click(button='left')
    
    engine.say("кому пишем?")
    engine.runAndWait()
    
    piop = recognize_speech()
    keyboard.write(str(piop))
    keyboard.send("ENTER")
    
    engine.say("что пишем?")
    engine.runAndWait()
    
    send = recognize_speech()
    print("это ты пишешь "+send)
    keyboard.write(str(send))
    keyboard.send("ENTER")
    

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
   
def openp():
    pass
    
   
#откроет рабочий стол   
def open_desktop():
    mouse.move(1919, 1079)
    mouse.click(button='left')
