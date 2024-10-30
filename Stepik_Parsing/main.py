# *******************************************************************************
# ***** Введение в pyrogram *****************************************************
# ******************************************************************************

# import pyrogram

# print(pyrogram.__version__)

# Первый запуск

# from pyrogram import Client
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "python_parsing"
# app = Client("my_session", api_id=api_id, api_hash=api_hash)


# def main():
#     with app:
#         all_messages = []
#         for message in app.get_chat_history(group_url, limit=100): # type: ignore
#             all_messages.append(message.text)

#         # Вывод сообщений на экран или сохранение в файл
#         for msg in all_messages:
#             print(msg)


# main()

# Первый запуск async

import asyncio
from pyrogram import Client
import json

with open('Stepik_Parsing/api_keys.json') as file:
    api_keys = json.load(file)

api_id = api_keys['api_id']
api_hash = api_keys['api_hash']
group_url = "python_parsing"

async def get_all_messages(app, group_url, limit=100):
    all_messages = []
    async for message in app.get_chat_history(group_url, limit=limit):
        all_messages.append(message.text)
    return all_messages

async def main():
    app = Client("my_session", api_id=api_id, api_hash=api_hash)
    async with app:
        messages = await get_all_messages(app, group_url, limit=100)
        for msg in messages:
            print(msg)

asyncio.run(main())
