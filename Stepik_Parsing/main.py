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

