# import requests

# url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
# resp = requests.get(url, stream=True)
# with open('Stepik_Parsing/video.mp4', 'wb') as ouf:
#     for bit in resp.iter_content(chunk_size=1000000):
#         ouf.write(bit)

# *** 3.3.3 Суммирование HTTP статус-кодов
# import requests
# import time

# total = 0
# start = time.time()
# with requests.Session() as rs:
#     for i in range(200):
#         response = rs.head(f'https://parsinger.ru/3.3/2/{i+1}.html')
#         total += response.status_code
# stop = time.time()
# t = stop - start
# print(f'Сумма статусов = {total}\nВремя выполнения = {t}')

# *** 3.3.4 Поиск рабочей ссылки и секретного кода на ней
# import requests

# with requests.Session() as rs:
#     for i in range(200):
#         response = rs.get(f'https://parsinger.ru/3.3/1/{i+1}.html')
#         if response.status_code == 200:
#             print(response.text)
#             break

# *** 3.3.5 Поиск самого большого изображения по размеру файла
# import requests

# name_img= ['1663231240183817644.jpg',
#  '1663231245165469794.jpg',
#  '1663231252148267596.jpg',
#  '16632460271311817.jpg',
#  '1663260860165832550.jpg',
#  '1663260862112644405.jpg',
#  '1663260864114071369.jpg',
#  '1663260869127473152.jpg',
#  '1663260874115452216.jpg',
#  '1663260877136512181.jpg',
#  '1663260878140464277.jpg',
#  '1663267600193799276.jpg',
#  '1663267613117130673.jpg',
#  '1663267619197170483.jpg',
#  '1663267626154597739.jpg',
#  '1663267648135114690.jpg',
#  '166326765416196421.jpg',
#  '1663267662118079649.jpg',
#  '1663267668165066872.jpg',
#  '1663267878176341940.jpg',
#  '166326990115068678.jpg',
#  '1663269922185881885.jpg',
#  '1663269927127433209.jpg',
#  '1663269942143420441.jpg',
#  '1663269946174943071.jpg',
#  '1663269964195277579.jpg',
#  '1663269970148058649.jpg',
#  '1663269974197750992.jpg',
#  '166326997917397750.jpg',
#  '1663270039138442380.jpg',
#  '1663388012194470737.jpg',
#  '166342371029995280.jpg',
#  '1663423712288242036.jpg',
#  '1663423715255612089.jpg',
#  '1663423720221155166.jpg',
#  '1663423722211139858.jpg',
#  '1663423724211218483.jpg',
#  '1663423728215479371.jpg',
#  '1663423729298828299.jpg',
#  '1663423732225964403.jpg',
#  '1663424198111663025.jpg',
#  '1663424199157537861.jpg',
#  '1663424200184778832.jpg',
#  '166342420214123494.jpg',
#  '166342420317539591.jpg',
#  '1663424204161674559.jpg',
#  '1663424206188873432.jpg',
#  '166342420813193185.jpg',
#  '1663424209187179962.jpg',
#  '1663424212162573102.jpg']
# def jpg_length(name):
#     url = 'https://parsinger.ru/3.3/3/img/'
#     resp = requests.get(url+name)
#     return int(resp.headers.get('Content-Length'))

# max_img = max(name_img, key=jpg_length)
# print(f'''URL изображения с наибольшим размером: 
# https://parsinger.ru/3.3/3/img/{max_img}
# Имя файла изображения: {max_img.rstrip('.jpg')}''')

# *** 3.3.6 Первая и последняя доступная страница

# import requests

# pages = []
# for i in range(1, 101):
#     url = f'https://parsinger.ru/3.3/4/{i}.html'
#     resp = requests.get(url)
#     if resp.status_code == 200:
#         pages.append(i)
# print(f"Первая доступная страница: {pages[0]}.html")
# print(f"Последняя доступная страница: {pages[-1]}.html")

# import requests

# response = requests.get(url='http://httpbin.org/image/jpeg')
# with open('image.jpeg', 'wb') as file:
#     file.write(response.content)

# *** 3.4.3 Получение и вывод HTML-кода веб-страницы

# import requests

# url = 'https://parsinger.ru/3.4/2/index.html'
# resp = requests.get(url)
# resp.encoding = 'utf-8'
# print(resp.text)

# *** 3.4.4 Поиск секретного кода на картинках
# import requests

# with requests.Session() as rs:
#     for i in range(1, 161):
#         url = f'https://parsinger.ru/img_download/img/ready/{i}.png'
#         resp = rs.get(url)
#         if resp.status_code == 200:
#             with open(f'Stepik_Parsing/imgs/{i}.png', 'wb') as ouf:
#                 ouf.write(resp.content)

# *** 3.4.5 Получение и анализ данных о погоде
# import requests

# url = 'https://parsinger.ru/3.4/1/json_weather.json'
# resp = requests.get(url)
# if resp.status_code == 200:
#     data = resp.json()
#     min_tmp_date = min(data, key=lambda x: int(x['Температура воздуха'].strip('°C')))['Дата']
#     print(min_tmp_date) 
# else:
#     print('Bad connect')

# *** 3.4.6 Анализ древовидной переписки из JSON API
# import requests

# def dc_list(lst):
#     if not lst:
#         return []
#     tmp = lst[:]
#     for dc in lst:
#         tmp += dc_list(dc['comments'])
#     return tmp

# url = 'https://parsinger.ru/3.4/3/dialog.json'
# resp = requests.get(url)
# usernames = {}
# if resp.status_code == 200:
#     data = resp.json()
#     for d in dc_list([data]):
#         usernames[d['username']] = usernames.get(d['username'], 0) + 1
#     sorted_usernames = {k: v for k, v in sorted(usernames.items(), key=lambda x: (-x[1], x[0]))}
#     print(sorted_usernames)
# else:
#     print('Bad connect')

import requests

url = 'http://httpbin.org/opopo/'
resp = requests.get(url)
print(resp.status_code)
print(bool(resp))
print(resp.request)
# Whoa!!!
