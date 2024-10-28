# *******************************************************************************
# ***** Введение в pyrogram *****************************************************
# ******************************************************************************

# import pyrogram

# print(pyrogram.__version__)

from pyrogram import Client

api_id = 25779997
api_hash = "93c2608907a0ed17a4fa0973bcc65ee3"
group_url = "python_parsing"
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        all_messages = []
        for message in app.get_chat_history(group_url, limit=100): # type: ignore
            all_messages.append(message.text)

        # Вывод сообщений на экран или сохранение в файл
        for msg in all_messages:
            print(msg)


main()