# import asyncio
# import aiohttp
# from codetiming import Timer

# #---------------------start block 1------------------------
# urls = ["http://google.com",
#         "http://yahoo.com",
#         "http://apple.com",
#         "http://microsoft.com",
#         "https://habr.com/",
#         "https://www.youtube.com/",
#         "https://stepik.org/",
#         "https://docs.python.org/",
#         "https://stackoverflow.com/",
#         "https://www.reg.ru/"]
# #---------------------end block 1------------------------



# #---------------------start block 2------------------------
# async def main(url):
#     with Timer(text=f"Затрачено времени на запрос: {{:.3f}} сек"):
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as resp:
#                 print(resp.url)
# #---------------------end block 2------------------------


# async def run_tasks():
#     tasks = [main(link) for link in urls]
#     await asyncio.gather(*tasks)

# #---------------------start block 3------------------------
# if __name__ == '__main__':
#     #   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     asyncio.run(run_tasks())
# #---------------------end block 3------------------------

# import asyncio
# from time import sleep


# async def nested(name, sl):
#     print(f'{name} start')
#     await asyncio.sleep(sl)
#     # sleep(sl)
#     print(f'{name} complete')
#     # return(f'result {name}')


# async def main():
#     # await nested('Task1', 5)
#     # await nested('Task2', 2)
#     await asyncio.gather(nested('Task1', 5), nested('Task2', 2))
#     # result = await asyncio.gather(task1, task2)
#     # print(result) 

# asyncio.run(main())

# import asyncio
# import random
# import time

# async def one():
#     # Получаем текущее время в секундах с начала эпохи. 
#     start = time.time()
#     await asyncio.sleep((sleep_time := random.randint(1, 3)))
#     # Получаем имя текущей задачи и выводим сообщение с временем ее выполнения:
#     print(f'{asyncio.current_task().get_name()} ({sleep_time=}) выполнена за {time.time() - start}')

# async def main():
#     # Создание списка задач.
#     lst_tasks = []
#     for x in range(10):
#         # Корутины должны быть явно обернуты в Task.
#         task = asyncio.create_task(one(), name=f'Задача_{x}')
#         lst_tasks.append(task)
#     done, pending = await asyncio.wait(lst_tasks, timeout=2)
#     print(f'Не успели выполниться: {[task.get_name() for task in pending]}')
#     print(done, pending, sep='\n')
#     # Даем время выполниться оставшимся задачам
#     await asyncio.sleep(3)

# asyncio.run(main())

# import asyncio

# import aiohttp


# async def main():
#     async with aiohttp.ClientSession(trust_env=True) as session:
#         async with session.get('https://parsinger.ru/html/index1_page_1.html') as response:
#             print(await response.text())

# asyncio.run(main())

# import aiohttp
# import asyncio

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
# url = 'http://httpbin.org/get'
# data = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}

# async def main():
#     async with aiohttp.ClientSession(trust_env=True) as session:
#         async with session.get(url=url, headers=headers, timeout=2, params=data) as response:
#             print(await response.text())

# asyncio.run(main())

# import time
# import aiohttp
# import asyncio
# import aiofiles

# url = 'http://httpbin.org/ip'


# async def check_proxy(prx, semaphore):
#     proxy = f'http://{prx}'
#     async with semaphore:
#         try:
#             async with aiohttp.ClientSession() as session:
#                 async with session.get(url=url, proxy=proxy, timeout=1) as response:
#                     if response.ok:
#                         return f'good proxy, status_code: {response.status}, {prx}'
#                     else:
#                         return f'bad proxy, status_code: {response.status}, {prx}'
#         except Exception as e:
#             return f'bad proxy, Error: {e.__class__.__name__}, {prx}'


# async def main():
#     # Внимание! Этот оператор ограничивает количество одновременно выполняемых задач
#     # Если код падает с ошибкой ValueError: too many file descriptors in select(), 
#     # уменьшите это число
#     semaphore = asyncio.BoundedSemaphore(500)

#     async with aiofiles.open('Stepik_Parsing/proxy1.txt', mode='r', encoding='utf8') as f:
#         # Получаем список прокси из файла
#         proxies = await f.readlines()
#         # Создаем и асинхронно запускаем список задач на проверку прокси
#         tasks = [check_proxy(prx.strip(), semaphore) for prx in proxies]
#         # Ждем, пока выполнятся все проверки
#         result = await asyncio.gather(*tasks, return_exceptions=True)
#         # Выводим результат проверки
#         print(f"Всего проверено: {len(result)} шт.")
#         print(*result, sep='\n')


# start = time.time()
# asyncio.run(main())
# print(f'Затрачено времени: {time.time() - start} секунд')

# import aiohttp
# import asyncio
# from aiohttp_socks import ProxyConnector, ProxyType


# async def main():
#     timeout = aiohttp.ClientTimeout(total=1)
#     url = 'http://httpbin.org/ip'
#     connector = ProxyConnector(
#             proxy_type=ProxyType.SOCKS5,
#             host='92.204.135.37',
#             port=2287,
#             rdns=True
#             )

#     async with aiohttp.ClientSession(connector=connector, timeout=timeout, trust_env=True) as session:
#         async with session.get(url=url, timeout=1) as response:
#             if response.status:
#                 print(f'good proxy, status_code -{response.status}-', end='')
#             elif response.status >= 400:
#                 print(f'bad proxy, status_code -{response.status}-', end='')

# asyncio.run(main())

# ****************************************
# **** 6.8 Приготовление асинхронного супа
# ****************************************

# ПРИМЕР 1
# *************

# import aiohttp
# import asyncio
# from bs4 import BeautifulSoup


# async def main():
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url=url, timeout=1) as response:
#             soup = BeautifulSoup(await response.text(), 'lxml')
#             name = soup.find_all('a', class_='name_item')
#             price = soup.find_all('p', class_='price')
#             for n, p in zip(name, price):
#                 print(n.text, p.text)

# asyncio.run(main())

# ПРИМЕР 2 асинхр (время вып 0.9504497051239014 сек)
# *************

# import asyncio
# import time
# import aiohttp
# from bs4 import BeautifulSoup

# # ---------------------start block 1------------------------
# category = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']
# urls = [f'https://parsinger.ru/html/{cat}/{i}/{i}_{x}.html' for cat, i in zip(category, range(1, len(category) + 1)) for
#         x in range(1, 33)]
# # ---------------------end block 1------------------------

# # ---------------------start block 2------------------------
# async def run_tasks(url, session):
#     async with session.get(url) as resp:
#         soup = BeautifulSoup(await resp.text(), 'lxml')
#         price = soup.find('span', id='price').text
#         name = soup.find('p', id='p_header').text
#         print(resp.url, price, name)
# # ---------------------end block 2------------------------

# # ---------------------start block 3------------------------
# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = [run_tasks(link, session) for link in urls]
#         await asyncio.gather(*tasks)
# # ---------------------end block 3------------------------

# # ---------------------start block 4------------------------

# if __name__ == '__main__':
#     start = time.time()
#     asyncio.run(main())
#     print(time.time()-start)

# ПРИМЕР 2 синхр (время вып 22.20810580253601 сек)
# *************

# import time
# import requests as r
# from bs4 import BeautifulSoup

# # ---------------------start block 1------------------------
# category = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']
# urls = [f'https://parsinger.ru/html/{cat}/{i}/{i}_{x}.html' for cat, i in zip(category, range(1, len(category) + 1)) for
#         x in range(1, 33)]
# # ---------------------end block 1------------------------

# # ---------------------start block 2------------------------
# def run_tasks(url, session):
#     with session.get(url) as resp:
#         resp.encoding = 'utf-8'
#         soup = BeautifulSoup(resp.text, 'lxml')
#         price = soup.find('span', id='price').text
#         name = soup.find('p', id='p_header').text
#         print(resp.url, price, name)
# # ---------------------end block 2------------------------

# # ---------------------start block 3------------------------
# start = time.time()
# with r.Session() as session:
#     for link in urls:
#         run_tasks(link, session)
# print(time.time()-start)
# ---------------------end block 3------------------------

# ПРИМЕР 3
# *************
# import aiohttp
# import asyncio
# import requests
# from bs4 import BeautifulSoup

# category_lst = []
# pagen_lst = []
# domain = 'https://parsinger.ru/html/'


# def get_soup(url):
#     resp = requests.get(url=url)
#     return BeautifulSoup(resp.text, 'lxml')


# def get_urls_categories(soup):
#     all_link = soup.find('div', class_='nav_menu').find_all('a')

#     for cat in all_link:
#         category_lst.append(domain + cat['href'])


# def get_urls_pages(category_lst):
#     for cat in category_lst:
#         resp = requests.get(url=cat)
#         soup = BeautifulSoup(resp.text, 'lxml')
#         for pagen in soup.find('div', class_='pagen').find_all('a'):
#             pagen_lst.append(domain + pagen['href'])


# async def get_data(session, link):
#     async with session.get(url=link) as response:
#         resp = await response.text()
#         soup = BeautifulSoup(resp, 'lxml')
#         item_card = [x['href'] for x in soup.find_all('a', class_='name_item')]
#         for x in item_card:
#             url2 = domain + x
#             async with session.get(url=url2) as response2:
#                 resp2 = await response2.text()
#                 soup2 = BeautifulSoup(resp2, 'lxml')
#                 article = soup2.find('p', class_='article').text
#                 name = soup2.find('p', id='p_header').text
#                 price = soup2.find('span', id='price').text
#                 print(url2, price, article, name)


# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for link in pagen_lst:
#             task = asyncio.create_task(get_data(session, link))
#             tasks.append(task)
#         await asyncio.gather(*tasks)


# url = 'https://parsinger.ru/html/index1_page_1.html'
# soup = get_soup(url)
# get_urls_categories(soup)
# get_urls_pages(category_lst)

# asyncio.run(main())

# ПРИМЕР 3 (ООП)
# *************

# import aiohttp
# import asyncio
# import requests
# from bs4 import BeautifulSoup

# class Parser:
#     def __init__(self, domain) -> None:
#         self._domain = domain
#         self._category_lst, self._pagen_lst = [], []

#     @staticmethod
#     def get_soup(url):
#         resp = requests.get(url=url)
#         return BeautifulSoup(resp.text, 'lxml')

#     def get_urls_categories(self, soup):
#         all_link = soup.find('div', class_='nav_menu').find_all('a')
#         for cat in all_link:
#             self._category_lst.append(self._domain + cat['href'])

#     def get_urls_pages(self):
#         for cat in self._category_lst:
#             soup = self.get_soup(cat)
#             for pagen in soup.find('div', class_='pagen').find_all('a'):
#                 self._pagen_lst.append(self._domain + pagen['href'])

#     async def get_data(self, session, link):
#         async with session.get(url=link) as response:
#             resp = await response.text()
#             soup = BeautifulSoup(resp, 'lxml')
#             item_card = [x['href'] for x in soup.find_all('a', class_='name_item')]
#             for x in item_card:
#                 url2 = self._domain + x
#                 async with session.get(url=url2) as response2:
#                     resp2 = await response2.text()
#                     soup2 = BeautifulSoup(resp2, 'lxml')
#                     article = soup2.find('p', class_='article').text
#                     name = soup2.find('p', id='p_header').text
#                     price = soup2.find('span', id='price').text
#                     print(url2, price, article, name)

#     async def main(self):
#         async with aiohttp.ClientSession() as session:
#             tasks = []
#             for link in self._pagen_lst:
#                 task = asyncio.create_task(self.get_data(session, link))
#                 tasks.append(task)

#             await asyncio.gather(*tasks)
    
#     def __call__(self, url, *args, **kwargs):
#         soup = self.get_soup(url)
#         self.get_urls_categories(soup)
#         self.get_urls_pages()
#         asyncio.run(self.main())

# if __name__ == '__main__':
#     parse_site = Parser(domain='https://parsinger.ru/html/')
#     parse_site('https://parsinger.ru/html/index1_page_1.html')

# import time
# import asyncio
# import aiohttp
# from aiohttp_retry import RetryClient, ExponentialRetry

# # Последние 2 ссылки — 404-е, добавлены в демонстрационных целях
# links = ['https://parsinger.ru/html/watch/1/1_1.html',
#          'https://parsinger.ru/html/watch/1/1_2.html',
#          'https://parsinger.ru/html/watch/1/1_3.html',
#          'https://parsinger.ru/html/watch/8/1_3.html',
#          'https://parsinger.ru/html/watch/8/2_3.html']


# # Корутина для вывода сообщения вида link:response.status
# async def get_data(retry_client, link):
#     async with retry_client.get(link) as response:
#         print(f'{link}:{response.status}')


# # Базовая корутина
# async def main():
#     async with aiohttp.ClientSession() as client_session:
#         # statuses=[404] выбран для демонстрации, на практике
#         # повторное обращение к несуществующей странице скорее всего бессмысленно
#         retry_options = ExponentialRetry(attempts=4, statuses={404})
#         async with RetryClient(
#                 raise_for_status=False, retry_options=retry_options,
#                 client_session=client_session) as retry_client:
#             await asyncio.gather(*[get_data(retry_client, link) for link in links])


# if __name__ == '__main__':
#     start = time.time()
#     asyncio.run(main())
#     print(f'время:{time.time() - start}')

# 6.8.1 Приготовление асинхронного супа. Задача 1

# ***** СИНХР

# import requests
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# from time import time

# def get_soup(url):
#     resp = requests.get(url)
#     resp.encoding = 'utf-8'
#     return BeautifulSoup(resp.text, 'lxml')

# def get_categories(soup):
#     links = soup.find('div', class_='nav_menu').select('a')
#     for link in links:
#         categories.append(domain + link['href'])

# def get_pages(cat_lst):
#     for cat in cat_lst:
#         soup = get_soup(cat)
#         links = soup.find('div', class_='pagen').select('a') # type: ignore
#         for link in links:
#             pages.append(domain + link['href']) # type: ignore

# def get_data(session, link):
#     with session.get(link) as responce:
#         soup = BeautifulSoup(responce.text, 'lxml')
#         cards = [domain + card['href'] for card in soup.select('a.name_item')] # type: ignore
#         discount_sum = 0
#         for card in cards:
#             with session.get(card) as response2:
#                 soup = BeautifulSoup(response2.text, 'lxml')
#                 qt = int(soup.find('span', id='in_stock').text.split()[-1]) # type: ignore
#                 old_price = int(soup.find('span', id='old_price').text.split()[0]) # type: ignore
#                 price = int(soup.find('span', id='price').text.split()[0]) # type: ignore
#                 discount = (old_price - price) * qt
#                 discount_sum += discount
#     return discount_sum

# def main():
#     ua = UserAgent()
#     headers = {'user-agent': ua.random}
#     with requests.Session() as session:
#         session.headers.update(headers)
#         discounts = [get_data(session, link) for link in pages]
#         result = sum(discounts)
#     print('Общий размер скидки для всех товаров:', result)

# if __name__ == '__main__':
#     start_time = time()
#     categories = []
#     pages = []
#     domain = 'https://parsinger.ru/html/'
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     soup = get_soup(url)
#     get_categories(soup)
#     get_pages(categories)
#     main()
#     print('Время выполнения:', time() - start_time)


# ***** АСИНХР 1

# import asyncio
# import aiohttp
# import requests
# from bs4 import BeautifulSoup
# from aiohttp_retry import RetryClient, ExponentialRetry
# from fake_useragent import UserAgent
# from time import time

# def get_soup(url): # type: ignore
#     resp = requests.get(url)
#     resp.encoding = 'utf-8'
#     return BeautifulSoup(resp.text, 'lxml')

# def get_categories(soup):
#     links = soup.find('div', class_='nav_menu').select('a')
#     for link in links:
#         categories.append(domain + link['href'])

# def get_pages(cat_lst):
#     for cat in cat_lst:
#         soup = get_soup(cat)
#         links = soup.find('div', class_='pagen').select('a') # type: ignore
#         for link in links:
#             pages.append(domain + link['href']) # type: ignore

# async def get_data(session, link):
#     retry_opt = ExponentialRetry(attempts=5)
#     retry_client = RetryClient(raise_for_status=False, retry_options=retry_opt, client_session=session, start_timeout=0.5)
#     async with retry_client.get(link) as responce:
#         soup = BeautifulSoup(await responce.text(), 'lxml')
#         cards = [domain + card['href'] for card in soup.select('a.name_item')] # type: ignore
#         discount_sum = 0
#         for card in cards:
#             async with retry_client.get(card) as response2:
#                 soup = BeautifulSoup(await response2.text(), 'lxml')
#                 qt = int(soup.find('span', id='in_stock').text.split()[-1]) # type: ignore
#                 old_price = int(soup.find('span', id='old_price').text.split()[0]) # type: ignore
#                 price = int(soup.find('span', id='price').text.split()[0]) # type: ignore
#                 discount = (old_price - price) * qt
#                 discount_sum += discount
#     return discount_sum

# async def main():
#     ua = UserAgent()
#     headers = {'user-agent': ua.random}
#     async with aiohttp.ClientSession(headers=headers) as session:
#         tasks = [asyncio.create_task(get_data(session, link)) for link in pages]
#         result = sum(await asyncio.gather(*tasks))
#     print('Общий размер скидки для всех товаров:', result)

# if __name__ == '__main__':
#     start_time = time()
#     categories = []
#     pages = []
#     domain = 'https://parsinger.ru/html/'
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     soup = get_soup(url)
#     get_categories(soup)
#     get_pages(categories)

#     asyncio.run(main())
#     print('Время выполнения:', time() - start_time)

# ***** АСИНХР 2

# import asyncio
# import aiohttp
# import requests
# from bs4 import BeautifulSoup
# from aiohttp_retry import RetryClient, ExponentialRetry
# from fake_useragent import UserAgent
# from time import time

# def get_categories(link):
#     resp = requests.get(link)
#     resp.encoding = 'utf-8'
#     soup = BeautifulSoup(resp.text, 'lxml')
#     categories = [domain + cat['href'] for cat in soup.find('div', class_='nav_menu').select('a')]
#     return categories

# async def get_soup(session, url):
#     async with session.get(url) as response:
#         resp = await response.text()
#         return BeautifulSoup(resp, 'lxml')

# async def get_pages_links(session, url):
#     soup = await get_soup(session, url)
#     pages = [domain + page['href'] for page in soup.find('div', class_='pagen').select('a')]
#     for page in pages:
#         pages_links.append(page)
#     return pages

# async def get_data(session, url):
#     soup = await get_soup(session, url)
#     cards = [domain + card['href'] for card in soup.select('a.name_item')]
#     discount_sum = 0
#     for card in cards:
#         soup = await get_soup(session, card)
#         qt = int(soup.find('span', id='in_stock').text.split()[-1])
#         old_price = int(soup.find('span', id='old_price').text.split()[0])
#         price = int(soup.find('span', id='price').text.split()[0])
#         discount = (old_price - price) * qt
#         discount_sum += discount
#     return discount_sum

# async def main():
#     ua = UserAgent()
#     headers = {'user-agent': ua.random}
#     async with aiohttp.ClientSession(headers=headers) as session:
#         retry_opt = ExponentialRetry(attempts=5)
#         rc_session = RetryClient(raise_for_status=False, retry_options=retry_opt, client_session=session, start_timeout=0.5)
#         tasks1 = [asyncio.create_task(get_pages_links(rc_session, cat)) for cat in categories_links]
#         sss = await asyncio.gather(*tasks1)
#         tasks2 = [asyncio.create_task(get_data(rc_session, page)) for page in pages_links]
#         result = sum(await asyncio.gather(*tasks2))
#         print('Общий размер скидки для всех товаров:', result)

# if __name__ == '__main__':
#     start_time = time()
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     domain = 'https://parsinger.ru/html/'
#     pages_links = []
#     categories_links = get_categories(url)
#     asyncio.run(main())
#     print('Время выполнения:', time() - start_time)

# ***** АСИНХР 3

# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
# from aiohttp_retry import RetryClient, ExponentialRetry
# from fake_useragent import UserAgent
# from time import time

# async def get_soup(session, url):
#     async with session.get(url) as response:
#         resp = await response.text()
#         return BeautifulSoup(resp, 'lxml')

# async def get_data(session, link):
#     soup = await get_soup(session, link)
#     qt = int(soup.find('span', id='in_stock').text.split()[-1])
#     old_price = int(soup.find('span', id='old_price').text.split()[0])
#     price = int(soup.find('span', id='price').text.split()[0])
#     discount = (old_price - price) * qt
#     return discount

# async def task_generator(session, url):
#     domain = 'https://parsinger.ru/html/'
#     soup = await get_soup(session, url)
#     categories = [domain + cat['href'] for cat in soup.find('div', class_='nav_menu').select('a')]
#     for cat in categories:
#         soup = await get_soup(session, cat)
#         pages = [domain + page['href'] for page in soup.find('div', class_='pagen').select('a')]
#         for page in pages:
#             soup = await get_soup(session, page)
#             cards = [domain + card['href'] for card in soup.select('a.name_item')]
#             for card in cards:
#                 yield asyncio.create_task(get_data(session, card))

# async def main():
#     ua = UserAgent()
#     headers = {'user-agent': ua.random}
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     async with aiohttp.ClientSession(headers=headers) as session:
#         retry_opt = ExponentialRetry(attempts=5)
#         rc_session = RetryClient(raise_for_status=False, retry_options=retry_opt, client_session=session, start_timeout=0.5)
#         tasks = [task async for task in task_generator(rc_session, url)]
#         result = sum(await asyncio.gather(*tasks))
#     print('Общий размер скидки для всех товаров:', result)

# if __name__ == '__main__':
#     start_time = time()
#     asyncio.run(main())
#     print('Время выполнения:', time() - start_time)

    # ***** АСИНХР 4

# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
# from aiohttp_retry import RetryClient, ExponentialRetry
# from fake_useragent import UserAgent
# from time import time

# async def get_soup(session, url):
#     async with session.get(url) as response:
#         resp = await response.text()
#         return BeautifulSoup(resp, 'lxml')

# async def get_data(session, link):
#     soup = await get_soup(session, link)
#     cards = [domain + card['href'] for card in soup.select('a.name_item')]
#     discount_sum = 0
#     for card in cards:
#         soup = await get_soup(session, card)
#         qt = int(soup.find('span', id='in_stock').text.split()[-1])
#         old_price = int(soup.find('span', id='old_price').text.split()[0])
#         price = int(soup.find('span', id='price').text.split()[0])
#         discount = (old_price - price) * qt
#         discount_sum += discount
#     return discount_sum

# async def task_generator(session, url):
#     soup = await get_soup(session, url)
#     categories = [domain + cat['href'] for cat in soup.find('div', class_='nav_menu').select('a')]
#     for cat in categories:
#         soup = await get_soup(session, cat)
#         pages = [domain + page['href'] for page in soup.find('div', class_='pagen').select('a')]
#         for page in pages:
#             yield asyncio.create_task(get_data(session, page))

# async def main():
#     ua = UserAgent()
#     headers = {'user-agent': ua.random}
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     async with aiohttp.ClientSession(headers=headers) as session:
#         retry_opt = ExponentialRetry(attempts=5)
#         rc_session = RetryClient(raise_for_status=False, retry_options=retry_opt, client_session=session, start_timeout=0.5)
#         tasks = [task async for task in task_generator(rc_session, url)]
#         result = sum(await asyncio.gather(*tasks))
#     print('Общий размер скидки для всех товаров:', result)

# if __name__ == '__main__':
#     start_time = time()
#     domain = 'https://parsinger.ru/html/'
#     asyncio.run(main())
#     print('Время выполнения:', time() - start_time)

# 6.8 Приготовление асинхронного супа. Задача 2

# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup

# async def get_response(session, link):
#     async with session.get(link) as response:
#         if response.ok:
#             resp = await response.text()
#             soup = BeautifulSoup(resp, 'lxml')
#             return int(soup.find('p', class_='text').text)
#         else:
#             return 0

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             resp = await response.text()
#             soup = BeautifulSoup(resp, 'lxml')
#             all_links = [domain + link['href'] for link in soup.select('a')]
#             tasks = [asyncio.create_task(get_response(session, link)) for link in all_links]
#             result = sum(await asyncio.gather(*tasks))
#     print(result)

# domain = 'https://parsinger.ru/asyncio/create_soup/1/'
# url = 'https://parsinger.ru/asyncio/create_soup/1/index.html'
# asyncio.run(main())

# fjfjfjgit 
# 111111

# import asyncio
# import aiohttp
# from codetiming import Timer

# #---------------------start block 1------------------------
# urls = ["http://google.com",
#         "http://yahoo.com",
#         "http://apple.com",
#         "http://microsoft.com",
#         "https://habr.com/",
#         "https://www.youtube.com/",
#         "https://stepik.org/",
#         "https://docs.python.org/",
#         "https://stackoverflow.com/",
#         "https://www.reg.ru/"]
# #---------------------end block 1------------------------



# #---------------------start block 2------------------------
# async def main(url):
#     with Timer(text=f"Затрачено времени на запрос: {{:.3f}} сек"):
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as resp:
#                 print(resp.url)
# #---------------------end block 2------------------------


# async def run_tasks():
#     tasks = [main(link) for link in urls]
#     await asyncio.gather(*tasks)

# #---------------------start block 3------------------------
# if __name__ == '__main__':
#     #   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     asyncio.run(run_tasks())
# #---------------------end block 3------------------------

# import asyncio
# from time import sleep


# async def nested(name, sl):
#     print(f'{name} start')
#     await asyncio.sleep(sl)
#     # sleep(sl)
#     print(f'{name} complete')
#     # return(f'result {name}')


# async def main():
#     # await nested('Task1', 5)
#     # await nested('Task2', 2)
#     await asyncio.gather(nested('Task1', 5), nested('Task2', 2))
#     # result = await asyncio.gather(task1, task2)
#     # print(result) 

# asyncio.run(main())

# import asyncio
# import random
# import time

# async def one():
#     # Получаем текущее время в секундах с начала эпохи. 
#     start = time.time()
#     await asyncio.sleep((sleep_time := random.randint(1, 3)))
#     # Получаем имя текущей задачи и выводим сообщение с временем ее выполнения:
#     print(f'{asyncio.current_task().get_name()} ({sleep_time=}) выполнена за {time.time() - start}')

# async def main():
#     # Создание списка задач.
#     lst_tasks = []
#     for x in range(10):
#         # Корутины должны быть явно обернуты в Task.
#         task = asyncio.create_task(one(), name=f'Задача_{x}')
#         lst_tasks.append(task)
#     done, pending = await asyncio.wait(lst_tasks, timeout=2)
#     print(f'Не успели выполниться: {[task.get_name() for task in pending]}')
#     print(done, pending, sep='\n')
#     # Даем время выполниться оставшимся задачам
#     await asyncio.sleep(3)

# asyncio.run(main())

# import asyncio

# import aiohttp


# async def main():
#     async with aiohttp.ClientSession(trust_env=True) as session:
#         async with session.get('https://parsinger.ru/html/index1_page_1.html') as response:
#             print(await response.text())

# asyncio.run(main())

# import aiohttp
# import asyncio

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
# url = 'http://httpbin.org/get'
# data = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}

# async def main():
#     async with aiohttp.ClientSession(trust_env=True) as session:
#         async with session.get(url=url, headers=headers, timeout=2, params=data) as response:
#             print(await response.text())

# asyncio.run(main())

# import time
# import aiohttp
# import asyncio
# import aiofiles

# url = 'http://httpbin.org/ip'


# async def check_proxy(prx, semaphore):
#     proxy = f'http://{prx}'
#     async with semaphore:
#         try:
#             async with aiohttp.ClientSession() as session:
#                 async with session.get(url=url, proxy=proxy, timeout=1) as response:
#                     if response.ok:
#                         return f'good proxy, status_code: {response.status}, {prx}'
#                     else:
#                         return f'bad proxy, status_code: {response.status}, {prx}'
#         except Exception as e:
#             return f'bad proxy, Error: {e.__class__.__name__}, {prx}'


# async def main():
#     # Внимание! Этот оператор ограничивает количество одновременно выполняемых задач
#     # Если код падает с ошибкой ValueError: too many file descriptors in select(), 
#     # уменьшите это число
#     semaphore = asyncio.BoundedSemaphore(500)

#     async with aiofiles.open('Stepik_Parsing/proxy1.txt', mode='r', encoding='utf8') as f:
#         # Получаем список прокси из файла
#         proxies = await f.readlines()
#         # Создаем и асинхронно запускаем список задач на проверку прокси
#         tasks = [check_proxy(prx.strip(), semaphore) for prx in proxies]
#         # Ждем, пока выполнятся все проверки
#         result = await asyncio.gather(*tasks, return_exceptions=True)
#         # Выводим результат проверки
#         print(f"Всего проверено: {len(result)} шт.")
#         print(*result, sep='\n')


# start = time.time()
# asyncio.run(main())
# print(f'Затрачено времени: {time.time() - start} секунд')

# import aiohttp
# import asyncio
# from aiohttp_socks import ProxyConnector, ProxyType


# async def main():
#     timeout = aiohttp.ClientTimeout(total=1)
#     url = 'http://httpbin.org/ip'
#     connector = ProxyConnector(
#             proxy_type=ProxyType.SOCKS5,
#             host='92.204.135.37',
#             port=2287,
#             rdns=True
#             )

#     async with aiohttp.ClientSession(connector=connector, timeout=timeout, trust_env=True) as session:
#         async with session.get(url=url, timeout=1) as response:
#             if response.status:
#                 print(f'good proxy, status_code -{response.status}-', end='')
#             elif response.status >= 400:
#                 print(f'bad proxy, status_code -{response.status}-', end='')

# asyncio.run(main())

# ****************************************
# **** 6.8 Приготовление асинхронного супа
# ****************************************

# ПРИМЕР 1
# *************

# import aiohttp
# import asyncio
# from bs4 import BeautifulSoup


# async def main():
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url=url, timeout=1) as response:
#             soup = BeautifulSoup(await response.text(), 'lxml')
#             name = soup.find_all('a', class_='name_item')
#             price = soup.find_all('p', class_='price')
#             for n, p in zip(name, price):
#                 print(n.text, p.text)

# asyncio.run(main())

# ПРИМЕР 2 асинхр (время вып 0.9504497051239014 сек)
# *************

# import asyncio
# import time
# import aiohttp
# from bs4 import BeautifulSoup

# # ---------------------start block 1------------------------
# category = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']
# urls = [f'https://parsinger.ru/html/{cat}/{i}/{i}_{x}.html' for cat, i in zip(category, range(1, len(category) + 1)) for
#         x in range(1, 33)]
# # ---------------------end block 1------------------------

# # ---------------------start block 2------------------------
# async def run_tasks(url, session):
#     async with session.get(url) as resp:
#         soup = BeautifulSoup(await resp.text(), 'lxml')
#         price = soup.find('span', id='price').text
#         name = soup.find('p', id='p_header').text
#         print(resp.url, price, name)
# # ---------------------end block 2------------------------

# # ---------------------start block 3------------------------
# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = [run_tasks(link, session) for link in urls]
#         await asyncio.gather(*tasks)
# # ---------------------end block 3------------------------

# # ---------------------start block 4------------------------

# if __name__ == '__main__':
#     start = time.time()
#     asyncio.run(main())
#     print(time.time()-start)

# ПРИМЕР 2 синхр (время вып 22.20810580253601 сек)
# *************

# import time
# import requests as r
# from bs4 import BeautifulSoup

# # ---------------------start block 1------------------------
# category = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']
# urls = [f'https://parsinger.ru/html/{cat}/{i}/{i}_{x}.html' for cat, i in zip(category, range(1, len(category) + 1)) for
#         x in range(1, 33)]
# # ---------------------end block 1------------------------

# # ---------------------start block 2------------------------
# def run_tasks(url, session):
#     with session.get(url) as resp:
#         resp.encoding = 'utf-8'
#         soup = BeautifulSoup(resp.text, 'lxml')
#         price = soup.find('span', id='price').text
#         name = soup.find('p', id='p_header').text
#         print(resp.url, price, name)
# # ---------------------end block 2------------------------

# # ---------------------start block 3------------------------
# start = time.time()
# with r.Session() as session:
#     for link in urls:
#         run_tasks(link, session)
# print(time.time()-start)
# ---------------------end block 3------------------------

# ПРИМЕР 3
# *************
# import aiohttp
# import asyncio
# import requests
# from bs4 import BeautifulSoup

# category_lst = []
# pagen_lst = []
# domain = 'https://parsinger.ru/html/'


# def get_soup(url):
#     resp = requests.get(url=url)
#     return BeautifulSoup(resp.text, 'lxml')


# def get_urls_categories(soup):
#     all_link = soup.find('div', class_='nav_menu').find_all('a')

#     for cat in all_link:
#         category_lst.append(domain + cat['href'])


# def get_urls_pages(category_lst):
#     for cat in category_lst:
#         resp = requests.get(url=cat)
#         soup = BeautifulSoup(resp.text, 'lxml')
#         for pagen in soup.find('div', class_='pagen').find_all('a'):
#             pagen_lst.append(domain + pagen['href'])


# async def get_data(session, link):
#     async with session.get(url=link) as response:
#         resp = await response.text()
#         soup = BeautifulSoup(resp, 'lxml')
#         item_card = [x['href'] for x in soup.find_all('a', class_='name_item')]
#         for x in item_card:
#             url2 = domain + x
#             async with session.get(url=url2) as response2:
#                 resp2 = await response2.text()
#                 soup2 = BeautifulSoup(resp2, 'lxml')
#                 article = soup2.find('p', class_='article').text
#                 name = soup2.find('p', id='p_header').text
#                 price = soup2.find('span', id='price').text
#                 print(url2, price, article, name)


# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for link in pagen_lst:
#             task = asyncio.create_task(get_data(session, link))
#             tasks.append(task)
#         await asyncio.gather(*tasks)


# url = 'https://parsinger.ru/html/index1_page_1.html'
# soup = get_soup(url)
# get_urls_categories(soup)
# get_urls_pages(category_lst)

# asyncio.run(main())

# ПРИМЕР 3 (ООП)
# *************

# import aiohttp
# import asyncio
# import requests
# from bs4 import BeautifulSoup

# class Parser:
#     def __init__(self, domain) -> None:
#         self._domain = domain
#         self._category_lst, self._pagen_lst = [], []

#     @staticmethod
#     def get_soup(url):
#         resp = requests.get(url=url)
#         return BeautifulSoup(resp.text, 'lxml')

#     def get_urls_categories(self, soup):
#         all_link = soup.find('div', class_='nav_menu').find_all('a')
#         for cat in all_link:
#             self._category_lst.append(self._domain + cat['href'])

#     def get_urls_pages(self):
#         for cat in self._category_lst:
#             soup = self.get_soup(cat)
#             for pagen in soup.find('div', class_='pagen').find_all('a'):
#                 self._pagen_lst.append(self._domain + pagen['href'])

#     async def get_data(self, session, link):
#         async with session.get(url=link) as response:
#             resp = await response.text()
#             soup = BeautifulSoup(resp, 'lxml')
#             item_card = [x['href'] for x in soup.find_all('a', class_='name_item')]
#             for x in item_card:
#                 url2 = self._domain + x
#                 async with session.get(url=url2) as response2:
#                     resp2 = await response2.text()
#                     soup2 = BeautifulSoup(resp2, 'lxml')
#                     article = soup2.find('p', class_='article').text
#                     name = soup2.find('p', id='p_header').text
#                     price = soup2.find('span', id='price').text
#                     print(url2, price, article, name)

#     async def main(self):
#         async with aiohttp.ClientSession() as session:
#             tasks = []
#             for link in self._pagen_lst:
#                 task = asyncio.create_task(self.get_data(session, link))
#                 tasks.append(task)

#             await asyncio.gather(*tasks)
    
#     def __call__(self, url, *args, **kwargs):
#         soup = self.get_soup(url)
#         self.get_urls_categories(soup)
#         self.get_urls_pages()
#         asyncio.run(self.main())

# if __name__ == '__main__':
#     parse_site = Parser(domain='https://parsinger.ru/html/')
#     parse_site('https://parsinger.ru/html/index1_page_1.html')

# import time
# import asyncio
# import aiohttp
# from aiohttp_retry import RetryClient, ExponentialRetry

# # Последние 2 ссылки — 404-е, добавлены в демонстрационных целях
# links = ['https://parsinger.ru/html/watch/1/1_1.html',
#          'https://parsinger.ru/html/watch/1/1_2.html',
#          'https://parsinger.ru/html/watch/1/1_3.html',
#          'https://parsinger.ru/html/watch/8/1_3.html',
#          'https://parsinger.ru/html/watch/8/2_3.html']


# # Корутина для вывода сообщения вида link:response.status
# async def get_data(retry_client, link):
#     async with retry_client.get(link) as response:
#         print(f'{link}:{response.status}')


# # Базовая корутина
# async def main():
#     async with aiohttp.ClientSession() as client_session:
#         # statuses=[404] выбран для демонстрации, на практике
#         # повторное обращение к несуществующей странице скорее всего бессмысленно
#         retry_options = ExponentialRetry(attempts=4, statuses={404})
#         async with RetryClient(
#                 raise_for_status=False, retry_options=retry_options,
#                 client_session=client_session) as retry_client:
#             await asyncio.gather(*[get_data(retry_client, link) for link in links])


# if __name__ == '__main__':
#     start = time.time()
#     asyncio.run(main())
#     print(f'время:{time.time() - start}')

# 6.8.1 Приготовление асинхронного супа. Задача 1

# ***** СИНХР

# import requests
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# from time import time

# def get_soup(url):
#     resp = requests.get(url)
#     resp.encoding = 'utf-8'
#     return BeautifulSoup(resp.text, 'lxml')

# def get_categories(soup):
#     links = soup.find('div', class_='nav_menu').select('a')
#     for link in links:
#         categories.append(domain + link['href'])

# def get_pages(cat_lst):
#     for cat in cat_lst:
#         soup = get_soup(cat)
#         links = soup.find('div', class_='pagen').select('a') # type: ignore
#         for link in links:
#             pages.append(domain + link['href']) # type: ignore

# def get_data(session, link):
#     with session.get(link) as responce:
#         soup = BeautifulSoup(responce.text, 'lxml')
#         cards = [domain + card['href'] for card in soup.select('a.name_item')] # type: ignore
#         discount_sum = 0
#         for card in cards:
#             with session.get(card) as response2:
#                 soup = BeautifulSoup(response2.text, 'lxml')
#                 qt = int(soup.find('span', id='in_stock').text.split()[-1]) # type: ignore
#                 old_price = int(soup.find('span', id='old_price').text.split()[0]) # type: ignore
#                 price = int(soup.find('span', id='price').text.split()[0]) # type: ignore
#                 discount = (old_price - price) * qt
#                 discount_sum += discount
#     return discount_sum

# def main():
#     ua = UserAgent()
#     headers = {'user-agent': ua.random}
#     with requests.Session() as session:
#         session.headers.update(headers)
#         discounts = [get_data(session, link) for link in pages]
#         result = sum(discounts)
#     print('Общий размер скидки для всех товаров:', result)

# if __name__ == '__main__':
#     start_time = time()
#     categories = []
#     pages = []
#     domain = 'https://parsinger.ru/html/'
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     soup = get_soup(url)
#     get_categories(soup)
#     get_pages(categories)
#     main()
#     print('Время выполнения:', time() - start_time)


# ***** АСИНХР 1

# import asyncio
# import aiohttp
# import requests
# from bs4 import BeautifulSoup
# from aiohttp_retry import RetryClient, ExponentialRetry
# from fake_useragent import UserAgent
# from time import time

# def get_soup(url): # type: ignore
#     resp = requests.get(url)
#     resp.encoding = 'utf-8'
#     return BeautifulSoup(resp.text, 'lxml')

# def get_categories(soup):
#     links = soup.find('div', class_='nav_menu').select('a')
#     for link in links:
#         categories.append(domain + link['href'])

# def get_pages(cat_lst):
#     for cat in cat_lst:
#         soup = get_soup(cat)
#         links = soup.find('div', class_='pagen').select('a') # type: ignore
#         for link in links:
#             pages.append(domain + link['href']) # type: ignore

# async def get_data(session, link):
#     retry_opt = ExponentialRetry(attempts=5)
#     retry_client = RetryClient(raise_for_status=False, retry_options=retry_opt, client_session=session, start_timeout=0.5)
#     async with retry_client.get(link) as responce:
#         soup = BeautifulSoup(await responce.text(), 'lxml')
#         cards = [domain + card['href'] for card in soup.select('a.name_item')] # type: ignore
#         discount_sum = 0
#         for card in cards:
#             async with retry_client.get(card) as response2:
#                 soup = BeautifulSoup(await response2.text(), 'lxml')
#                 qt = int(soup.find('span', id='in_stock').text.split()[-1]) # type: ignore
#                 old_price = int(soup.find('span', id='old_price').text.split()[0]) # type: ignore
#                 price = int(soup.find('span', id='price').text.split()[0]) # type: ignore
#                 discount = (old_price - price) * qt
#                 discount_sum += discount
#     return discount_sum

# async def main():
#     ua = UserAgent()
#     headers = {'user-agent': ua.random}
#     async with aiohttp.ClientSession(headers=headers) as session:
#         tasks = [asyncio.create_task(get_data(session, link)) for link in pages]
#         result = sum(await asyncio.gather(*tasks))
#     print('Общий размер скидки для всех товаров:', result)

# if __name__ == '__main__':
#     start_time = time()
#     categories = []
#     pages = []
#     domain = 'https://parsinger.ru/html/'
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     soup = get_soup(url)
#     get_categories(soup)
#     get_pages(categories)

#     asyncio.run(main())
#     print('Время выполнения:', time() - start_time)

# ***** АСИНХР 2

# import asyncio
# import aiohttp
# import requests
# from bs4 import BeautifulSoup
# from aiohttp_retry import RetryClient, ExponentialRetry
# from fake_useragent import UserAgent
# from time import time

# def get_categories(link):
#     resp = requests.get(link)
#     resp.encoding = 'utf-8'
#     soup = BeautifulSoup(resp.text, 'lxml')
#     categories = [domain + cat['href'] for cat in soup.find('div', class_='nav_menu').select('a')]
#     return categories

# async def get_soup(session, url):
#     async with session.get(url) as response:
#         resp = await response.text()
#         return BeautifulSoup(resp, 'lxml')

# async def get_pages_links(session, url):
#     soup = await get_soup(session, url)
#     pages = [domain + page['href'] for page in soup.find('div', class_='pagen').select('a')]
#     for page in pages:
#         pages_links.append(page)
#     return pages

# async def get_data(session, url):
#     soup = await get_soup(session, url)
#     cards = [domain + card['href'] for card in soup.select('a.name_item')]
#     discount_sum = 0
#     for card in cards:
#         soup = await get_soup(session, card)
#         qt = int(soup.find('span', id='in_stock').text.split()[-1])
#         old_price = int(soup.find('span', id='old_price').text.split()[0])
#         price = int(soup.find('span', id='price').text.split()[0])
#         discount = (old_price - price) * qt
#         discount_sum += discount
#     return discount_sum

# async def main():
#     ua = UserAgent()
#     headers = {'user-agent': ua.random}
#     async with aiohttp.ClientSession(headers=headers) as session:
#         retry_opt = ExponentialRetry(attempts=5)
#         rc_session = RetryClient(raise_for_status=False, retry_options=retry_opt, client_session=session, start_timeout=0.5)
#         tasks1 = [asyncio.create_task(get_pages_links(rc_session, cat)) for cat in categories_links]
#         sss = await asyncio.gather(*tasks1)
#         tasks2 = [asyncio.create_task(get_data(rc_session, page)) for page in pages_links]
#         result = sum(await asyncio.gather(*tasks2))
#         print('Общий размер скидки для всех товаров:', result)

# if __name__ == '__main__':
#     start_time = time()
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     domain = 'https://parsinger.ru/html/'
#     pages_links = []
#     categories_links = get_categories(url)
#     asyncio.run(main())
#     print('Время выполнения:', time() - start_time)

# ***** АСИНХР 3

# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
# from aiohttp_retry import RetryClient, ExponentialRetry
# from fake_useragent import UserAgent
# from time import time

# async def get_soup(session, url):
#     async with session.get(url) as response:
#         resp = await response.text()
#         return BeautifulSoup(resp, 'lxml')

# async def get_data(session, link):
#     soup = await get_soup(session, link)
#     qt = int(soup.find('span', id='in_stock').text.split()[-1])
#     old_price = int(soup.find('span', id='old_price').text.split()[0])
#     price = int(soup.find('span', id='price').text.split()[0])
#     discount = (old_price - price) * qt
#     return discount

# async def task_generator(session, url):
#     domain = 'https://parsinger.ru/html/'
#     soup = await get_soup(session, url)
#     categories = [domain + cat['href'] for cat in soup.find('div', class_='nav_menu').select('a')]
#     for cat in categories:
#         soup = await get_soup(session, cat)
#         pages = [domain + page['href'] for page in soup.find('div', class_='pagen').select('a')]
#         for page in pages:
#             soup = await get_soup(session, page)
#             cards = [domain + card['href'] for card in soup.select('a.name_item')]
#             for card in cards:
#                 yield asyncio.create_task(get_data(session, card))

# async def main():
#     ua = UserAgent()
#     headers = {'user-agent': ua.random}
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     async with aiohttp.ClientSession(headers=headers) as session:
#         retry_opt = ExponentialRetry(attempts=5)
#         rc_session = RetryClient(raise_for_status=False, retry_options=retry_opt, client_session=session, start_timeout=0.5)
#         tasks = [task async for task in task_generator(rc_session, url)]
#         result = sum(await asyncio.gather(*tasks))
#     print('Общий размер скидки для всех товаров:', result)

# if __name__ == '__main__':
#     start_time = time()
#     asyncio.run(main())
#     print('Время выполнения:', time() - start_time)

    # ***** АСИНХР 4

# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
# from aiohttp_retry import RetryClient, ExponentialRetry
# from fake_useragent import UserAgent
# from time import time

# async def get_soup(session, url):
#     async with session.get(url) as response:
#         resp = await response.text()
#         return BeautifulSoup(resp, 'lxml')

# async def get_data(session, link):
#     soup = await get_soup(session, link)
#     cards = [domain + card['href'] for card in soup.select('a.name_item')]
#     discount_sum = 0
#     for card in cards:
#         soup = await get_soup(session, card)
#         qt = int(soup.find('span', id='in_stock').text.split()[-1])
#         old_price = int(soup.find('span', id='old_price').text.split()[0])
#         price = int(soup.find('span', id='price').text.split()[0])
#         discount = (old_price - price) * qt
#         discount_sum += discount
#     return discount_sum

# async def task_generator(session, url):
#     soup = await get_soup(session, url)
#     categories = [domain + cat['href'] for cat in soup.find('div', class_='nav_menu').select('a')]
#     for cat in categories:
#         soup = await get_soup(session, cat)
#         pages = [domain + page['href'] for page in soup.find('div', class_='pagen').select('a')]
#         for page in pages:
#             yield asyncio.create_task(get_data(session, page))

# async def main():
#     ua = UserAgent()
#     headers = {'user-agent': ua.random}
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#     async with aiohttp.ClientSession(headers=headers) as session:
#         retry_opt = ExponentialRetry(attempts=5)
#         rc_session = RetryClient(raise_for_status=False, retry_options=retry_opt, client_session=session, start_timeout=0.5)
#         tasks = [task async for task in task_generator(rc_session, url)]
#         result = sum(await asyncio.gather(*tasks))
#     print('Общий размер скидки для всех товаров:', result)

# if __name__ == '__main__':
#     start_time = time()
#     domain = 'https://parsinger.ru/html/'
#     asyncio.run(main())
#     print('Время выполнения:', time() - start_time)

# 6.8 Приготовление асинхронного супа. Задача 2

# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup

# async def get_response(session, link):
#     async with session.get(link) as response:
#         if response.ok:
#             resp = await response.text()
#             soup = BeautifulSoup(resp, 'lxml')
#             return int(soup.find('p', class_='text').text)
#         else:
#             return 0

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             resp = await response.text()
#             soup = BeautifulSoup(resp, 'lxml')
#             all_links = [domain + link['href'] for link in soup.select('a')]
#             tasks = [asyncio.create_task(get_response(session, link)) for link in all_links]
#             result = sum(await asyncio.gather(*tasks))
#     print(result)

# domain = 'https://parsinger.ru/asyncio/create_soup/1/'
# url = 'https://parsinger.ru/asyncio/create_soup/1/index.html'
# asyncio.run(main())

# 6.9 aiofiles Скачивание картинок в асинхронном стиле
# *****************************************************************

# ПРИМЕР 1. Асинхронный (результат = 10.975 сек)

# import time
# import aiofiles
# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
# import os


# async def write_file(session, url, name_img):
#     async with aiofiles.open(f'Stepik_Parsing/images/{name_img}', mode='wb') as f:
#         async with session.get(url) as response:
#             async for x in response.content.iter_chunked(1024):
#                 await f.write(x)
#         print(f'Изображение сохранено {name_img}')


# async def main():
#     url = 'https://parsinger.ru/asyncio/aiofile/1/index.html'
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             soup = BeautifulSoup(await response.text(), 'lxml')
#             img_url = [f'https://parsinger.ru/asyncio/aiofile/1/{x["src"]}' for x in soup.find_all('img')]
#             tasks = []
#             for link in img_url:
#                 name_img = link.split('/')[7]
#                 task = asyncio.create_task(write_file(session, link, name_img))
#                 tasks.append(task)
#             await asyncio.gather(*tasks)


# start = time.perf_counter()
# asyncio.run(main())
# print(f'Cохранено изображений {len(os.listdir("Stepik_Parsing/images/"))} за {round(time.perf_counter() - start, 3)} сек')

# ПРИМЕР 2. Синхронный (результат = 136.590 сек)

# import time
# import requests
# from bs4 import BeautifulSoup


# def main(url):
#     img_url = []
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     images_link = [f'https://parsinger.ru/asyncio/aiofile/1/{x["src"]}' for x in soup.find_all('img')]
#     img_url.extend(images_link)

#     for x in images_link:
#         response2 = requests.get(x, stream=True).content
#         name_img = x.split('/')[7]
#         read_file = open(f'Stepik_Parsing/images_sync/{name_img}.jpg', 'wb')
#         read_file.write(response2)


# start = time.perf_counter()
# url = 'https://parsinger.ru/asyncio/aiofile/1/index.html'
# main(url)
# print(time.perf_counter() - start)

# ******************************************************
# 6.9.1 aiofiles Глубина парсинга уровень 1
# ******************************************************
import time
import aiofiles
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os

def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size

async def get_img_links(session, url):
    async with session.get(url) as response:
        soup = BeautifulSoup(await response.text(), 'lxml')
        img_links = [link['src'] for link in soup.find_all('img')]
        all_links.update(img_links)

async def get_img(session, url):
    img_name = os.path.basename(url)
    async with aiofiles.open(img_path + img_name, mode='wb') as file:
        async with session.get(url) as response:
            async for x in response.content.iter_chanked(1024):
                await file.write(x)

async def main():
    domain = 'https://parsinger.ru/asyncio/aiofile/2/'
    url = 'https://parsinger.ru/asyncio/aiofile/2/index.html'
    async with aiohttp.ClientSession() as session:
        response = session.get(url)
        soup = BeautifulSoup(await response.text(), 'lxml')
        page_links = [domain + page['href'] for page in soup.select('a')]
        tasks1 = [asyncio.create_task(get_img_links(session, link)) for link in page_links]
        await asyncio.gather(*tasks1)
        tasks2 = [asyncio.create_task(get_img(session, link)) for link in all_links]
        await asyncio.gather(*tasks2)

img_path = 'Stepik_Parsing/images'
all_links = set()
start = time.perf_counter()
os.makedirs(img_path, exist_ok=True)
asyncio.run(main())
size = get_folder_size(img_path)
print('Размер скачанных изображений:', size)
print('Время скачиывния:', time.perf_counter() - start, 'сек.')
