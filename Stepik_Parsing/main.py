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
# from bs4 import BeautifulSoup

# html_doc = """
# <!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
#     <title>Пример карточки товара</title>
# </head>
# <body>
#     <div class="card">
#         <img src="image.jpg" alt="Пример изображения товара">
#         <h2 class="card-title"> iPhone 15 </h2>
#         <p class="card-description">Аппаратной основой Apple iPhone 15 Pro Max стал 3-нанометровый чипсет A17 Pro с 6-ядерным GPU и поддержкой трассировки лучей.</p>
#         <p class="card-price">999 999 руб.</p>
#         <a href="https://example.com/product-link" class="card-link">Подробнее</a>
#     </div>
# </body>
# </html>
# """

# def main ():
#     soup = BeautifulSoup(html_doc, 'html.parser')
#     p_description = soup.find('p', class_='card-description').text
#     print(p_description)

# main()

# 4.4.2 Суммируйте значение всех артикулов
# from bs4 import BeautifulSoup

# html_doc = """
# <!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
# </head>
# <body>
#     <div class="cards">
#         <!-- Карточка товара 1 -->
#         <div class="card">
#             <img src="parsing.png" alt="WEB Парсинг на Python">
#             <h2 class="card-title">WEB Парсинг на Python</h2>
#             <p class="card-articul">Артикул: 104774</p>
#             <p class="card-stock">Наличие: 5 шт.</p>
#             <p class="card-price">3500 руб.</p>
#             <a href="https://stepik.org/a/104774" class="card-button">Купить</a>
#         </div>
#         <!-- Карточка товара 2 -->
#         <div class="card">
#             <img src="async.png" alt="Асинхронный Python">
#             <h2 class="card-title">Асинхронный Python</h2>
#             <p class="card-articul">Артикул: 170777</p>
#             <p class="card-stock">Наличие: 10 шт.</p>
#             <p class="card-price">3500 руб.</p>
#             <a href="https://stepik.org/a/170777" class="card-button">Купить</a>
#         </div>
#         <!-- Карточка товара 3 -->
#         <div class="card">
#             <img src="selenium.PNG" alt="Selenium Python">
#             <h2 class="card-title">Selenium Python</h2>
#             <p class="card-articul">Артикул: 119495</p>
#             <p class="card-stock">Наличие: 5 шт.</p>
#             <p class="card-price">1250 руб.</p>
#             <a href="https://stepik.org/a/119495" class="card-button">Купить</a>
#         </div>
#     </div>
# </body>
# </html>
# """
# def main ():
#     # Инициализация объекта BeautifulSoup
#     soup = BeautifulSoup(html_doc, 'html.parser')

#     # Поиск всех элементов с классом 'card-articul'
#     articuls = [int(i.text.strip('Артикул: ')) for i in soup.select('p.card-articul')]

#     # Извлечение числовых значений артикулов и их суммирование
#     sum_articuls = sum(articuls)

#     print(f"Сумма артикулов: {sum_articuls}")  # Вывод результата
# main()

# 4.4.3 Суммируйте значения alt всех img на странице
# from bs4 import BeautifulSoup

# html_doc = """
# <!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
# </head>
# <body>

# <div class="card">
#     <h2>Товар 1</h2>
#     <img src="parsing.png" alt="779966">
#     <p>Цена: 1000 руб.</p>
#     <p>Описание: Отличный товар, изготовлен из качественных материалов.</p>
#     <p>Технические характеристики: Размеры: 10x10x10 см, Вес: 1 кг.</p>
#     <p>Доступные размеры: S, M, L</p>
#     <p>Отзывы: 5 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 3000 руб.</p>
#     <a href="https://stepik.org/a/104774" class="btn">Купить</a>
# </div>

# <div class="card">
#     <h2>Товар 2</h2>
#     <img src="async.png" alt="331155">
#     <p>Цена: 1500 руб.</p>
#     <p>Описание: Превосходный товар, подходит для повседневного использования.</p>
#     <p>Технические характеристики: Размеры: 15x15x15 см, Вес: 1.5 кг.</p>
#     <p>Доступные размеры: M, L, XL</p>
#     <p>Отзывы: 4.5 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 5000 руб.</p>
#     <a href="https://stepik.org/a/170777" class="btn">Купить</a>
# </div>

# <div class="card">
#     <h2>Товар 3</h2>
#     <img src="parsing.png" alt="558877">
#     <p>Цена: 2000 руб.</p>
#     <p>Описание: Удобный товар для дома и офиса.</p>
#     <p>Технические характеристики: Размеры: 12x12x12 см, Вес: 1.2 кг.</p>
#     <p>Доступные размеры: S, M</p>
#     <p>Отзывы: 4.7 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 3500 руб.</p>
#     <a href="https://stepik.org/a/104774" class="btn">Купить</a>
# </div>

# <div class="card">
#     <h2>Товар 4</h2>
#     <img src="async.png" alt="449933">
#     <p>Цена: 2500 руб.</p>
#     <p>Описание: Стильный и практичный товар.</p>
#     <p>Технические характеристики: Размеры: 14x14x14 см, Вес: 1.4 кг.</p>
#     <p>Доступные размеры: L, XL</p>
#     <p>Отзывы: 4.8 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 4000 руб.</p>
#     <a href="https://stepik.org/a/170777" class="btn">Купить</a>
# </div>

# <div class="card">
#     <h2>Товар 5</h2>
#     <img src="parsing.png" alt="667711">
#     <p>Цена: 2700 руб.</p>
#     <p>Описание: Идеальный товар для повседневного использования.</p>
#     <p>Технические характеристики: Размеры: 13x13x13 см, Вес: 1.3 кг.</p>
#     <p>Доступные размеры: M, L, XL</p>
#     <p>Отзывы: 4.9 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 4500 руб.</p>
#     <a href="https://stepik.org/a/104774" class="btn">Купить</a>
# </div>

# <div class="card">
#     <h2>Товар 6</h2>
#     <img src="async.png" alt="334455">
#     <p>Цена: 3000 руб.</p>
#     <p>Описание: Прочный и надежный товар.</p>
#     <p>Технические характеристики: Размеры: 16x16x16 см, Вес: 1.6 кг.</p>
#     <p>Доступные размеры: S, M</p>
#     <p>Отзывы: 5 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 5000 руб.</p>
#     <a href="https://stepik.org/a/170777" class="btn">Купить</a>
# </div>


# </body>
# </html>
# """


# def main():
#     # Инициализация объекта BeautifulSoup
#     soup = BeautifulSoup(html_doc, 'html.parser')

#     # Находим все теги img
#     img_tags = soup.find_all('img', alt=True)

#     # Извлекаем значения атрибута alt и суммируем их
#     total_sum = sum([int(tag['alt']) for tag in img_tags])

#     print(f"Сумма всех значений в атрибуте alt тега img: {total_sum}")

# main()

# 4.4.4 Суммируйте атрибуты только у тегов <p> четной длины
from bs4 import BeautifulSoup

html ='''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тестовая страница для веб-парсинга</title>
</head>
<body>
    <p id="435456" class="123984">Веб-парсинг – это мощный инструмент для анализа данных в интернете.</p>
    <p id="284359" class="493572">Python предоставляет отличные библиотеки для парсинга веб-страниц.</p>
    <p id="789234" class="293487">Для начинающих веб-парсеров важно изучить основы HTML и CSS.</p>
    <p id="239048" class="392874">Библиотека BeautifulSoup позволяет легко извлекать данные с веб-страниц.</p>
    <p id="923874" class="120948">Scrapy – другой популярный фреймворк для веб-парсинга на Python.</p>
    <p id="982374" class="302984">Веб-парсинг может помочь аналитикам и маркетологам собирать ценную информацию.</p>
    <p id="238940" class="238492">Соблюдение законов и правил при парсинге веб-сайтов – это ключевой момент.</p>
    <p id="923485" class="283947">Ограничения robots.txt могут влиять на возможность парсинга некоторых сайтов.</p>
    <p id="293847" class="394872">Динамические веб-сайты могут требовать использование Selenium для парсинга.</p>
    <p id="239487" class="238492">Регулярные выражения могут быть полезными при извлечении специфических данных.</p>
    <p id="203984" class="394872">При веб-парсинге важно учитывать нагрузку на целевой веб-сайт.</p>
    <p id="394872" class="203984">Кэширование данных может ускорить процесс парсинга и снизить нагрузку на сервер.</p>
    <p id="238492" class="394872">Прокси-сервера могут помочь обойти ограничения, связанные с IP-адресом.</p>
    <p id="239847" class="238947">Парсинг может быть автоматизирован с помощью планировщика задач.</p>
    <p id="394872" class="238492">Обработка ошибок – важный этап в разработке парсера.</p>
    <p id="238492" class="394872">Сохранение данных в базу данных позволяет легко анализировать и обрабатывать информацию.</p>
    <p id="293847" class="203984">Многопоточность может значительно ускорить процесс парсинга веб-сайтов.</p>
    <p id="394872" class="203984">Веб-парсинг – это не только технический процесс, но и аналитический навык.</p>
    <p id="293847" class="394872">Изучение веб-парсинга открывает новые возможности для исследования интернета.</p>
    <p id="238947" class="238492">Качественный парсер требует тщательной проработки и тестирования.</p>
    <p id="384756" class="293487">Парсинг веб-страниц – это процесс извлечения данных с онлайн-ресурсов.</p>
    <p id="238947" class="293487">Python стал популярным языком для веб-парсинга благодаря своей простоте и богатой экосистеме.</p>
    <p id="384756" class="238492">Знание структуры HTML и CSS сделает вас более эффективным веб-парсером.</p>
    <p id="238947" class="238492">BeautifulSoup предоставляет удобные методы для поиска и извлечения данных из HTML-документов.</p>
    <p id="384756" class="293487">Scrapy облегчает парсинг множества страниц и управление запросами.</p>
    <p id="238947" class="293487">Веб-парсинг помогает в анализе конкурентов и рынка для бизнеса.</p>
    <p id="384756" class="238492">Соблюдение этичных и юридических норм важно при веб-парсинге.</p>
    <p id="238947" class="238492">Файл robots.txt указывает правила доступа для веб-краулеров и парсеров.</p>
    <p id="384756" class="293487">Selenium полезен для парсинга динамических веб-сайтов с JavaScript.</p>
    <p id="238947" class="293487">Регулярные выражения могут быть мощным инструментом для извлечения данных из текста.</p>
    <p id="384756" class="238492">Оптимизация запросов и паузы важны для избежания блокировки при парсинге.</p>
    <p id="238947" class="238492">Кэширование данных улучшает производительность парсера и снижает нагрузку.</p>
    <p id="384756" class="293487">Использование прокси-серверов помогает в обходе ограничений по IP-адресу.</p>
    <p id="238947" class="293487">Автоматизация парсинга с помощью планировщика может сэкономить время.</p>
    <p id="384756" class="238492">Обработка и логирование ошибок важны для стабильной работы парсера.</p>
    <p id="238947" class="238492">Сохранение данных в базу данных обеспечивает их долгосрочное хранение и анализ.</p>
    <p id="384756" class="293487">Многопоточность увеличивает скорость парсинга и снижает время выполнения задач.</p>
    <p id="238947" class="293487">Веб-парсинг требует аналитического мышления и понимания данных.</p>
    <p id="384756" class="238492">Изучение веб-парсинга расширяет возможности для исследования интернета и данных.</p>
    <p id="238947" class="238492">Разработка качественного парсера – это процесс, требующий тщательной проработки и тестирования.</p>
    <p id="384756" class="293487">Извлечение данных из веб-страницы – ключевой этап в анализе интернет-контента.</p>
    <p id="238947" class="293487">Python предоставляет множество возможностей для работы с текстом и данными.</p>
    <p id="384756" class="238492">Оптимизация запросов и управление скоростью парсинга – залог успешного сбора данных.</p>
    <p id="238947" class="238492">Использование кэширования может значительно снизить нагрузку на серверы и ускорить работу парсера.</p>
    <p id="384756" class="293487">Прокси-сервера – надежный способ обойти ограничения по IP и повысить анонимность.</p>
    <p id="238947" class="293487">Автоматизация задач с помощью планировщика обеспечивает регулярное обновление данных.</p>
    <p id="384756" class="238492">Обработка ошибок и их логирование помогают выявить проблемы и улучшить стабильность парсера.</p>
    <p id="238947" class="238492">Сохранение данных в базе обеспечивает их сохранность и возможность дальнейшего анализа.</p>
    <p id="384756" class="293487">Использование многопоточности позволяет параллельно обрабатывать множество страниц.</p>
    <p id="238947" class="293487">Веб-парсинг – это искусство анализа и извлечения информации из виртуального мира.</p>
    <p id="384756" class="238492">Изучение веб-парсинга даёт возможность исследовать интернет в поисках ценных данных.</p>
    <p id="238947" class="238492">Разработка парсера – это непрерывный процесс улучшения и оптимизации.</p>
    <p id="384756" class="293487">API предоставляют более удобный способ доступа к данным, чем парсинг страниц.</p>
    <p id="238947" class="293487">XPath – мощный инструмент для навигации и извлечения данных из XML и HTML.</p>
    <p id="384756" class="238492">Парсинг данных из JSON позволяет эффективно работать с данными в этом формате.</p>
    <p id="238947" class="238492">Анализ времени выполнения запросов помогает оптимизировать парсинг и снизить нагрузку.</p>
    <p id="384756" class="293487">Эффективный веб-парсинг требует понимания принципов работы HTTP-протокола.</p>
    <p id="238947" class="293487">Системы управления версиями помогают отслеживать изменения в коде парсера.</p>
    <p id="384756" class="238492">Интеграция с облачными хранилищами данных облегчает анализ собранных данных.</p>
    <p id="238947" class="238492">Аналитика и визуализация данных помогают получить ценные инсайты из собранных информационных ресурсов.</p>
    <p id="384756" class="293487">Понимание DOM-структуры помогает эффективно навигировать по веб-страницам.</p>
    <p id="238947" class="293487">Python имеет богатую экосистему для анализа данных, что делает его отличным выбором для парсинга.</p>
    <p id="384756" class="238492">Контроль частоты запросов позволяет избегать блокировок со стороны серверов.</p>
    <p id="238947" class="238492">Использование регулярных выражений требует навыков и практики, но может быть мощным инструментом.</p>
    <p id="384756" class="293487">Прокси-сервера могут быть необходимы для работы с сайтами, блокирующими IP-адреса.</p>
    <p id="238947" class="293487">Планировщики задач помогают автоматизировать процесс парсинга по расписанию.</p>
    <p id="384756" class="238492">Обработка ошибок включает в себя исключения и стратегии восстановления парсера.</p>
    <p id="238947" class="238492">Сохранение данных в базе обеспечивает надежное хранение и возможность долгосрочного анализа.</p>
    <p id="384756" class="293487">Использование многопоточности может значительно ускорить процесс сбора данных.</p>
    <p id="238947" class="293487">Веб-парсинг помогает исследователям извлекать информацию из различных источников.</p>
    <p id="384756" class="238492">Разработка парсера требует тщательного планирования и тестирования функциональности.</p>
    <p id="238947" class="238492">Интеграция с RESTful API облегчает получение данных с веб-серверов.</p>
    <p id="384756" class="293487">XPath позволяет точно находить и извлекать элементы на веб-странице.</p>
    <p id="238947" class="293487">JSON является удобным форматом для передачи и хранения данных при парсинге.</p>
    <p id="384756" class="238492">Мониторинг и управление ресурсами помогают избежать перегрузки серверов.</p>
    <p id="238947" class="293487">Знание структуры URL важно для формирования правильных запросов.</p>
    <p id="384756" class="293487">Веб-парсинг может использоваться для сравнения цен на товары и услуги.</p>
    <p id="238947" class="238492">Эффективный парсер должен быть адаптирован к особенностям целевых веб-сайтов.</p>
    <p id="384756" class="293487">Интеграция с базами данных позволяет хранить и анализировать большие объемы данных.</p>
    <p id="238947" class="238492">Аналитика данных позволяет выявить тенденции и паттерны в собранных информационных ресурсах.</p>
</body>
</html>
'''

def sum_even_length_ids(html):
    soup = BeautifulSoup(html, 'html.parser')
    p_tags = [tag for tag in soup.find_all('p', id=True, class_=True) if len(tag.text.replace(' ', '')) % 2 == 0]
    total_id_sum = total_class_sum = 0
    print(p_tags)
    for tag in p_tags:
        total_id_sum += int(tag['id'])
        total_class_sum += int(tag['class'][0])
    return print(f"Сумма ID и CLASS тегов <p> с чётной длиной текста без пробелов: {total_id_sum + total_class_sum}")


sum_even_length_ids(html)