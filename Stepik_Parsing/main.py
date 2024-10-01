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

import asyncio

async def two():
    await asyncio.sleep(1)
    print('world')


async def one():
    print('hello')
    task2 = asyncio.create_task(two())
    await asyncio.sleep(5)
    # await task2
    print('end!')


asyncio.run(one())