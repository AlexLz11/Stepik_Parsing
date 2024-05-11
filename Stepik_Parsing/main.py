#******************************************
#      Part 5. Selenium
#******************************************

# 5.2 Установка Selenium Webdriver

#------------------------------------------------------------
# Для запуска вебдрайвера на локальной IDE
#------------------------------------------------------------
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
# from selenium.webdriver.chrome.service import Service as ChromiumService

# with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as driver:
#     driver.get("https://stepik.org/course/104774")
#     time.sleep(5)

# ------------------------------------------------------
# ***Примечание:
# Когда интерпретатор дойдёт до строки ChromeDriverManager().install(), будет происходить следующее:
# Библиотека webdriver_manager проверит, установлен ли уже на вашем компьютере нужный chromedriver и соответствует ли он версии вашего браузера Chrome.
# Если нужный chromedriver не найден или его версия не соответствует, webdriver_manager автоматически скачает нужную версию ChromeDriver с официального сайта.
# Загруженный файл будет распакован и сохранён в удобное место (обычно это каталог .cache в вашем домашнем каталоге).
# Путь к этому распакованному файлу chromedriver будет автоматически добавлен к вашей сессии, и WebDriver будет инициализирован с использованием этого драйвера.
# ВСЕ ВЫШЕОПИСАННОЕ НЕ РАБОТАЕТ В ОБЛАЧНОМ REPLIT !!!!
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Настройка для драйвера для replit ("безголовый" режим)
# (без вебдрайвер менеджера)
#-----------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--disable-gpu')

# with webdriver.Chrome(options=chrome_options) as driver:
#     driver.get('https://www.example.com')
#     print(driver.page_source)

# 5.3 Опции и аргументы. Запуск браузера с расширениями
# import time
# from selenium import webdriver

# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('Stepik_Parsing/chrome_ext_pak/coordinates.crx')

# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://stepik.org/course/104774'
#     browser.get(url)
#     time.sleep(15)

# import time
# from selenium import webdriver

# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('user-data-dir=/home/lizard/.config/google-chrome')
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://google.ru/'
#     browser.get(url)
#     time.sleep(30)

# 5.3 Proxy и Selenium
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# opts = Options()
# opts.add_argument('--headless')
# opts.add_argument('--no-sandbox')
# opts.add_argument('--disable-dev-shm-usage')
# opts.add_argument('--disable-gpu')

# url = 'https://2ip.ru/'
# with webdriver.Chrome(options=opts) as browser:
#     browser.get(url)
#     time.sleep(5)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# proxy = '178.218.44.79:3128'
# opts = webdriver.ChromeOptions()
# # opts.add_argument('--headless')
# # opts.add_argument('--no-sandbox')
# # opts.add_argument('--disable-dev-shm-usage')
# # opts.add_argument('--disable-gpu')
# opts.add_argument('--proxy-server=%s' % proxy)
# # opts.add_argument('--ignore-certificate-errors-spki-list')
# # opts.add_argument('--ignore-ssl-errors')
# # opts.add_argument("--ignore-certificate-errors")

# url = 'https://2ip.ru/'
# with webdriver.Chrome(options=opts) as browser:
#     browser.get(url)
#     time.sleep(5)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

# import requests
# url = 'http://httpbin.org/ip'
# ip = '178.218.44.79:3128'
# try:
#     proxy = {'http': f'http://{ip}',
#              'https': f'https://{ip}'
#              }
#     resp = requests.get(url, proxies=proxy)
#     print(resp.json(), 'Success connection')
# except Exception as _ex:
#     print(ip, '--Not work')

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# proxy_list = ['46.47.197.210:3128', '178.218.44.79:3128', 
# '95.66.138.21:8880', '109.194.22.61:8080', 
# '45.8.211.113:80', '45.8.211.90:80', ]

# for PROXY in proxy_list:
#     try:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--proxy-server=%s' % PROXY)
#         chrome_options.add_argument('--ignore-ssl-errors')
#         chrome_options.add_argument("--ignore-certificate-errors")
#         url = 'https://2ip.ru'

#         with webdriver.Chrome(options=chrome_options) as browser:
#             browser.get(url)
#             print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

#             browser.set_page_load_timeout(20)

            
#     except Exception as _ex:
#         print(f"Превышен timeout ожидания для - {PROXY}")
#         continue

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = browser.find_element(By.ID, "sale_button").click()

# time.sleep(10)

# 5.4 Поиск элементов Selenium. Работаем с браузером

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver= webdriver.Chrome()
# driver.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = driver.find_element(By.ID, "sale_button")
# time.sleep(2)
# button.click()
# time.sleep(2)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# try:
#     driver= webdriver.Chrome()
#     driver.get('http://parsinger.ru/html/watch/1/1_1.html')
#     button = driver.find_element(By.ID, "sale_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(2)
# finally:
#     driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# with webdriver.Chrome() as driver:
#     driver.get('http://parsinger.ru/html/watch/1/1_1.html')
#     button = driver.find_element(By.ID, "sale_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(2)

# 5.4.1 Мастер заполнения форм
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/1/1.html')
#     data = ['Иванов', 'Иван', 'Иванович', '27', 'Н-ск', 'mail@mail.ru']
#     input_forms = browser.find_elements(By.CLASS_NAME, 'form')
#     for form, text in zip(input_forms, data):
#         form.send_keys(text)
#     browser.find_element(By.ID, 'btn').click()
#     time.sleep(10)
#     result = browser.find_element(By.ID, 'result').text
# print(result)

# 5.4.2 Охотник за Сокровищами
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# with webdriver.Chrome() as drv:
#     drv.get('https://parsinger.ru/selenium/2/2.html')
#     drv.find_element(By.LINK_TEXT, '16243162441624').click()
#     time.sleep(10)
#     res = drv.find_element(By.ID, 'result').text
# print(res)

# 5.4.3 Кодекс Охотников за Цифрами
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/selenium/3/3.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     p_tags = browser.find_elements(By.TAG_NAME, 'p')
#     res = sum([int(p.text) for p in p_tags])
# print(res)

# 5.4.4 Поход за сокровищами в Цифровом Лабиринте
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/selenium/3/3.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     elems = browser.find_elements(By.XPATH, '//div/p[2]')
#     result = sum([int(elem.text) for elem in elems])
# print(result)

# 5.4.5 Операция 'Кодовый Замок
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'http://parsinger.ru/selenium/4/4.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for box in browser.find_elements(By.CLASS_NAME, 'check'):
#         box.click()
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     result = browser.find_element(By.ID, 'result').text
# print(result)

# 5.4.6 Кодовая Одиссея
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'http://parsinger.ru/selenium/5/5.html'
# numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38, 
# 39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73, 
# 74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118, 
# 119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153, 
# 154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
# 187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207, 
# 208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233, 
# 234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255, 
# 256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
# 292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314, 
# 318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349, 
# 353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412, 
# 419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451, 
# 452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479, 
# 480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for box in browser.find_elements(By.CLASS_NAME, 'check'):
#         if int(box.get_attribute('value')) in numbers:
#             box.click()
#     time.sleep(10)
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     result = browser.find_element(By.ID, 'result').text
# print(result)

# 5.4.7 Операция "Выпадающие списки"
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'http://parsinger.ru/selenium/7/7.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     keys = browser.find_elements(By.TAG_NAME, 'option')
#     code = sum([int(key.text) for key in keys])
#     browser.find_element(By.ID, 'input_result').send_keys(code)
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     time.sleep(5)
#     result = browser.find_element(By.ID, 'result').text
# print(result)

# 5.4.8 Миссия "Загадочный След"
# import sympy
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'http://parsinger.ru/selenium/6/6.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     expr = browser.find_element(By.ID, 'text_box').text
#     key = str(sympy.simplify(expr))
#     browser.find_element(By.XPATH, f'//*[text()={key}]').click()
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     result = browser.find_element(By.ID, 'result').text
#     print(result)

# 5.5.1 Охота на Скрытые Сокровища
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/methods/1/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     result = browser.find_element(By.ID, 'result').text
#     while result == 'refresh page':
#         browser.refresh()
#         result = browser.find_element(By.ID, 'result').text
# print(result)

# 5.5.2 Операция "Чистый Лист"
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/selenium/5.5/1/1.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for field in browser.find_elements(By.CLASS_NAME, 'text-field'):
#         field.clear()
#     browser.find_element(By.ID, 'checkButton').click()
#     alert = browser.switch_to.alert
#     result = alert.text
# print(result)

# 5.5.3 Операция "Минное поле"
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/selenium/5.5/2/1.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for field in browser.find_elements(By.CLASS_NAME, 'text-field'):
#         if field.is_enabled():
#             field.clear()
#     browser.find_element(By.ID, 'checkButton').click()
#     alert = browser.switch_to.alert
#     result = alert.text
# print(result)

# 5.5.4 Числовая Добыча: Операция 'Чекбокс'
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/selenium/5.5/3/1.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     fields = browser.find_elements(By.CLASS_NAME, 'parent')
#     result = sum([int(i.find_element(By.TAG_NAME, 'textarea').text) for i in fields if i.find_element(By.CLASS_NAME, 'checkbox').is_selected()])
# print(result)

# 5.5.5 Операция "Цветовая Синхронизация"
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/selenium/5.5/4/1.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for i in browser.find_elements(By.CLASS_NAME, 'parent'):
#         num = i.find_element(By.CSS_SELECTOR, '[color="gray"]')
#         i.find_element(By.CSS_SELECTOR, '[color="blue"]').send_keys(num.text)
#         num.clear()
#         i.find_element(By.TAG_NAME, 'button').click()
#     browser.find_element(By.ID, 'checkAll').click()
#     result = browser.find_element(By.ID, 'congrats').text
# print(result)

# 5.5.6 Квест "Ад Цветовых Шифров"
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/selenium/5.5/5/1.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for div in browser.find_elements(By.XPATH, '//div/div[@style]'):
#         color = div.find_element(By.TAG_NAME, 'span').text
#         div.find_element(By.XPATH, f'.//*[@value="{color}"]').click()
#         div.find_element(By.XPATH, f'.//button[@data-hex="{color}"]').click()
#         div.find_element(By.XPATH, './/input[@type="checkbox"]').click()
#         div.find_element(By.XPATH, './/input[@type="text"]').send_keys(color)
#         div.find_element(By.XPATH, './/button[text()="Проверить"]').click()
#     browser.find_element(By.XPATH, '//button[text()="Проверить все элементы"]').click()
#     alert = browser.switch_to.alert
#     result = alert.text
# print(result)

# 5.6 Cookies в Selenium
# from pprint import pprint
# from selenium import webdriver

# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://ya.ru/')
#     cookies = webdriver.get_cookies()
#     pprint(cookies)

# 5.6.1 Кодовое имя: "Секретные печеньки"
# from selenium import webdriver

# url = 'https://parsinger.ru/methods/3/index.html'
# with webdriver.Chrome() as webdriver:
#     webdriver.get(url)
#     cookies = webdriver.get_cookies()
#     result = sum([int(cookie['value']) for cookie in cookies if 'secret_cookie_' in cookie['name']])
# print(result)

# 5.6.2 Кодовое имя: Следопыт Чётных Печеньек
# from selenium import webdriver

# def is_even_cookie(cookie):
#     return int(cookie['name'].split('_')[-1]) % 2 == 0

# url = 'https://parsinger.ru/methods/3/index.html'
# with webdriver.Chrome() as webdriver:
#     webdriver.get(url)
#     cookies = webdriver.get_cookies()  
#     total = sum([int(cookie['value']) for cookie in cookies if is_even_cookie(cookie)])
# print(total)

# 5.6.3 Кодовое имя: Операция "Бессмертный Печенюшка"
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/methods/5/index.html'
# cookie_info = []
# with webdriver.Chrome() as webdriver:
#     webdriver.get(url)
#     for link in webdriver.find_elements(By.TAG_NAME, 'a'):
#         link.click()
#         cookie = webdriver.get_cookies()[0]
#         expiry = int(cookie['expiry'])
#         num = webdriver.find_element(By.ID, 'result').text
#         cookie_info.append((expiry, num))
#         webdriver.back()
# print(max(cookie_info)[1])

# 5.6.4 Кодовое имя: Операция "Младший Виртуоз"
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/selenium/5.6/1/index.html'
# cookies = [{'name': 'KXIYO4xMrWh', 'value': 'ibyAZPfXAsPqptPaNyL'}, 
#        {'name': '0OIJ4G4ZLzK', 'value': 'kJcPzQu5Jr8ELK'},
#        {'name': 'O1C4sd3RK5udnZ6P', 'value': '4mYYxbfgnIvuip2ry58EQ'},
#        {'name': 'AUZgaLJ4Y', 'value': 'FLSZvYrkf1E57YMUkdD'},
#        {'name': '9PWJc0VXVtnXNcS5Tf', 'value': 'YQ2G4RayBoXSEqEgA3oXRN3FAvAMT'},
#        {'name': 'pN2x6MDb', 'value': 'htbtD59XD3vCemHRCe9iUxV1smvXAIk5XOwuHnnmMB0'},
#        {'name': 'AsqpQd', 'value': 'uNFFRiqeRrj25MwJajG4AxeKvCxKbHUSbbvzb3C'},
#        {'name': '73PVEdwTk0txDp4L', 'value': 'DTniz3Fwj110H24dfZfd5JqqfEtN'},
#        {'name': 'jZ1MwGy5z0L8ZW00U', 'value': 'sspfahNvfeo3zHWAIW0jdp2A9LyDbIm0'},
#        {'name': 'aLRosjpBhYrZ0J69a', 'value': 'zcoXWv5L9Pz5kwGeyP5jlAQ'},
#        {'name': '9LPCTyKTNmvBcnZ', 'value': 'GWBjw1Gosk4IKxuh5J2eu0ikgowOaZwP8FOm1ekKeQIxJDIXBy'},
#        {'name': 'psH0h', 'value': 'wNAUmVlQwG6VK5TvDfryipzWeLXX46WDbXUd8yGrhrA3Hnc'},
#        {'name': 'BULl3P', 'value': 'wefA0ljyA82kYpV1OoOixtAIp6xjmiQlS9SLeN'},
#        {'name': '3bIJVJCylqgshRC9r1dH', 'value': '6Y6EZE5dttgx7rKzP881nAhRPE'},
#        {'name': 'dBDhCzi6VO0', 'value': 'LKMcpZ6bEJy5IY352OMViznSP5OMqS9IgZB0YMv'},
#        {'name': '6SGnnuoZ7v', 'value': '6asdYiIPBsMEdO0mQ9Jlq0mSMbJjfg'},
#        {'name': '4dfAVZ1qZwijwYMUj', 'value': '3TOxOPelSdN6cK273'},
#        {'name': 'RMOPZQILwFr3o637M', 'value': 'RZoaTFTdytqxB6sZhO4ebrhWlxjhMoQn8ZiObpdcGgH'},
#        {'name': '08cQ7E3qHOOMk4uy1fLz', 'value': 'YfYkz9boRjDHLTahMuZcAJPzbjwTlRt1iNZzGl'},
#        {'name': 'YT1NKf55egy', 'value': '3MSmfnklFY5TzvM8np4guMsJYtmdHmbyHiz3Vp6Rtk7r4GWhC'},
#        {'name': 'cTKnm0a3H2euL46Ibi', 'value': 'HCZ0KYkidXfFowGinPuWG19cT79gEJC'},
#        {'name': 'mvAz0P7Igjs2JY', 'value': '8O67zvSDHJx'},
#        {'name': 'TzWXbWMvDBcKTo', 'value': 'dzwNYZCg4jpxKtpCeumwq0DO2KtGWLIHpQLOrzmGbXMC8G'},
#        {'name': '1BMgyMHkzUemIEr', 'value': '08Sd1v8kQi6eB1FTs9qfjDkJ9UfKCLOFGtDgbOlu9v9iiuu'},
#        {'name': 'Jig5voy', 'value': 'Pi4OA6hY21TeHlHyPMaMFHgY0BZRcQ9V0nXg'},
#        {'name': '10wa7lhCoJXIzEYW5kQ', 'value': 'BFp4YeKWKVKXHTOesJLleaAelwYwPz51C95IYzd'},
#        {'name': 'BqXt5D', 'value': 'n99ZSFFhseCs7aVjU31pYSJxqMgFYGfreFZl9ixb2NNHRBp'},
#        {'name': 'GJunU5e1BEvfd', 'value': 'y5YFJ3hF9hG45G86MD9W9nRk61JMsh8rsmbFFrDoeJVUfyBvZ'},
#        {'name': 'itFJBn79wksvZ15lc2', 'value': 'nXpdqpt0Po84uOuSU'},
#        {'name': 'O5Q70eOB5ivJt5DZ', 'value': 'AZRr2ATREeF9HQR2opgF'},
#        {'name': '6jBEUxI0a7x790m', 'value': 'comi8Mx5ig95NAiSO8'},
#        {'name': 'KpVF7aIkav32LuqIDI', 'value': 'ik4furgLieyUawgJpttvHxWoXm2zO19'},
#        {'name': 'OTRFyN', 'value': 'vlzV7Z97sWcJStZgDJiRjzIf'},
#        {'name': 'hKLzMbgdIlUTAMYSEo', 'value': 'Tq2l0QJ3ekwxY3uaC8n2ln1nDMWhltFQm2TNaBefAAzk'},
#        {'name': 'GJKNrAvRn', 'value': 'dByJXuSsAIz3Rnqa9BvU11okpnSydEZnkaqMQu9RoE'},
#        {'name': 'AowB8Q3t74JHmXTGc1', 'value': '02JklRAtbsNNe'},
#        {'name': 'xPpvKmo03bGBYrmqw', 'value': '7bf4FgaLKoj6YvGq4huLT5r9eCflo70QhI9gAPkMIuj4Bg'},
#        {'name': '8UqFFBP3Dm0s6XM', 'value': 'kSZJPw6oTBwqG94q'},
#        {'name': 'WeeXL7bKNWIZZkgX', 'value': 'ap3DPbBYqlfEOZ6'},
#        {'name': 'fhdSevpxKUzledgGtbL4', 'value': 'v5I4A3PFOlN9zWPDkedlC2eLbMZ5cn3cf8'},
#        {'name': '3H6lO', 'value': 'jxc9994fPQBKpnyr8aZBDZlMAolnxXh'},
#        {'name': 'QVen8QnA1648g4Dm9p', 'value': 'RXNYpaUTJlD4xVIOm'},
#        {'name': '3PxMnD9w', 'value': 'JC74xNLEc5ujZge7OmXj5EWk3hwdm4OH8FgF60D6pFl'},
#        {'name': 'o8yY57CZSN', 'value': 'afO10rX663gaVttfSxeE70Gd22JKxwJAli7EhEdzkxxME'},
#        {'name': 'UpAdf46rvxXW', 'value': 'Ft2FEQV71gLnG'},
#        {'name': 'WRrpVIAkMKiZVxHt299', 'value': 'FC53hjqCGooNgV'},
#        {'name': 'XHViH149aRl5', 'value': 'YbozZeoGCt3gO1kRMoLExcfCotBz'},
#        {'name': 'yjNLzeR4k', 'value': 'Chd2mmuK7nxuVTi'},
#        {'name': '5M4RGm', 'value': 'tj3HWN5mVpz9zgIie2ac2KHKIeABaou'},
#        {'name': 'CcxIZZYgojDZpHnO9zJl', 'value': 'xLiql8yXUxULBG9w2snaMLI4FjSyX'},
#        {'name': 'NScrEjcTmwo639PQqki', 'value': 'eOSFemtdjyphiPubTAzTICUhgw92By'},
#        {'name': '9b5OpL5NrCpmtsE', 'value': 'VKdEIeX5ZNTghD6sq3qyjBHJaUuXfpQ7YnYb'},
#        {'name': 'uyBoiSTHTtxV8Wszttb', 'value': 'SHEEfVcj1jNv3V1oqeT2wfEbWKZ0uJ2ljwv'},
#        {'name': 'qR6AeEoEbQb1GYRj', 'value': 'mA66a177y8e6Nm7BlKBvpcUrM3fm6y4K'},
#        {'name': 'l0Y9gn8MNtC', 'value': 'M1L2OUmAisn1c6DNB9mJfTHRM9V3HuXUAEGG8Zx'},
#        {'name': 'L8m4GeWyECR', 'value': 'QuFfnWXebyrwwqXfVvAN2dbSisST8IgGyLggrVzTjaCeQ'},
#        {'name': 'GxJSMQh9aZjFdhgjaAj', 'value': 'phOonlKiMt0xLDtvoB52TbATS1Ggm4Pv5lztk5vTNkXVqp'},
#        {'name': 'GRE1eZ8D1bb', 'value': 'llpIP76V4S978YmQcfW'},
#        {'name': 'dooT1cyS41bIWEB9c', 'value': 'ORu004k9aFl9FdS77Iz'},
#        {'name': 'csjauyxnCpBySvkXTDzS', 'value': 'SJKqcIqWDbUJbxnHfD8jNJzYKb3Yp3TPIRDIpxCNB'},
#        {'name': 'Y6CgAqWN8', 'value': 'qu0g6xEm0iJeTKM8NfOZUxP0XQaCtUfiTWHtQJ5soU5cpZ'},
#        {'name': 'xxtL44KLbN60b5q', 'value': 'RSNFhhicL7pWpo3gvE3tJbHaIjU'},
#        {'name': 'KcvqC30', 'value': '58IlGI646RMaGMYtL5XYqxFq8UaMwjPDNFNApAuDpUI9tMoM4t'},
#        {'name': 'y761v6wZDo3V7O', 'value': '3i9iZjnZXdHlJxDz7ZrkPthYdI3PowS5yRomV0v8fR9WVco4'},
#        {'name': 'Ixr7AetyC', 'value': 'lYRaNZAnoNHc9UZIoXI9E'},
#        {'name': 'QIvvsr04T0JGVJE', 'value': 'tr6fE8moJI897w967QTmKojC730GdkKTUonevQbYsHQ71mi'},
#        {'name': 'CBTq9zQjJx', 'value': 'z7BuIeFufYeZysVnrglrDJk8KW8UBWYt62'},
#        {'name': '2ALhFQM7svECfgsSaiTa', 'value': 'VGMsulQVoobUe4m6w8dZGej8jFzSES3hzl9OG2csqpl'},
#        {'name': '7VQixJTzu2H', 'value': 'jPnLpldHTFNgPCH1RUlmRQx7N58P7CQHajLYvGxho'},
#        {'name': 'KdmUSh1SJH6M9', 'value': 'HPKIgmOBqq6Ln6QSPKedXuFpOoWhrOUzCxRMlcoJ2Gd0S7Hd'},
#        {'name': 't6B9gl6QeGEDl1LW', 'value': 'kGs0hk4Pmeb83dBbuHTSzIVNcY0G4iucq73lkCMwt6Akv4w'},
#        {'name': 'gcjmy3', 'value': 'QtB6duKOGc7eNc9MFwiOOaikXCYQg6dO4m66sJJxkRebKIKiR'},
#        {'name': '2oBZU9j', 'value': '2U80qbFDpRElKTshedtaZ42OzYG48OQckEt2Zy9D7T'},
#        {'name': 'g2tyy8erqS4E5pdSynCB', 'value': 'VN5zSYJpNHQC14FVl'},
#        {'name': 'lLhLcbED3XAgAPaMp', 'value': 'tBUVWsfSNg0Iv4TLPAmBRm2m2nrWh'},
#        {'name': 'iUfgKa7OX', 'value': 'GtyGoiA00RNiTgqvbXs78khbzQ7d0rh5xTk1aZK'},
#        {'name': 'WQGGXKzZXvRXLC0', 'value': 'itGXA2mVtchzcqstP39BvfBvwh'},
#        {'name': 'p37sYwX5mgtwXJl3yFBL', 'value': 'h20iY8XooVE'},
#        {'name': 'tubsOLf', 'value': 'YGlaF0EEJrT1c5Z2HBAWnc1Q3an3Ob'},
#        {'name': 'mg1Pr2NJJEnw2UkGFg', 'value': 'L48wovkYz32wa16iiswcgbA6JmyVoysUqjfm4i7'},
#        {'name': 'V55E3ui8KHXybSDSSnoc', 'value': '7rhA8PSMZFy1aC8CQXbitOxY0qdUkDOUWijijIvlHhtB0q1'},
#        {'name': 'AcWBQQy', 'value': 'zl1GXRHA3neBLCN8'},
#        {'name': 'PtvgV4eJ21CrPE3xeH9', 'value': '1tU9KvLdq2uRNRKtA'},
#        {'name': 'XjuSocgLwoMvFo8a', 'value': 'pvmx5A97Sad0U6d6i'},
#        {'name': 'mMpdmPLcZEAZDzNyA8a2', 'value': 'WG6CrZ3zXfxN84hJXUKJq0ZroYditsADYplxwhkgXkUcZ'},
#        {'name': 'tojhHp0ZlGrZ8Y3', 'value': 'fqpJvGkfQRT7ytNTU5KPum150MmcVR1nja0QIQRVEOPiNvT7Pg'},
#        {'name': 'LDHgCR5PNoqYdffU5', 'value': '7a0tCBgGzylPTGUStOuNXORrRWwy03Upm2CvJX'},
#        {'name': 'F4xcvPzuYYAvDrvDi', 'value': 'zQEpxlKpKprtwFbJyx0XYxFrlc8XP2RhRG'},
#        {'name': 'fmnoi', 'value': 'yB9333KC4bP4SHUF90Kj7OC9QXz22WAZ3xtZxLi9'},
#        {'name': 'TbGdmTkjcC52T7q', 'value': '2HCejTOfB98e30JMj3Pz9Ok9xLz5Y9lkaJaHoRF2vA5xq0i'},
#        {'name': 'tg3vMrNIZHs', 'value': '2XRV99ShR8yc0bCe0QOuC9xd0A'},
#        {'name': '8FaJo5TVO7TmoOI', 'value': 'bGYulAOS3ARzN3Rsyx9JJzu'},
#        {'name': 'YLBwBAUCJ05p5fx2', 'value': 'Z8lGSb7AnZKVwlIqKgRIafpIfTVufj'},
#        {'name': 'fpZCwfH', 'value': 'cqo4KOj8LSagd6VUhBrq6RJtUquwK7mJaDQsQb'},
#        {'name': 'zjUiv081bH', 'value': 'LSJtgc56ylEJGMd1AhE9QcXudC8g'},
#        {'name': 'yiWR1RtAnWH71I1', 'value': 'ruskXwdCQOfbfIgtKcetVb'},
#        {'name': 'KMKvYURaBlIEmtyX', 'value': 'NFIzhI600J5QYN'},
#        {'name': 'hbFS4sDwQh', 'value': 's4zWhushscPPDDFqT5tzPJqix0HMjjG'},
#        {'name': 'b9wAAVSyw4V2LQ', 'value': 'SDkldbPnf6NjLZSxWZV7CpCW'},
#        {'name': 'jFhFn0wPFRG', 'value': 'RYqOrD21ZN7aUeBXqISZ2afocnvvwd6hw3BXUj1wEm0mUO'}]
# value = ''
# max_skills = 0
# min_age = 1000
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for cookie in cookies:
#         browser.add_cookie(cookie)
#         browser.refresh()
#         time.sleep(0.5)
#         age = int(browser.find_element(By.ID, 'age').text.split()[1])
#         skills = len(browser.find_elements(By.TAG_NAME, 'li'))
#         if age <= min_age and skills >= max_skills:
#             max_skills = skills
#             min_age = age
#             value = cookie['value']
#         browser.delete_all_cookies()
# print(value)

# 5.7 Скроллинг страниц
# import time
# from selenium import webdriver

# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     browser.execute_script("window.scrollBy(0,5000)")
#     time.sleep(10)

# import time
# from selenium import webdriver

# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     for i in range(10):
#         browser.execute_script("window.scrollBy(0,5000)")
#         time.sleep(2)

# 5.7.1 Кодовое имя: Операция "Освобождение Пути"
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import ElementClickInterceptedException 

# url = 'http://parsinger.ru/scroll/4/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     result = 0
#     for button in browser.find_elements(By.CLASS_NAME, 'btn'):
#         try:
#             button.click()
#         except ElementClickInterceptedException:
#             browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#             button.click()
#         result += int(browser.find_element(By.ID, 'result').text)
# print(result)

# 5.7.2 Кодовое имя: "Космическая чистка урана"
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'https://parsinger.ru/selenium/5.7/1/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for button in browser.find_elements(By.CLASS_NAME, 'clickMe'):
#         button.click()
#     alert = browser.switch_to.alert
#     result = alert.text
# print(result)

# Прокрутка содержимого страницы с помощью класса Keys
# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     tags_input = browser.find_elements(By.TAG_NAME, 'input')

#     for input in tags_input:
#         input.send_keys(Keys.DOWN)
#         time.sleep(1)

# ActionChains(driver)(Цепочка действий)
# Import 
# from selenium.webdriver.common.action_chains import ActionChains


# Использование ActionChains для выполнения последовательности действий

# actions = ActionChains(driver) # Создаём экземпляр класса ActionChains
# actions.move_to_element(menu)  # Переместить курсор на элемент меню
# actions.click(submenu)         # Кликнуть по подменю
# actions.perform()              # Выполнить накопленные действия

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# # Инициализация драйвера
# driver = webdriver.Chrome()

# # Открыть веб-страницу (замените URL на ваш адрес)
# driver.get("https://parsinger.ru/selenium/5.7/2/index.html")

# # Найти элемент на странице с использованием локатора By
# draggable = driver.find_element(By.ID, "draggable")

# # Использование ActionChains для выполнения перетаскивания элемента
# actions = ActionChains(driver)

# # 1. Переместить блок влево на 100px
# actions.drag_and_drop_by_offset(draggable, -100, 0).perform()

# # 2. Переместить блок вниз на 100px
# actions.drag_and_drop_by_offset(draggable, 0, 100).perform()

# # 3. Переместить блок вправо на 100px
# actions.drag_and_drop_by_offset(draggable, 100, 0).perform()

# # 4. Переместить блок вверх на 100px
# actions.drag_and_drop_by_offset(draggable, 0, -100).perform()

# # Закрыть браузер после завершения
# driver.quit()

# 5.7.3 Операция 'Зелёный Лотос'
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# url = 'https://parsinger.ru/selenium/5.7/5/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     actions = ActionChains(browser)
#     for button in browser.find_elements(By.CLASS_NAME, 'timer_button'):
#         hold_time = float(button.get_attribute('value'))
#         actions.click_and_hold(button).pause(hold_time).release(button).perform()
#     alert = browser.switch_to.alert
#     result = alert.text
# print(result)

# 5.7.4 Поиск чисел
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by

# url = 'https://parsinger.ru/scroll/2/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     elems = browser.find_elements(by.CLASS_NAME, 'item')
#     print(len(elems))
#     nums = []
#     for elem in elems:
#         elem.find_element(by.XPATH, './input').click()
#         if (num := elem.find_element(by.XPATH, './/span').text):
#             nums.append(int(num))
# result = sum(nums)
# print(result)

# 5.7.5 Infinite scroll
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By as by

# def check_last(lst):
#     return not(any([tag.get_attribute('class') for tag in lst]))

# url = 'http://parsinger.ru/infiniti_scroll_1/'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     div = browser.find_element(by.XPATH, '//div[@id="scroll-container"]/div')
#     flag = True
#     while flag:
#         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 1000).perform()
#         flag = check_last(browser.find_elements(by.XPATH, '//div[@id="scroll-container"]/span'))
        
#     result = sum([int(tag.text) for tag in browser.find_elements(by.XPATH, '//div[@id="scroll-container"]/span')])
# print(result)

# 5.7.6 Десант в глубину: Поиск сокровищ среди скрытых элементов
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By as by

# def check_last(lst):
#     return not(any([tag.get_attribute('class') for tag in lst]))

# url = 'http://parsinger.ru/infiniti_scroll_2/'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     div = browser.find_element(by.XPATH, '//div[@id="scroll-container"]/div')
#     flag = True
#     while flag:
#         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 1000).perform()
#         flag = check_last(browser.find_elements(by.XPATH, '//div[@id="scroll-container"]/p'))
        
#     result = sum([int(tag.text) for tag in browser.find_elements(by.XPATH, '//div[@id="scroll-container"]/p')])
# print(result)

# 5.7.7 Операция "Пятерка": Одновременный Глубокий Скроллинг
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By as by

# def check_last(lst):
#     return not(any([tag.get_attribute('class') for tag in lst]))

# url = 'http://parsinger.ru/infiniti_scroll_3/'
# total = 0
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for i in range(5):
#         path = f'//div[@id="scroll-container_{i + 1}"]'
#         div = browser.find_element(by.XPATH, f'{path}/div')
#         flag = True
#         while flag:
#             ActionChains(browser).move_to_element(div).scroll_by_amount(1, 1000).perform()
#             flag = check_last(browser.find_elements(by.XPATH, f'{path}/span'))
#         res = sum([int(tag.text) for tag in browser.find_elements(by.XPATH, f'{path}/span')])
#         total += res
# print(total)

# 5.7.8 Чётный Выбор: Бесконечный Чекбоксовый список
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("force-device-scale-factor=0.75")
# chrome_options.add_argument("high-dpi-support=0.75")

# url = 'https://parsinger.ru/selenium/5.7/4/index.html'
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#     containers = []
#     while len(containers) < 100:
#         containers = browser.find_elements(by.CSS_SELECTOR, 'div.child_container')
#         ActionChains(browser).scroll_to_element(containers[-1]).perform()
#     for container in containers:
#         ActionChains(browser).move_to_element(container).perform()
#         for box in container.find_elements(by.XPATH, './input'):
#             if int(box.get_attribute('value')) % 2 == 0:
#                 ActionChains(browser).move_to_element(box).click(box).perform()
#     sleep(5)
#     browser.find_element(by.CLASS_NAME, 'alert_button').click()
#     alert = browser.switch_to.alert
#     result = alert.text
# print(result)

# 5.8.1 Условие задачи: "Поиск секретного кода"
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# url = 'https://parsinger.ru/selenium/5.8/1/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for tag in browser.find_elements(by.CLASS_NAME, 'buttons'):
#         tag.click()
#         WebDriverWait(browser, 5).until(ec.alert_is_present())
#         browser.switch_to.alert.accept()
#         if (result := browser.find_element(by.ID, 'result').text):
#             break
# print(result)

# 5.8.2 Поиск секретных пин-кодов
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from time import time

# def check_pin(pin):
#     browser.find_element(by.ID, 'input').send_keys(pin)
#     browser.find_element(by.ID, 'check').click()
#     check_result = browser.find_element(by.ID, 'result').text
#     if check_result == 'Неверный пин-код':
#         return None
#     return check_result

# url = 'https://parsinger.ru/selenium/5.8/2/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for button in browser.find_elements(by.CLASS_NAME, 'buttons'):
#         button.click()
#         tb = time()
#         WebDriverWait(browser, 5).until(ec.alert_is_present())
#         te = time()
#         print(te - tb)
#         alert = browser.switch_to.alert
#         pin = alert.text
#         alert.accept()
#         if (result := check_pin(pin)):
#             break
# print(result)

# 5.8.3 Секретный код: кибер-расследование
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# def check_pin(pin):
#     button = browser.find_element(by.ID, 'check')
#     button.click()
#     WebDriverWait(browser, 5).until(ec.alert_is_present())
#     alert = browser.switch_to.alert
#     alert.send_keys(pin)
#     alert.accept()
#     result = browser.find_element(by.ID, 'result').text
#     if result == 'Неверный пин-код':
#         return None
#     return result

# url = 'https://parsinger.ru/selenium/5.8/3/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for span in browser.find_elements(by.CLASS_NAME, 'pin'):
#         pin = span.text
#         result = check_pin(pin)
#         if result:
#             print(result)
#             break

# 5.8.4 Погружение во фреймы
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as ec

# def alert_check(iframe):
#     browser.switch_to.frame(iframe)
#     browser.find_element(by.TAG_NAME, 'button').click()
#     num = browser.find_element(by.ID, 'numberDisplay').text
#     browser.switch_to.default_content()
#     browser.find_element(by.ID, 'guessInput').clear()
#     browser.find_element(by.ID, 'guessInput').send_keys(num)
#     browser.find_element(by.ID, 'checkBtn').click()
#     try:
#         WebDriverWait(browser, 1).until(ec.alert_is_present())
#         alert = browser.switch_to.alert
#         alert_text = alert.text
#         alert.accept()
#         return alert_text
#     except TimeoutException:
#         return None

# url = 'https://parsinger.ru/selenium/5.8/5/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for iframe in browser.find_elements(by.TAG_NAME, 'iframe'):
#         code = alert_check(iframe)
#         if code:
#             print(code)
#             break

# 5.8.5 Размеры окна браузера
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from time import sleep

# dx = 16 # 16px занимают боковые границы браузера: левая и правая.
# dy = 133 # 133px занимает верхняя панель управления браузера и нижняя граница.
# url = 'https://parsinger.ru/window_size/1/'
# x, y = 553, 555+139+34
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     browser.set_window_size(x, y)
#     print(browser.get_window_size())
#     width = browser.find_element(by.ID, 'width').text
#     height = browser.find_element(by.ID, 'height').text
#     result = browser.find_element(by.ID, 'result').text
#     sleep(10)
# print(width, height, f'result = {result}', sep='\n')

# 5.8.6 Поиск секретного сочетания размера окна
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--disable-gpu')
# # chrome_options.add_argument("--disable-extensions")
# # chrome_options.add_argument("--start-maximized")
# # chrome_options.add_argument("force-device-scale-factor=0.8")
# # chrome_options.add_argument("high-dpi-support=0.8")

# window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# url = 'http://parsinger.ru/window_size/2/index.html'
# result = ''
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#     for x in window_size_x:
#         for y in window_size_y:
#             browser.set_window_size(x, y)
#             result = browser.find_element(by.ID, 'result').text
#             if result:
#                 print(result)
#                 break
#         if result:
#             break
#     else:
#         print('No result')

# 5.8.7 Таинственные размеры окна
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--disable-gpu')
# # chrome_options.add_argument("--disable-extensions")
# # chrome_options.add_argument("--start-maximized")
# # chrome_options.add_argument("force-device-scale-factor=0.8")
# # chrome_options.add_argument("high-dpi-support=0.8")

# window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# url = 'http://parsinger.ru/window_size/2/index.html'
# result = ''
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#     for x in window_size_x:
#         for y in window_size_y:
#             browser.set_window_size(x, y)
#             width = int(browser.find_element(by.ID, 'width').text.split()[1])
#             height = int(browser.find_element(by.ID, 'height').text.split()[1])
#             size = {'width': width, 'height': height}
#             result = browser.find_element(by.ID, 'result').text
#             if result:
#                 print(result, size, sep='\n')
#                 print(browser.get_window_size())
#                 break
#         if result:
#             break
#     else:
#         print('No result')

# Вкладки в браузере
# import time
# from selenium import webdriver


# with webdriver.Chrome() as browser:
#     result = []
#     browser.get('http://parsinger.ru/blank/2/1.html')
#     time.sleep(1)
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
#     time.sleep(2)
#     print(browser.window_handles)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep

# with webdriver.Chrome() as browser:
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/1.html", "_blank1");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank2");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank3");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank4");')

#     for page in browser.window_handles:
#         browser.switch_to.window(page)
#         sleep(5)
#         for y in browser.find_elements(By.CLASS_NAME, 'check'):
#             y.click()

# import time
# from selenium import webdriver
# with webdriver.Chrome() as browser:
#     time.sleep(1)
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')

#     for page in browser.window_handles:
#         browser.switch_to.window(page)
#         time.sleep(1)
#         print(browser.execute_script("return document.title;"), page)

# from selenium import webdriver
# with webdriver.Chrome() as browser:
#     browser.get("https://stepik.org/course/104774/promo")
#     print(browser.execute_script("return document.title;"))

# 5.8.8 Охотник за загадочными числами
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by

# url = 'http://parsinger.ru/blank/3/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     total = 0
#     for button in browser.find_elements(by.CLASS_NAME, 'buttons'):
#         button.click()
#     current_page = browser.current_window_handle
#     pages = browser.window_handles
#     pages.remove(current_page)
#     for page in pages:
#         browser.switch_to.window(page)
#         total += int(browser.execute_script('return document.title;'))
# print(total)

# 5.8.9 Откройте сокровища интернета
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from math import sqrt

# sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
#          'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html']
# nums = []
# with webdriver.Chrome() as browser:
#     browser.get(sites[0])
#     for site in sites[1:]:
#         browser.execute_script(f'window.open("{site}", "_blank");')
#     for page in browser.window_handles:
#         browser.switch_to.window(page)
#         browser.find_element(by.CLASS_NAME, 'checkbox_class').click()
#         nums.append(int(browser.find_element(by.ID, 'result').text))
# result = round(sum(map(sqrt, nums)), 9)
# print(result)

# 5.9.1 Ожидание title
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from time import sleep

# url1 = 'https://parsinger.ru/expectations/3/index.html'
# url2 = 'https://stepik.org/lesson/715955/step/5?auth=login&unit=716749'
# with webdriver.Chrome() as browser:
#     browser.get(url1)
#     WebDriverWait(browser, 10).until(ec.element_to_be_clickable((by.ID, 'btn'))).click()
#     WebDriverWait(browser, 20).until(ec.title_is('345FDG3245SFD'))
#     result = browser.find_element(by.ID, 'result').text
# print(result)
    # browser.get(url2)
    # sleep(10)
    # browser.find_element(by.XPATH, '//input[@placeholder="Введите число"]').send_keys(result)
    # WebDriverWait(browser, 10).until(ec.element_to_be_clickable((by.XPATH, '//button[@class="submit-submission"]'))).click()
    # sleep(20)

# 5.9.2 Тайный заголовок
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# url = 'https://parsinger.ru/expectations/4/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     WebDriverWait(browser, 5).until(ec.element_to_be_clickable((by.ID, 'btn'))).click()
#     if WebDriverWait(browser, 20, 0.1).until(ec.title_contains('JK8HQ')):
#         title = browser.title
#         print(title)

# 5.9.3 Мимолётные теги
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# url = 'https://parsinger.ru/expectations/6/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     browser.find_element(by.ID, 'btn').click()
#     element = WebDriverWait(browser, 20).until(ec.presence_of_element_located((by.CLASS_NAME, 'BMH21YY')))
#     print(element.text)

# 5.9.4 Охота на таинственный Блок
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# url = 'https://parsinger.ru/selenium/5.9/2/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     WebDriverWait(browser, 30).until(ec.presence_of_element_located((by.ID, 'qQm9y1rk'))).click()
#     WebDriverWait(browser, 5).until(ec.alert_is_present())
#     alert = browser.switch_to.alert
#     result = alert.text
# print(result)

# 5.9.5 Познание атрибута display
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# url = 'https://parsinger.ru/selenium/5.9/3/index.html'
# ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     for iid in ids_to_find:
#         WebDriverWait(browser, 100).until(ec.visibility_of_element_located((by.ID, iid))).click()
#     WebDriverWait(browser, 5).until(ec.alert_is_present())
#     alert = browser.switch_to.alert
#     result = alert.text
# print(result)

# 5.9.6 Триумф над рекламным Заговором
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("force-device-scale-factor=0.75")

# url = 'https://parsinger.ru/selenium/5.9/4/index.html'
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#     browser.find_element(by.CLASS_NAME, 'close').click()
#     WebDriverWait(browser, 30).until(ec.invisibility_of_element_located((by.ID, 'ad')))
#     browser.find_element(by.TAG_NAME, 'button').click()
#     result = browser.find_element(by.ID, 'message').text
# print(result)

# 5.9.7 Коллекционер секретных рун
# from selenium import webdriver
# from selenium.webdriver.common.by import By as by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from time import sleep
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("force-device-scale-factor=0.75")

# url = 'https://parsinger.ru/selenium/5.9/5/index.html'
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#     boxes = browser.find_elements(by.CLASS_NAME, 'box_button')
#     for box in boxes:
#         WebDriverWait(browser, 30).until(ec.element_to_be_clickable(box)).click()
#         browser.find_element(by.ID, 'close_ad').click()
#         WebDriverWait(browser, 30).until(ec.invisibility_of_element_located((by.ID, 'ad_window')))
#         sleep(10)
#     code = '-'.join([box.text for box in boxes])
# print(code)