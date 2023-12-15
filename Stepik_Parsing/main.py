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
# get_html(html.text)git 

# 4.3.6 Одновременный поиск и извлечение название товара
# import requests
# from bs4 import BeautifulSoup

# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     tags = [el.get_text(strip=True) for el in soup.find_all('a', class_='name_item product_name')]
#     for tag in tags:
#         print(tag)

# url = 'https://parsinger.ru/4.1/1/index4.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# get_html(html.text)

# 4.3.7 Суммирование цен на странице
# import requests
# from bs4 import BeautifulSoup

# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     count = sum(map(lambda x: int(''.join([i for i in x if i.isdigit()])), [pr.text for pr in soup.find_all('p', class_='price product_price')]))
    
#     return count

# url = 'https://parsinger.ru/4.1/1/index4.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# print(get_html(html.text))

# 4.3.8 Поиск всех идентификаторов у тегов <li>
# import requests
# from bs4 import BeautifulSoup

# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     tags_li = soup.find_all('li', id=True)
#     for tag in tags_li:
#         print(tag['id'])

# url = 'https://parsinger.ru/4.1/1/index4.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# get_html(html.text)

# 4.3.9 .previous_sibling и .next_sibling
# import requests
# from bs4 import BeautifulSoup
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     sibling = soup.find('p', string='Текст раздела 3').next_sibling


#     return sibling

# url = 'https://parsinger.ru/4.1/1/index6.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# print(get_html(html.text))

# 4.3.10 .previous_sibling и .next_sibling
# import requests
# from bs4 import BeautifulSoup
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     emails = [elem.next_sibling.strip() for elem in soup.select('.email_field strong')]

#     return emails

# url = 'https://parsinger.ru/4.1/1/index5.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# print(get_html(html.text))

# 4.4.0 Получите HTML разметку из файла index.html
# from bs4 import BeautifulSoup
# import lxml

# with open('Stepik_Parsing/index.html', encoding='utf-8') as inf:
#     soup = BeautifulSoup(inf, 'lxml')
# print(soup)

# 4.4.1 Извлеките текст из тега
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Пример карточки товара</title>
</head>
<body>
    <div class="card">
        <img src="image.jpg" alt="Пример изображения товара">
        <h2 class="card-title"> iPhone 15 </h2>
        <p class="card-description">Аппаратной основой Apple iPhone 15 Pro Max стал 3-нанометровый чипсет A17 Pro с 6-ядерным GPU и поддержкой трассировки лучей.</p>
        <p class="card-price">999 999 руб.</p>
        <a href="https://example.com/product-link" class="card-link">Подробнее</a>
    </div>
</body>
</html>
"""

def main ():
    soup = BeautifulSoup(html_doc, 'html.parser')
    p_description = soup.find('p', class_='card-description').text
    print(p_description)

main()