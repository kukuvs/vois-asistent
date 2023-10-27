import speech_recognition as sr
from glav_fun import *  # noqa: F403



dictionary = {
    'greeting': ['привет', 'здравствуй', 'здарова', 'здравствуйте'],
    'create_task': ['создать задачу', 'добавь задачу', 'добавить в список'],
    'dela': ['как дела', 'как поживаешь'],
    'googletime': ['загугли', 'найди в интернете'],
    'what_time': ['который час', 'сколько время'],
    'exit_program': ['закрыть', 'выйти', 'закрыть программу'],
    'openp': ['открой', 'аткрой'],
    'open_desktop': ['рабочий стол'],
    'telegram': ['напиши'],
    }

def recognize_speech():
    # Создаем объект Recognizer
    recognizer = sr.Recognizer()

    # Открываем микрофон для записи звука
    with sr.Microphone() as source:
        print("Говорите что-нибудь...")
        audio = recognizer.listen(source)

    try:
        # Распознаем речь с помощью Google Web Speech API
        recognized_text = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Вы сказали: {recognized_text}")
        return recognized_text
    except sr.UnknownValueError:
        print("Извините, не удалось распознать речь")
        recognize_speech()
    except sr.RequestError as e:
        print(f"Произошла ошибка при отправке запроса к Google Web Speech API: {e}")
        return None



def fiend(dictionary):
    recognized_text = recognize_speech()
    # Преобразуем распознанный текст в нижний регистр, чтобы сделать поиск регистронезависимым
    recognized_text = recognized_text.lower()

    # Поиск фразы в словаре
    for definition, keyword in dictionary.items():
        if recognized_text.lower() in keyword:
            globals()[definition]()
    # Если фраза не найдена, возвращаем сообщение об отсутствии совпадений
    return "Фраза не найдена в словаре"

if __name__ == "__main__":
    while True:
        fiend(dictionary)