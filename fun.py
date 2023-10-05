import os
import pyttsx3
import time
import datetime
import sys
import speech_recognition
from selenium import webdriver
import keyboard
from gain import *

engine = pyttsx3.init()
sr = speech_recognition.Recognizer()

engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

commands_list = {
    'greeting': ['привет', 'здравствуй', 'здарова', 'здравствуйте'],
    'create_task': ['создать задачу', 'добавь задачу', 'добавить в список'],
    'dela': ['как дела', 'как поживаешь'],
    'goodletime': ['загугли', 'найди в интернете'],
    'what_time': ['который час', 'сколько время'],
    'exit_program': ['закрыть', 'выйти', 'закрыть программу'],
    'openp': ['открой', 'аткрой']
    
}

def list_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(mic)
            audio = sr.listen(mic)
            query = sr.recognize_google(audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'ничего не понял'
    except speech_recognition.RequestError:
        return 'ошибка соединения'
    

def openp():
    engine.say('какую программу открыть?')
    engine.runAndWait()
    query = str(list_command())
    keyboard.send("Windows")
    time.sleep(3)
    keyboard.write(query)
    time.sleep(1)
    keyboard.send("Enter")


def what_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    engine.say(current_time)
    if current_time == '00:00':
        engine.say('It is midnight, time to go to bed.')


def goodletime():
   print("Starting search...")
   driver = webdriver.Chrome()
   driver.get("https://www.google.com/search?q=" + list_command())
   time.sleep(5)
   driver.quit()
   print("Search completed.")
   return "Search completed."


def exit_program():
    sys.exit('Программа закрыта.')


def dela():
    return 'Хорошо, а у тебя?'


def greeting():
    return 'привет'


def create_task():
    engine.say('что добавим в список дел ?')
    engine.runAndWait()
    query = list_command()

    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')

    return f'успешно добавлено: {query}'


def open_desktop():
    # Получим путь к рабочему столу
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    # Откроем рабочий стол (для Windows)
    os.startfile(desktop_path)

    return 'Открываю рабочий стол'


def main():
    query = list_command()
    print("Распознано: ", query)

    for k, v in commands_list.items():
        if query in v:
            result = globals()[k]()  # Вызов функции по имени из globals()
            engine.say(result)
            engine.say("пик")
            engine.runAndWait()
            print("Ответ: ", result)
            time.sleep(1)
            
            engine.runAndWait()
            
if __name__ == '__main__':
    while True:
        main()
        