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
# from bs4 import BeautifulSoup

# html ='''<!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
#     <title>Тестовая страница для веб-парсинга</title>
# </head>
# <body>
#     <p id="435456" class="123984">Веб-парсинг – это мощный инструмент для анализа данных в интернете.</p>
#     <p id="284359" class="493572">Python предоставляет отличные библиотеки для парсинга веб-страниц.</p>
#     <p id="789234" class="293487">Для начинающих веб-парсеров важно изучить основы HTML и CSS.</p>
#     <p id="239048" class="392874">Библиотека BeautifulSoup позволяет легко извлекать данные с веб-страниц.</p>
#     <p id="923874" class="120948">Scrapy – другой популярный фреймворк для веб-парсинга на Python.</p>
#     <p id="982374" class="302984">Веб-парсинг может помочь аналитикам и маркетологам собирать ценную информацию.</p>
#     <p id="238940" class="238492">Соблюдение законов и правил при парсинге веб-сайтов – это ключевой момент.</p>
#     <p id="923485" class="283947">Ограничения robots.txt могут влиять на возможность парсинга некоторых сайтов.</p>
#     <p id="293847" class="394872">Динамические веб-сайты могут требовать использование Selenium для парсинга.</p>
#     <p id="239487" class="238492">Регулярные выражения могут быть полезными при извлечении специфических данных.</p>
#     <p id="203984" class="394872">При веб-парсинге важно учитывать нагрузку на целевой веб-сайт.</p>
#     <p id="394872" class="203984">Кэширование данных может ускорить процесс парсинга и снизить нагрузку на сервер.</p>
#     <p id="238492" class="394872">Прокси-сервера могут помочь обойти ограничения, связанные с IP-адресом.</p>
#     <p id="239847" class="238947">Парсинг может быть автоматизирован с помощью планировщика задач.</p>
#     <p id="394872" class="238492">Обработка ошибок – важный этап в разработке парсера.</p>
#     <p id="238492" class="394872">Сохранение данных в базу данных позволяет легко анализировать и обрабатывать информацию.</p>
#     <p id="293847" class="203984">Многопоточность может значительно ускорить процесс парсинга веб-сайтов.</p>
#     <p id="394872" class="203984">Веб-парсинг – это не только технический процесс, но и аналитический навык.</p>
#     <p id="293847" class="394872">Изучение веб-парсинга открывает новые возможности для исследования интернета.</p>
#     <p id="238947" class="238492">Качественный парсер требует тщательной проработки и тестирования.</p>
#     <p id="384756" class="293487">Парсинг веб-страниц – это процесс извлечения данных с онлайн-ресурсов.</p>
#     <p id="238947" class="293487">Python стал популярным языком для веб-парсинга благодаря своей простоте и богатой экосистеме.</p>
#     <p id="384756" class="238492">Знание структуры HTML и CSS сделает вас более эффективным веб-парсером.</p>
#     <p id="238947" class="238492">BeautifulSoup предоставляет удобные методы для поиска и извлечения данных из HTML-документов.</p>
#     <p id="384756" class="293487">Scrapy облегчает парсинг множества страниц и управление запросами.</p>
#     <p id="238947" class="293487">Веб-парсинг помогает в анализе конкурентов и рынка для бизнеса.</p>
#     <p id="384756" class="238492">Соблюдение этичных и юридических норм важно при веб-парсинге.</p>
#     <p id="238947" class="238492">Файл robots.txt указывает правила доступа для веб-краулеров и парсеров.</p>
#     <p id="384756" class="293487">Selenium полезен для парсинга динамических веб-сайтов с JavaScript.</p>
#     <p id="238947" class="293487">Регулярные выражения могут быть мощным инструментом для извлечения данных из текста.</p>
#     <p id="384756" class="238492">Оптимизация запросов и паузы важны для избежания блокировки при парсинге.</p>
#     <p id="238947" class="238492">Кэширование данных улучшает производительность парсера и снижает нагрузку.</p>
#     <p id="384756" class="293487">Использование прокси-серверов помогает в обходе ограничений по IP-адресу.</p>
#     <p id="238947" class="293487">Автоматизация парсинга с помощью планировщика может сэкономить время.</p>
#     <p id="384756" class="238492">Обработка и логирование ошибок важны для стабильной работы парсера.</p>
#     <p id="238947" class="238492">Сохранение данных в базу данных обеспечивает их долгосрочное хранение и анализ.</p>
#     <p id="384756" class="293487">Многопоточность увеличивает скорость парсинга и снижает время выполнения задач.</p>
#     <p id="238947" class="293487">Веб-парсинг требует аналитического мышления и понимания данных.</p>
#     <p id="384756" class="238492">Изучение веб-парсинга расширяет возможности для исследования интернета и данных.</p>
#     <p id="238947" class="238492">Разработка качественного парсера – это процесс, требующий тщательной проработки и тестирования.</p>
#     <p id="384756" class="293487">Извлечение данных из веб-страницы – ключевой этап в анализе интернет-контента.</p>
#     <p id="238947" class="293487">Python предоставляет множество возможностей для работы с текстом и данными.</p>
#     <p id="384756" class="238492">Оптимизация запросов и управление скоростью парсинга – залог успешного сбора данных.</p>
#     <p id="238947" class="238492">Использование кэширования может значительно снизить нагрузку на серверы и ускорить работу парсера.</p>
#     <p id="384756" class="293487">Прокси-сервера – надежный способ обойти ограничения по IP и повысить анонимность.</p>
#     <p id="238947" class="293487">Автоматизация задач с помощью планировщика обеспечивает регулярное обновление данных.</p>
#     <p id="384756" class="238492">Обработка ошибок и их логирование помогают выявить проблемы и улучшить стабильность парсера.</p>
#     <p id="238947" class="238492">Сохранение данных в базе обеспечивает их сохранность и возможность дальнейшего анализа.</p>
#     <p id="384756" class="293487">Использование многопоточности позволяет параллельно обрабатывать множество страниц.</p>
#     <p id="238947" class="293487">Веб-парсинг – это искусство анализа и извлечения информации из виртуального мира.</p>
#     <p id="384756" class="238492">Изучение веб-парсинга даёт возможность исследовать интернет в поисках ценных данных.</p>
#     <p id="238947" class="238492">Разработка парсера – это непрерывный процесс улучшения и оптимизации.</p>
#     <p id="384756" class="293487">API предоставляют более удобный способ доступа к данным, чем парсинг страниц.</p>
#     <p id="238947" class="293487">XPath – мощный инструмент для навигации и извлечения данных из XML и HTML.</p>
#     <p id="384756" class="238492">Парсинг данных из JSON позволяет эффективно работать с данными в этом формате.</p>
#     <p id="238947" class="238492">Анализ времени выполнения запросов помогает оптимизировать парсинг и снизить нагрузку.</p>
#     <p id="384756" class="293487">Эффективный веб-парсинг требует понимания принципов работы HTTP-протокола.</p>
#     <p id="238947" class="293487">Системы управления версиями помогают отслеживать изменения в коде парсера.</p>
#     <p id="384756" class="238492">Интеграция с облачными хранилищами данных облегчает анализ собранных данных.</p>
#     <p id="238947" class="238492">Аналитика и визуализация данных помогают получить ценные инсайты из собранных информационных ресурсов.</p>
#     <p id="384756" class="293487">Понимание DOM-структуры помогает эффективно навигировать по веб-страницам.</p>
#     <p id="238947" class="293487">Python имеет богатую экосистему для анализа данных, что делает его отличным выбором для парсинга.</p>
#     <p id="384756" class="238492">Контроль частоты запросов позволяет избегать блокировок со стороны серверов.</p>
#     <p id="238947" class="238492">Использование регулярных выражений требует навыков и практики, но может быть мощным инструментом.</p>
#     <p id="384756" class="293487">Прокси-сервера могут быть необходимы для работы с сайтами, блокирующими IP-адреса.</p>
#     <p id="238947" class="293487">Планировщики задач помогают автоматизировать процесс парсинга по расписанию.</p>
#     <p id="384756" class="238492">Обработка ошибок включает в себя исключения и стратегии восстановления парсера.</p>
#     <p id="238947" class="238492">Сохранение данных в базе обеспечивает надежное хранение и возможность долгосрочного анализа.</p>
#     <p id="384756" class="293487">Использование многопоточности может значительно ускорить процесс сбора данных.</p>
#     <p id="238947" class="293487">Веб-парсинг помогает исследователям извлекать информацию из различных источников.</p>
#     <p id="384756" class="238492">Разработка парсера требует тщательного планирования и тестирования функциональности.</p>
#     <p id="238947" class="238492">Интеграция с RESTful API облегчает получение данных с веб-серверов.</p>
#     <p id="384756" class="293487">XPath позволяет точно находить и извлекать элементы на веб-странице.</p>
#     <p id="238947" class="293487">JSON является удобным форматом для передачи и хранения данных при парсинге.</p>
#     <p id="384756" class="238492">Мониторинг и управление ресурсами помогают избежать перегрузки серверов.</p>
#     <p id="238947" class="293487">Знание структуры URL важно для формирования правильных запросов.</p>
#     <p id="384756" class="293487">Веб-парсинг может использоваться для сравнения цен на товары и услуги.</p>
#     <p id="238947" class="238492">Эффективный парсер должен быть адаптирован к особенностям целевых веб-сайтов.</p>
#     <p id="384756" class="293487">Интеграция с базами данных позволяет хранить и анализировать большие объемы данных.</p>
#     <p id="238947" class="238492">Аналитика данных позволяет выявить тенденции и паттерны в собранных информационных ресурсах.</p>
# </body>
# </html>
# '''

# def sum_even_length_ids(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     p_tags = [tag for tag in soup.find_all('p', id=True, class_=True) if len(tag.text.replace(' ', '')) % 2 == 0]
#     total_id_sum = total_class_sum = 0
#     print(p_tags)
#     for tag in p_tags:
#         total_id_sum += int(tag['id'])
#         total_class_sum += int(tag['class'][0])
#     return print(f"Сумма ID и CLASS тегов <p> с чётной длиной текста без пробелов: {total_id_sum + total_class_sum}")


# sum_even_length_ids(html)

# 4.5.1 Рассчитывайте общую стоимость всех товаров
# from bs4 import BeautifulSoup

# html ='''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Онлайн Магазин Книг</title>
# </head>
# <body>
#     <div class="book-card">
#         <img src="1.png" alt="Обложка книги 1" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 1</h2>
#         <p class="book-author">Автор: Автор 1</p>
#         <p class="book-isbn">ISBN: 978-1234567890</p>
#         <p class="book-cover-type">Обложка: Твердая</p>
#         <p class="count price">Цена: $20.00</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 300</p>
#         <p class="count stock">Количество на складе: 75</p>
#         <p class="book-publisher">Издательство: Издательство 1</p>
#         <p class="book-publication-date">Дата публикации: 01.01.2023</p>
#         <p class="count rating">Рейтинг: 4.5</p>
#         <p class="book-genre">Жанр: Роман</p>
#         <p class="book-language">Язык: Английский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 1.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="2.png" alt="Обложка книги 2" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 2</h2>
#         <p class="book-author">Автор: Автор 2</p>
#         <p class="book-isbn">ISBN: 978-9876543210</p>
#         <p class="book-cover-type">Обложка: Мягкая</p>
#         <p class="count price">Цена: $18.50</p>
#         <p class="book-format">Формат: Электронная версия (e-book)</p>
#         <p class="count pages">Количество страниц: 250</p>
#         <p class="count stock">Количество на складе: 119</p>
#         <p class="book-publisher">Издательство: Издательство 3</p>
#         <p class="book-publication-date">Дата публикации: 20.03.2023</p>
#         <p class="count rating">Рейтинг: 4.7</p>
#         <p class="book-genre">Жанр: Детская литература</p>
#         <p class="book-language">Язык: Французский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 2.</p>
#          <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="3.png" alt="Обложка книги 3" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 3</h2>
#         <p class="book-author">Автор: Автор 3</p>
#         <p class="book-isbn">ISBN: 978-0987654321</p>
#         <p class="book-cover-type">Обложка: Твердая</p>
#         <p class="count price">Цена: $25.00</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 400</p>
#         <p class="count stock">Количество на складе: 216</p>
#         <p class="book-publisher">Издательство: Издательство 2</p>
#         <p class="book-publication-date">Дата публикации: 15.02.2023</p>
#         <p class="count rating">Рейтинг: 4.8</p>
#         <p class="book-genre">Жанр: Фантастика</p>
#         <p class="book-language">Язык: Русский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 3.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="4.png" alt="Обложка книги 4" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 4</h2>
#         <p class="book-author">Автор: Автор 4</p>
#         <p class="book-isbn">ISBN: 978-5432109876</p>
#         <p class="book-cover-type">Обложка: Твердая</p>
#         <p class="count price">Цена: $22.00</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 350</p>
#         <p class="count stock">Количество на складе: 17</p>
#         <p class="book-publisher">Издательство: Издательство 4</p>
#         <p class="book-publication-date">Дата публикации: 10.04.2023</p>
#         <p class="count rating">Рейтинг: 4.9</p>
#         <p class="book-genre">Жанр: Детектив</p>
#         <p class="book-language">Язык: Английский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 4.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="5.png" alt="Обложка книги 5" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 5</h2>
#         <p class="book-author">Автор: Автор 5</p>
#         <p class="book-isbn">ISBN: 978-8765432109</p>
#         <p class="book-cover-type">Обложка: Мягкая</p>
#         <p class="count price">Цена: $19.50</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 280</p>
#         <p class="count stock">Количество на складе: 63</p>
#         <p class="book-publisher">Издательство: Издательство 5</p>
#         <p class="book-publication-date">Дата публикации: 05.05.2023</p>
#         <p class="count rating">Рейтинг: 4.6</p>
#         <p class="book-genre">Жанр: Фэнтези</p>
#         <p class="book-language">Язык: Испанский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 5.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
# </body>
# </html>
# '''

# def calculate_total_price(html: str) -> float:
#     # Инициализация BeautifulSoup.
#     soup = BeautifulSoup(html, 'html.parser')
#     total = 0
#     for book in soup.select('div.book-card'):
#         price = float(book.select_one('p.count.price').text.strip('Цена: $'))
#         qt = int(book.select_one('p.count.stock').text.strip('Количество на складе: '))
#         total += price * qt
#     return total

# total = calculate_total_price(html)
# print(f"Общая стоимость в случае продажи всех товаров: ${total}")

# 4.5.5 Открываем сайт
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/html/index1_page_1.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'html.parser')
# prices = [int(tag.text.strip(' руб')) for tag in soup.select('.price')]
# print(sum(prices))

# 4.5.6 Открываем сайт
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/html/hdd/4/4_1.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'html.parser')
# new_pr = int(soup.find(id='price').text.strip(' руб'))
# old_pr = int(soup.find(id='old_price').text.strip(' руб'))
# print((old_pr - new_pr) * 100 / old_pr)

# 4.6.1 Извлечение названий товаров с веб-сайта
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/html/index3_page_1.html'
# html_pg = requests.get(url)
# soup = BeautifulSoup(html_pg.text, 'html.parser')
# ln = 'https://parsinger.ru/html/'
# links = [ln + tag['href'] for tag in soup.select_one('div.pagen').select('a')]
# goods_name = []
# for link in links:
#     html = requests.get(str(link))
#     html.encoding = 'utf-8'
#     soup = BeautifulSoup(html.text, 'html.parser')
#     names = [tag.text for tag in soup.select('a.name_item')]
#     goods_name.append(names)
# print(goods_name)

# 4.6.2 Парсинг артикулов товаров с веб-сайта
# import requests
# from bs4 import BeautifulSoup

# def get_article(n):
#     url = f'https://parsinger.ru/html/mouse/3/3_{n}.html'
#     html = requests.get(url)
#     html.encoding = 'utf-8'
#     soup = BeautifulSoup(html.text, 'lxml')
#     article = soup.find('p', class_='article').text.split()[1]
#     return int(article)
# print(sum([get_article(i) for i in range(1, 33)]))

# 4.6.3 Комплексное извлечение стоимости товаров
# import requests
# from bs4 import BeautifulSoup

# def get_soup(url):
#     html = rs.get(url)
#     html.encoding = 'utf-8'
#     return BeautifulSoup(html.text, 'lxml')

# url = 'https://parsinger.ru/html/index1_page_1.html'
# with requests.Session() as rs:
#     soup = get_soup(url)
#     url = 'https://parsinger.ru/html/'
#     total = 0
#     for lc in soup.find('div', 'nav_menu').select('a'):
#         soup = get_soup(url + lc['href'])
#         for lp in soup.find('div', 'pagen').select('a'):
#             soup = get_soup(url+lp['href'])
#             for lg in soup.select('a.name_item'):
#                 soup = get_soup(url+lg['href'])
#                 qt = int(soup.find('span', id='in_stock').text.split()[2])
#                 price = int(soup.find('span', id='price').text.split()[0])
#                 total += price * qt
# print(total)

# 4.7 Парсинг AJAX
# 4.7.1 Пример парсинг bitality.cc
# import requests
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest'
# }

# url = "https://bitality.cc/Home/GetSum?GiveName=Ethereum&GetName=Bitcoin&Sum=4.1895414&Direction=0"
# response = requests.get(url=url, headers=headers).json()
# print(response)

# {'giveSum': '4.1895414', 'getSum': '0.25619551'}

# import requests

# headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
#            'X-Requested-With': 'XMLHttpRequest', }
# headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'}

# url = 'https://cbr.ru/Queries/AjaxDataSource/112805'

# data_dollar = {
#     'DT': '',
#     'val_id': 'R01235',
#     '_': '1667219511852'
# }
# data_euro = {
#     'DT': '',
#     'val_id': 'R01239',
#     '_': '1667219511853'
# }
# response_dollar = requests.get(url=url, headers=headers, params=data_dollar).json()[-1]
# response_euro = requests.get(url=url, headers=headers, params=data_euro).json()[-1]

# print(f'Дата: {response_dollar["data"][:10]}')
# print(f'Курс USD: {response_dollar["curs"]} рублей')
# print(f'Курс EUR: {response_euro["curs"]} рублей')

# 4.8 Парсинг табличных данных
#********************************

# 4.8.1 Агрегация уникальных данных из таблицы
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/table/1/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'lxml')
# numbers = {float(cell.text) for row in soup.select('tr')[1:] for cell in row.select('td')}
# print(sum(numbers))

# 4.8.2 Суммирование чисел из первого столбца таблицы
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/table/2/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'lxml')
# numbers = [float(row.find('td').text) for row in soup.select('tr')[1:]]
# print(sum(numbers))

# 4.8.3 Агрегация выделенных чисел из таблицы
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/table/3/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'lxml')
# numbers = [float(cell.text) for cell in soup.select('b')]
# print(sum(numbers))

# 4.8.4 Суммирование чисел из зелёных ячеек таблицы
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/table/4/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'lxml')
# numbers = [float(cell.text) for cell in soup.select('td.green')]
# print(sum(numbers))

# 4.8.5 Агрегация произведений чисел из оранжевых и голубых ячеек таблицы
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/table/5/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'lxml')
# numbers = [float(row.find('td', 'orange').text) * int(row.select('td')[-1].text) for row in soup.select('tr')[1:]]
# print(sum(numbers))

# 4.8.6 Агрегация данных из столбцов таблицы в словарь
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/table/5/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'lxml')
# mx = [[float(cell.text) for cell in row.select('td')] for row in soup.select('tr')[1:]]
# headers = [header.text for header in soup.select('th')]
# dc = {key: round(sum(vals), 3) for key, vals in zip(headers, zip(*mx))}
# print(dc)

# 4.8.7 Суммирование чисел, кратных трём, из шести таблиц
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/4.8/7/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'lxml')
# total = sum([int(i.text) for i in soup.select('td') if int(i.text) % 3 == 0])
# print(total)

# 4.8.8 Извлечение и суммирование данных из таблицы в объединённых ячейках
# import requests
# from bs4 import BeautifulSoup

# url = 'https://parsinger.ru/4.8/8/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'lxml')
# s = sum([int(i.text) for i in soup.select('[colspan]')[1:]])
# print(s)

# 4.8.9 Поиск подходящих авто
# import requests
# import json
# from bs4 import BeautifulSoup

# def check_car(car):
#     is_year = int(car.select('td')[1].text) >= 2005
#     is_engin = car.select('td')[4].text == 'Бензиновый'
#     is_price = int(car.select('td')[7].text) <= 4000000
#     return all([is_year, is_engin, is_price])

# url = 'https://parsinger.ru/4.8/6/index.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = BeautifulSoup(html.text, 'lxml')
# col_nums = [0, 1, 4, 7]
# headers = [header.text for i, header in enumerate(soup.select('th')) if i in col_nums]
# filtered_cars = []
# for row in soup.select('tr')[1:]:
#     if check_car(row):
#         car = {}
#         for i, key in zip(col_nums, headers):
#             car[key] = int(data) if (data := row.select('td')[i].text).isdigit() else data
#         filtered_cars.append(car)
# sorted_cars = sorted(filtered_cars, key=lambda x: x["Стоимость авто"])
# cars_json = json.dumps(sorted_cars, indent=4, ensure_ascii=False)
# print(cars_json)

# 4.9 Сохраняем результат в Excel. CSV часть 2 (пример)
# import csv
# import requests
# from bs4 import BeautifulSoup

# # 1 ------------------------------------------------------
# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Артикул', 'Бренд', 'Модель',
#         'Тип', 'Игровая', 'Размер', 'Разрешение','Подсветка',
#         'Сайт производителя', 'В наличии', 'Цена'])
# # 1 ------------------------------------------------------

# # 2 ------------------------------------------------------
# url = 'http://parsinger.ru/html/mouse/3/3_11.html'

# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# # 2 ------------------------------------------------------

# # 3 ------------------------------------------------------
# name = soup.find('p', id='p_header').text
# article = soup.find('p', class_='article').text.split(': ')[1]
# brand = soup.find('li', id='brand').text.split(': ')[1]
# model = soup.find('li', id='model').text.split(': ')[1]
# type = soup.find('li', id='type').text.split(': ')[1]
# purpose = soup.find('li', id='purpose').text.split(': ')[1]
# light = soup.find('li', id='light').text.split(': ')[1]
# size = soup.find('li', id='size').text.split(': ')[1]
# dpi = soup.find('li', id='dpi').text.split(': ')[1]
# site = soup.find('li', id='site').text.split(': ')[1]
# in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
# price = soup.find('span', id='price').text.split(' ')[0]
# # 3 ------------------------------------------------------

# # 4 ------------------------------------------------------
# with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         name, article, brand, model,
#         type, purpose, light, size, dpi,
#         site, in_stock, price])
# # 4 ------------------------------------------------------

# 4.9.1 Сбор данных о HDD
# import requests
# import csv  
# from bs4 import BeautifulSoup

# def get_soup(url, parser='lxml'):
#     html = requests.get(url)
#     html.encoding = 'utf-8'
#     return BeautifulSoup(html.text, parser)

# url = 'https://parsinger.ru/html/index4_page_1.html'
# html = requests.get(url)
# html.encoding = 'utf-8'
# soup = get_soup(url)

# links = [a['href'] for a in soup.find('div', 'pagen').select('a')]
# headers = ['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена']
# with open('Stepik_Parsing/result.csv', 'w', encoding='utf-8-sig', newline='') as ouf:
#     writer = csv.writer(ouf, delimiter=';')
#     writer.writerow(headers)
# with open('Stepik_Parsing/result.csv', 'a', encoding='utf-8-sig', newline='') as ouf:
#     writer = csv.writer(ouf, delimiter=';')
#     scheme = 'https://parsinger.ru/html/'
#     for link in links:
#         url = scheme + link
#         soup = get_soup(url)
#         for box in soup.select('div.img_box'):
#             data = [box.find('a', 'name_item').text.strip()] + [tag.text.split(': ')[1].strip() for tag in box.select('li')] + [box.find('p', 'price').text]
#             writer.writerow(data)

# 4.9.2 Сбор данных о часах с карточек товара
# import requests
# import csv
# from bs4 import BeautifulSoup

# def get_soup(url, parser='lxml'):
#     html = requests.get(url)
#     html.encoding = 'utf-8'
#     return BeautifulSoup(html.text, parser)

# def data_row(link):
#     soup = get_soup(link)
#     product = soup.select_one('#p_header').text.strip()
#     article = soup.select_one('.article').text.split(':')[1].strip()
#     qt = int(soup.select_one('#in_stock').text.split(':')[1].strip())
#     price = soup.select_one('#price').text.strip()
#     old_price = soup.select_one('#old_price').text.strip()
#     descr = [i.text.split(': ')[1].strip() for i in soup.select('li')]
#     data = [product, article, *descr, qt, price, old_price, link]
#     return data

# headers = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса', 'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие','Цена', 'Старая цена', 'Ссылка на карточку с товаром']
# with open('Stepik_Parsing/WatchInfo.csv', 'w', encoding='utf-8-sig', newline='') as ouf:
#     wr = csv.writer(ouf, delimiter=';')
#     wr.writerow(headers)
# scheme = 'https://parsinger.ru/html/'
# url = 'https://parsinger.ru/html/index1_page_1.html'
# soup = get_soup(url)
# pages = [a['href'] for a in soup.select_one('.pagen').select('a')]
# with open('Stepik_Parsing/WatchInfo.csv', 'a', encoding='utf-8-sig', newline='') as ouf:
#     wr = csv.writer(ouf, delimiter=';')
#     for page in pages:
#         link = scheme + page
#         soup = get_soup(link)
#         cards = [a['href'] for a in soup.select('a.name_item')]
#         for card in cards:
#             link = scheme + card
#             data = data_row(link)
#             wr.writerow(data)

# 4.9.3 Сбор данных со всех карточек(160шт)
# import requests
# import csv
# from bs4 import BeautifulSoup

# def get_soup(url, parser='lxml'):
#     html = rs.get(url)
#     html.encoding = 'utf-8'
#     return BeautifulSoup(html.text, parser)

# def card_data(card):
#     item = card.select_one('a.name_item').text.strip()
#     descr = [i.text.split(':')[1].strip() for i in card.select('li')]
#     price = card.select_one('p.price').text.strip()
#     return [item, *descr, price]

# scheme = 'https://parsinger.ru/html/'
# url = 'https://parsinger.ru/html/index1_page_1.html'
# cards = []
# with requests.Session() as rs:
#     soup = get_soup(url)
#     sections = [scheme + a['href'] for a in soup.select_one('div.nav_menu').select('a')]
#     for sect in sections:
#         soup = get_soup(sect)
#         pages = [scheme + a['href'] for a in soup.select_one('div.pagen').select('a')]
#         for page in pages:
#             soup = get_soup(page)
#             cards.extend(soup.select('div.item'))
# with open('Stepik_Parsing/GoodsInfo.csv', 'w', encoding='utf-8-sig', newline='') as ouf:
#     writer = csv.writer(ouf, delimiter=';')
#     for card in cards:
#         writer.writerow(card_data(card))

# 4.9.4 Рецензируйте код других учеников
# import requests
# import csv
# from bs4 import BeautifulSoup

# def get_soup(url, session=None, parser='lxml'):
#     '''Функция скачивает содержимое html страницы по переданной ссылке в качестве аргумента и возвращает "приготовленный суп"'''
#     try:
#         # В зависимости от того предана ли вторым аргументом ссылка на объект сессию отправляет запрос с испоьзованием сессии, либо обычный get запрос
#         html = session.get(url) if session else requests.get(url)
#         html.encoding = 'utf-8'
#         if not html.ok:
#             raise requests.HTTPError(html.status_code)
#     except (requests.ConnectionError, requests.HTTPError, requests.Timeout) as e:
#         print(f'Перехвачено исключение типа: {type(e).__name__}')
#         print(f'Сообщение об ошибке: {str(e)}')
#     return BeautifulSoup(html.text, parser)

# def link_generator(url, scheme, session=None):
#     '''Генератор ссылок, принимает в качестве аргумента ссылку на главную страницу и на каждой итеррации возвращает очередную ссылку на карточку товара'''
#     soup = get_soup(url, session)
#     # Формирование списка ссылок на категории товара
#     categories = [scheme + a['href'] for a in soup.select_one('div.nav_menu').select('a')]
#     for category in categories:
#         soup = get_soup(category, session)
#         # Формирование списка ссылок страниц для текущей категории товаров
#         pages = [scheme + a['href'] for a in soup.select_one('div.pagen').select('a')]
#         for page in pages:
#             soup = get_soup(page, session)
#             # Формирование списка ссылок на карточки товара для текущей страницы
#             links = [scheme + a['href'] for a in soup.select('a.name_item')]
#             for link in links:
#                 yield link

# def get_card_row(url, session=None):
#     '''Функция принимает в качестве аргумента ссылку на карточку товара и возвращает список, элементами которого являются требуемые характеристики товара'''
#     soup = get_soup(url, session)
#     row=[]
#     selectors = ['#p_header', 'p.article', '#brand', '#model', '#in_stock', '#price', '#old_price'] # Селекторы для нахождения интересующих характеристик на странице
#     for selector in selectors:
#         # Выбор обработки текстовой информации, содержащейся тегах в зависимости от структуры записи
#         if selector in ('#p_header', '#price', '#old_price'):
#             row.append(soup.select_one(selector).text.strip())
#         else:
#             row.append(soup.select_one(selector).text.split(':')[1].strip())
#     row.append(url)
#     return row

# url = 'https://parsinger.ru/html/index1_page_1.html' # URL основной страницы сайта
# scheme = 'https://parsinger.ru/html/' # Начальная часть ссылки к которой будет добавляться относительная ссылка для формирования абсолютной
# headers = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена', 'Ссылка'] # Список заголовков таблицы
# # Открытие файла CSV в корневом каталоге проекта в режиме записи
# with open('ProductsInfo.csv', 'w', encoding='utf-8-sig', newline='') as ouf:
#     writer = csv.writer(ouf, delimiter=';')
#     writer.writerow(headers) # Запись заголовков в файл
#     # Создание сесси в рамках которой будут идти все запросы по ссылкам без разрыва соединения с сервером
#     with requests.Session() as rs:
#         lg = link_generator(url, scheme, rs) # Создание генератора ссылок на страницы с карточками товаров
#         for link in lg:
#             row = get_card_row(link, rs) # Формирование информации о товаре в виде списка
#             writer.writerow(row) # Запись строки с информацие о товаре в файл CSV

# 4.10.1 Сбор данных о HDD в JSON
# import requests
# import json
# from bs4 import BeautifulSoup

# def get_soup(url, session=None, parser='lxml'):
#     try:
#         html = session.get(url) if session else requests.get(url)
#         html.encoding = 'utf-8'
#         if not html.ok:
#             raise requests.HTTPError(html.status_code)
#     except (requests.ConnectionError, requests.HTTPError, requests.Timeout) as e:
#         print(f'Перехвачено исключение типа: {type(e).__name__}')
#         print(f'Сообщение об ошибке: {str(e)}')
#     return BeautifulSoup(html.text, parser)

# url = 'https://parsinger.ru/html/index4_page_1.html'
# scheme = 'https://parsinger.ru/html/'
# soup = get_soup(url)
# data_json = []
# pages = [scheme + a['href'] for a in soup.select_one('div.pagen').select('a')]
# for page in pages:
#     soup = get_soup(page)
#     for hdd in [tag for tag in soup.select('div.img_box')]:
#         dc = {
#             'Наименование': hdd.select_one('.name_item').text.strip(),
#             'Бренд': hdd.select('li')[0].text.split(':')[1].strip(),
#             'Форм-фактор': hdd.select('li')[1].text.split(':')[1].strip(),
#             'Ёмкость': hdd.select('li')[2].text.split(':')[1].strip(),
#             'Объем буферной памяти': hdd.select('li')[3].text.split(':')[1].strip(),
#             'Цена': hdd.select_one('.price').text.strip()
#         }
#         data_json.append(dc)
# with open('Stepik_Parsing/hdd_info.json', 'w', encoding='utf-8') as ouf:
#     json.dump(data_json, ouf, indent=4, ensure_ascii=False)

# 4.10.2 Сбор данных со всех карточек товара
# import requests
# import json
# from bs4 import BeautifulSoup

# def get_soup(url, session=None, parser='lxml'):
#     try:
#         html = session.get(url) if session else requests.get(url)
#         html.encoding = 'utf-8'
#         if not html.ok:
#             raise requests.HTTPError(html.status_code)
#     except (requests.ConnectionError, requests.HTTPError, requests.Timeout) as e:
#         print(f'Перехвачено исключение типа: {type(e).__name__}')
#         print(f'Сообщение об ошибке: {str(e)}')
#     return BeautifulSoup(html.text, parser)

# def get_info_json(tag):
#     dc = {}
#     dc['Наименование'] = tag.select_one('.name_item').text.strip()
#     for key, val in [i.text.split(':') for i in tag.select('li')]:
#         dc[key.strip()] = val.strip()
#     dc['Цена'] = tag.select_one('.price').text.strip()
#     return dc

# url = 'https://parsinger.ru/html/index1_page_1.html'
# scheme = 'https://parsinger.ru/html/'
# data_json = []
# with requests.Session() as rs:
#     soup = get_soup(url, rs)
#     categories = [scheme + a['href'] for a in soup.select_one('.nav_menu').select('a')]
#     for category in categories:
#         soup = get_soup(category, rs)
#         pages = [scheme + a['href'] for a in soup.select_one('.pagen').select('a')]
#         for page in pages:
#             soup = get_soup(page, rs)
#             pg_data = [get_info_json(tag) for tag in soup.select('.img_box')]
#             data_json.extend(pg_data)
# with open('Stepik_Parsing/all_goods_info.json', 'w', encoding='utf-8') as ouf:
#     json.dump(data_json, ouf, indent=4, ensure_ascii=False)

# # 4.10.3 Сбор данных о телефонах с карточек товара
# import requests
# import json
# from bs4 import BeautifulSoup

# def get_soup(url, parser='lxml'):
#     html = requests.get(url)
#     html.encoding = 'utf-8'
#     return BeautifulSoup(html.text, parser)

# def link_generator(url):
#     scheme = 'https://parsinger.ru/html/'
#     soup = get_soup(url)
#     pages = [scheme + a['href'] for a in soup.select_one('.pagen').select('a')]
#     for page in pages:
#         soup = get_soup(page)
#         links = [scheme + a['href'] for a in soup.select('.name_item')]
#         for link in links:
#             yield link

# def get_card_info(url):
#     soup = get_soup(url)
#     description = {li['id']: li.text.split(':')[1].strip() for li in soup.select('li')}
#     dc = {'categories': 'mobile',
#           'name': soup.select_one('#p_header').text.strip(),
#           'article': soup.select_one('p.article').text.split(':')[1].strip(),
#           'description': description,
#           'count': soup.select_one('#in_stock').text.split(':')[1].strip(),
#           'price': soup.select_one('#price').text.strip(),
#           'old_price': soup.select_one('#old_price').text.strip(),
#           'link': url}
#     return dc

# url = 'https://parsinger.ru/html/index2_page_1.html'
# data_json = []
# lg = link_generator(url)
# for link in lg:
#     data_json.append(get_card_info(link))
# with open('Stepik_Parsing/phone_info.json', 'w', encoding='utf-8') as ouf:
#     json.dump(data_json, ouf, indent=4, ensure_ascii=False)

# 4.10.4 Рецензируйте код других учеников
# import requests
# import json
# from bs4 import BeautifulSoup

# def get_soup(url, session, parser='lxml'):
#     '''Функция скачивает содержимое html страницы по переданной ссылке в качестве аргумента 
#     и возвращает "приготовленный суп"'''
#     html = session.get(url) if session else requests.get(url)
#     html.encoding = 'utf-8'
#     return BeautifulSoup(html.text, parser)

# def link_generator(url):
#     '''Генератор ссылок, принимает в качестве аргумента ссылку на страницу категории товара 
#     и на каждой итеррации возвращает очередную ссылку на карточку товара этой категории'''
#     soup = get_soup(url, rs)
#     pages = [scheme + a['href'] for a in soup.select_one('.pagen').select('a')]
#     for page in pages:
#         soup = get_soup(page, rs)
#         links = [scheme + a['href'] for a in soup.select('.name_item')]
#         for link in links:
#             yield link

# def get_card_info(category, url):
#     '''Функция принимает в качестве аргументов наименование катенории и ссылку на карточку товара из этой категории
#     и возвращает словарь, элементами которого являются требуемые характеристики товара'''
#     soup = get_soup(url, rs)
#     description = {li['id']: li.text.split(':')[1].strip() for li in soup.select('li')}
#     dc = {'categories': category,
#           'name': soup.select_one('#p_header').text.strip(),
#           'article': soup.select_one('p.article').text.split(':')[1].strip(),
#           'description': description,
#           'count': soup.select_one('#in_stock').text.split(':')[1].strip(),
#           'price': soup.select_one('#price').text.strip(),
#           'old_price': soup.select_one('#old_price').text.strip(),
#           'link': url}
#     return dc

# url = 'https://parsinger.ru/html/index1_page_1.html'
# scheme = 'https://parsinger.ru/html/'
# data_json = []
# with requests.Session() as rs:
#     soup = get_soup(url, rs)
#     category_urls = [scheme + a['href'] for a in soup.select_one('.nav_menu').select('a')]
#     for url in category_urls:
#         soup = get_soup(url, rs)
#         category = soup.select_one('a.name_item')['href'].split('/')[0]
#         lg = link_generator(url)
#         for link in lg:
#             data_json.append(get_card_info(category, link))
# with open('all_goods_info.json', 'w', encoding='utf-8') as ouf:
#     json.dump(data_json, ouf, indent=4, ensure_ascii=False)

# 4.11 Парсим JSON
# ********************************

# 4.11.1 Анализ количества товаров через JSON
# import requests

# url = 'https://parsinger.ru/downloads/get_json/res.json'
# resp = requests.get(url).json()
# goods_qt = {}
# for dc in resp:
#     key, var = dc['categories'], int(dc['count'])
#     goods_qt[key] = goods_qt.get(key, 0) + var
# print(goods_qt)

# 4.11.2 Вычисление Стоимости Товаров в Каждой Категории
# import requests

# url = 'https://parsinger.ru/downloads/get_json/res.json'
# resp = requests.get(url).json()
# goods_cost = {}
# for dc in resp:
#     category, qt, price = dc['categories'], int(dc['count']), int(dc['price'].split()[0])
#     goods_cost[category] = goods_cost.get(category, 0) + qt * price
# print(goods_cost)

# 4.11.3 Вычисление Произведения 'article' и 'rating'
import requests

url = 'https://parsinger.ru/4.6/1/res.json'
resp = requests.get(url).json()
data = {}
for dc in resp:
    category, article, rating = dc['categories'], int(dc['article']), dc['description']['rating']
    data[category] = data.get(category, 0) + article * rating
print(data)