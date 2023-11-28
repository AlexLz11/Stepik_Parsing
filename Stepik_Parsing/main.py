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

import re
pattern = re.compile('hello')
result = pattern.match('hello world')
print(result.group(1))