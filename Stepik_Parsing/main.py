import requests

url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
resp = requests.get(url, stream=True)
with open('Stepik_Parsing/video.mp4', 'wb') as ouf:
    for bit in resp.iter_content(chunk_size=1000000):
        ouf.write(bit)