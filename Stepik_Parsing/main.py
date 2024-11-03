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

# import asyncio
# from pyrogram import Client
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "python_parsing"

# async def get_all_messages(app, group_url, limit=100):
#     all_messages = []
#     async for message in app.get_chat_history(group_url, limit=limit):
#         all_messages.append(message.text)
#     return all_messages

# async def main():
#     app = Client("my_session", api_id=api_id, api_hash=api_hash)
#     async with app:
#         messages = await get_all_messages(app, group_url, limit=100)
#         for msg in messages:
#             print(msg)

# asyncio.run(main())

# ****** Основные методы *********
# ********************************
# [1] app.get_chat(chat_id): Получает информацию о чате по его идентификатору или имени пользователя.

# from pyrogram import Client
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "parsinger_pyrogram"

# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     with app:
#         chat = app.get_chat(group_url)
#         print('Chat Info:', chat)

# main()

# [2] app.get_chat_members(chat_id, query, limit, filter): Получает список участников чата или группы.
# from pyrogram import Client, enums
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "parsinger_pyrogram"
# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     query = 'John'
#     limit = 10
#     filter = enums.ChatMembersFilter.ADMINISTRATORS
#     with app:
#         members = app.get_chat_members(group_url, query=query, limit=limit, filter=filter)
#         for member in members:
#             print(member.user.first_name, member.user.id)

# if __name__ == '__main__':
#     main()

# [3] app.get_chat_member(chat_id, user_id): Получает информацию об определенном участнике чата или группы.
# from pyrogram import Client
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "parsinger_pyrogram"
# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     user_id = '@HybridAppParser51'
#     with app:
#         member = app.get_chat_member(group_url, user_id=user_id)
#         print(member)

# if __name__ == '__main__':
#     main()

# app.get_messages(chat_id, message_ids, reply_to_message_ids, replies): 
# Используется для получения одного или нескольких сообщений из чата.
# from pyrogram import Client
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "parsinger_pyrogram"
# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     with app:
#         messages = app.get_messages(group_url, 
#         message_ids=[123, 456, 789], 
#         reply_to_message_ids=[321], 
#         replies=5)
#         print(messages)

# if __name__ == '__main__':
#     main()

# [5] app.search_messages(chat_id, query, offset, filter, limit, from_user): 
# Ищет сообщения в чате или группе по определенным критериям.

# from pyrogram import Client, enums
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']

# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     chat_id = "Parsinger_Telethon_Test"  # Используйте ID чата или его имя пользователя
#     query = "Python"                      # Текст для поиска в сообщениях
#     offset = 0                           # Начать с самого первого сообщения
#     filter = enums.MessagesFilter.PHOTO  # Искать только сообщения с фотографиями
#     limit = 100                          # Ограничить результаты поиском первых 100 сообщений
#     from_user = "@vladimir_might"              # Искать сообщения только от определенного пользователя
#     with app:
#         for message in app.search_messages(
#             chat_id=chat_id,
#             query=query,
#             offset=offset,
#             # filter=filter,
#             limit=limit,
#             from_user=from_user):
#             print(message.text)

# if __name__ == '__main__':
#     main()

# [6] app.get_chat_history(chat_id, limit, offset, offset_id, offset_date): 
# Получает историю сообщений из чата или группы.

# from pyrogram import Client, enums
# from datetime import datetime
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "parsinger_pyrogram"

# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     with app:
#         limit = 100
#         offset = 0
#         offset_id = 0
#         offset_date = datetime(2023, 11, 8)
#         for message in app.get_chat_history(group_url, limit=limit, offset=offset, offset_id=offset_id, offset_date=offset_date):
#             print(message.text)

# if __name__ == '__main__':
#     main()

# [7] app.get_chat_photos(chat_id, limit): Получает фотографии профиля чата или группы.

# from pyrogram import Client
# from datetime import datetime
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "Parsinger_Telethon_Test"

# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     with app:
#         chat_photos = app.get_chat_photos(group_url)
#         for photo in chat_photos:
#             app.download_media(photo.file_id, file_name=f'photos/{photo.file_id}.jpg')

# if __name__ == '__main__':
#     main()

# 7.3.1. Исследователь структур и точечной нотации

# from pyrogram import Client
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "parsinger_pyrogram"

# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     with app:
#         chat = app.get_chat(group_url)
#         with open('Stepik_Parsing/chat_data.json', 'w') as file:
#             print(chat, file=file)

# main()

# 7.3.2. В поисках идентификатора чата

# from pyrogram import Client
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "parsinger_pyrogram"

# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     with app:
#         chat = app.get_chat(group_url)
#         print(chat.id)

# main()

# 7.3.3. Поиск уникального идентификатора аватара группы

# from pyrogram import Client
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "parsinger_pyrogram"

# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     with app:
#         chat = app.get_chat(group_url)
#         print(chat.photo.big_photo_unique_id)

# main()

# 7.3.4. Охота за сокровищами в цифровых глубинах

# from pyrogram import Client
# import json

# with open('Stepik_Parsing/api_keys.json') as file:
#     api_keys = json.load(file)

# api_id = api_keys['api_id']
# api_hash = api_keys['api_hash']
# group_url = "parsinger_pyrogram"

# def main():
#     app = Client('my_session', api_id=api_id, api_hash=api_hash)
#     with app:
#         chat = app.get_chat(group_url)
#         description = chat.description
#         jem = ''.join([x for x in description if x.isdigit() and int(x)>0 and int(x)%2 == 0])
#         print(jem)

# main()

# 7.3.5. Сборщик идентификаторов
from pyrogram import Client
import json

with open('Stepik_Parsing/api_keys.json') as file:
    api_keys = json.load(file)

api_id = api_keys['api_id']
api_hash = api_keys['api_hash']
group_url = "parsinger_pyrogram"

def main():
    app = Client('my_session', api_id=api_id, api_hash=api_hash)
    with app:
        members_ids = [member.user.id for member in app.get_chat_members(group_url)]
        print(sum(members_ids))

if __name__ == '__main__':
    main()