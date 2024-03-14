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
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/methods/5/index.html'
cookie_info = []
with webdriver.Chrome() as webdriver:
    webdriver.get(url)
    for link in webdriver.find_elements(By.TAG_NAME, 'a'):
        link.click()
        cookie = webdriver.get_cookies()[0]
        expiry = int(cookie['expiry'])
        num = webdriver.find_element(By.ID, 'result').text
        cookie_info.append((expiry, num))
        webdriver.back()
print(max(cookie_info)[1])