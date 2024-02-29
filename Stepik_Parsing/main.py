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