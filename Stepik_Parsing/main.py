# import requests

# url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
# resp = requests.get(url, stream=True)
# with open('Stepik_Parsing/video.mp4', 'wb') as ouf:
#     for bit in resp.iter_content(chunk_size=1000000):
#         ouf.write(bit)

import requests
import time

total = 0
start = time.time()
with requests.Session() as rs:
    for i in range(200):
        response = rs.head(f'https://parsinger.ru/3.3/2/{i+1}.html')
        total += response.status_code
stop = time.time()
t = stop - start
print(f'Сумма статусов = {total}\nВремя выполнения = {t}')