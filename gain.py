import speech_recognition 
import pyttsx3
import time
from fun import *

engine = pyttsx3.init()

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
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        try:
            audio = recognizer.listen(mic)
            query = recognizer.recognize_google(audio, language='ru-RU').lower() 
            return query
        except speech_recognition.UnknownValueError:
            return 'не удалось распознать речь'
        except speech_recognition.RequestError:
            return 'произошла ошибка соединения'

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
       