### PART 04 BeautifulSoup ####
#*************************************
# import requests
# from bs4 import BeautifulSoup
# html = """
# <html>
#     <head>
#         <title>Мой сайт</title>
#     </head>
#     <body>
#         <div class="content">
#             <p>Привет, мир!</p>
#         </div>
#     </body>
# </html>
# """
# soup = BeautifulSoup(html, 'html.parser')
# title_tag = soup.title
# print(title_tag.text)  # Выведет: Мой сайт

# *** .text и .get_text()
# from bs4 import BeautifulSoup

# # Пример HTML-строки
# html_string = """
# <div>
#     <p>Первый абзац.</p>
#     <p>Второй абзац <span>со вложенным</span> текстом.</p>
# </div>
# """

# # Создание объекта BeautifulSoup
# soup = BeautifulSoup(html_string, 'html.parser')

# # Использование .text для извлечения всего текста из div
# div_text = soup.find('div').text

# print(div_text)

# ht = '''
# <div>
#     <p>Пример</p>
#     <p>Текст</p>
# </div>
# '''
# soup = BeautifulSoup(ht, 'html.parser')
# dt = soup.find('div').get_text(separator=" | ", strip=True)
# print(dt)

# from bs4 import BeautifulSoup

# # Тот же пример HTML-строки
# html_string = """
# <div>
#     <p>Первый абзац.</p>
#     <p>Второй абзац <span>со вложенным</span> текстом.</p>
# </div>
# """

# # Создание объекта BeautifulSoup
# soup = BeautifulSoup(html_string, 'html.parser')

# # Использование .get_text() с параметром separator
# div_text = soup.find('div').get_text(separator='|')

# print(div_text)

# import re
# pattern = re.compile('hello')
# result = pattern.match('hello world')
# print(result.group(1))

# 4.3.1 Поиск тега по значению атрибута
# import requests
# from bs4 import BeautifulSoup

# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     tag = soup.find('li', {'data-gpu': 'nVidia GeForce RTX 4060'})
#     if tag:
#         return tag.text
#     return None

# url = 'https://parsinger.ru/4.1/1/index3.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# print(get_html(html.text))

# 4.3.2 Поиск тега по пользовательскому атрибуту
# import requests
# from bs4 import BeautifulSoup

# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     li_tag = soup.find('li', {'data-key': 'cooling_system'}).text
#     if li_tag:
#         return li_tag
#     return None

# url = 'https://parsinger.ru/4.1/1/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# print(get_html(html.text))

# 4.3.3 Извлечение тега <img>
# import requests
# from bs4 import BeautifulSoup

# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     img = soup.find('img')
#     if img:
#         return print(img['alt'])
#     return None

# url = 'https://parsinger.ru/4.1/1/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# get_html(html.text)

# 4.3.4 Получение тега с двойным классом
# import requests
# from bs4 import BeautifulSoup

# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     li_tag = soup.find(class_='description detailz').text
#     if li_tag:
#         return print(li_tag)
#     return None

# url = 'https://parsinger.ru/4.1/1/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# get_html(html.text)

# 4.3.5 Сложный поиск по всем атрибутам и значениям
# import requests
# from bs4 import BeautifulSoup

# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     tag = soup.find(attrs={
#         'class': ['description_detail', 'class1', 'class2', 'class3'],
#         'data-fdg45': 'value13',
#         'data-54dfg60': 'value14',
#         'data-d6f50hg': 'value15'
#     })
#     if tag:
#         return print(tag.text, type(tag))
#     return print('Not exist')

# url = 'https://parsinger.ru/4.1/1/index2.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# get_html(html.text)