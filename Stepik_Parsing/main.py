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
import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('Stepik_Parsing/chrome_ext_pak/coordinates.crx')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)