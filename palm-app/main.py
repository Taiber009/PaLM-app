from dotenv import load_dotenv
import os
import google.generativeai as palm
load_dotenv()
palm.configure(api_key=os.getenv("PALM_API_KEY"))


try:
    print("Ручной ввод активирован. Консольные запросы поддерживают сообщения с конекстом ('context'|'messages') и без него ('messages'). \
    \nДля использования контекста пишите его в начале запроса и выделите знаком '|'.")
    text = str(input("Напишите вашу команду для PaLM на английском языке:\n"))
    splited = text.split('|')
    while True:
        if len(splited) == 2:
            con = splited[0]
            mes = splited[1]
            print(palm.chat(context=con,messages=mes).last)
        elif len(splited) == 1:
            print(palm.chat(messages=text).last)
        else:
            pass
        print('\n\n\n')
        text = str(input("Напишите вашу команду для PaLM на английском языке:\n"))
except Exception as e:
    print(f"Ошибка ручного ввода! Консоль упала! Причина: \
        {str(e) if e.args.__len__() else 'Неизвестно, нет Exception'}\n")