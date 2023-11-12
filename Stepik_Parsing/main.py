# import requests
# from bs4 import BeautifulSoup

# # Отправляем GET-запрос на веб-страницу
# url = 'http://parsinger.ru/2.1/DOM/index2.html'
# response = requests.get(url)
# response.encoding = 'utf-8'

# # Проверяем статус-код ответа
# if response.status_code == 200:
    
#     # Инициализируем объект BeautifulSoup для парсинга HTML
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Ищем элемент с ID "text777"
#     target_element = soup.find(id="text777")

#     # Извлекаем текст из найденного элемента
#     if target_element:
#         extracted_text = target_element.text
#         print(f"Извлеченный текст: {extracted_text}")  # Вывод на экран
#     else:
#         print("Элемент с ID 'text777' не найден.")
# else:
#     print(f"Не удалось получить доступ к странице, статус-код: {response.status_code}")

# response = requests.get(url='http://httpbin.org/')
# print(type(response))

# import requests

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml', 'Connection': 'keep-alive'}
# # URL для примеров
# url = "https://httpbin.org/user-agent"

# # Выполняем GET-запрос
# response = requests.get(url, headers=headers)

# # status_code: HTTP-код статуса ответа.
# print("HTTP-код статуса ответа:", response.status_code)

# # text: Текстовое представление содержимого ответа.
# print("Текстовое содержимое ответа:", response.text)

# # content: Содержимое ответа в виде байтов.
# print("Содержимое ответа в виде байтов:", response.content)

# # json: Метод для десериализации JSON-ответа.
# json_response = response.json()
# print("Десериализованный JSON-ответ:", json_response)

# # headers: Заголовки HTTP, возвращаемые сервером.
# print("Заголовки HTTP:", response.headers)

# # url: Исходный URL-адрес, на который был выполнен запрос.
# print("Исходный URL-адрес запроса:", response.url)

# # encoding: Кодировка ответа.
# print("Кодировка ответа:", response.encoding)

# # elapsed: Время, затраченное на выполнение запроса.
# print("Время выполнения запроса:", response.elapsed)

# # cookies: Куки, возвращаемые сервером.
# print("Куки, возвращаемые сервером:", response.cookies)

# # history: Список объектов Response, представляющих историю перенаправлений.
# print("История перенаправлений:", response.history)

# # ok: Логический атрибут, указывающий, был ли запрос успешным (коды 2xx).
# print("Запрос успешен (коды 2xx):", response.ok)

# # reason: Сообщение статуса HTTP (например, "OK", "Not Found").
# print("Сообщение статуса HTTP:", response.reason)

# import requests
# from random import choice

# url = 'http://httpbin.org/user-agent'

# with open('user_agent.txt') as file:
#     lines = file.read().split('\n')

# for line in lines:
#     user_agent = {'user-agent': choice(lines)}
#     response = requests.get(url=url, headers=user_agent)
#     print(response.text)

# import requests
# import time
# from requests.exceptions import Timeout, ProxyError

# url = 'http://httpbin.org/get'

# proxies = {
#     'http': 'http://200.12.55.90:80',
#     'https': 'http://200.12.55.90:80'
# }
# start = time.perf_counter()
# try:
#     requests.get(url=url, proxies=proxies)
# except (Timeout, ProxyError) as _ex:
#     print(_ex, time.perf_counter() - start)

from fake_useragent import UserAgent

ua = UserAgent()
print(type(ua))