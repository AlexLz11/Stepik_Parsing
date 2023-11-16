import requests

def check_ip(ip_port):
    ''' Проверка ip и порта proxy'''
    ip, *port = ip_port.split(':')
    is_ip = len(ip.split('.')) == 4 and all(map(lambda x: x.isdigit() and int(x) < 256, ip.split('.')))
    is_port = len(port) == 1 and port[0].isdigit() and 0 < int(port[0]) < 65536
    return all([is_ip, is_port])

url = 'http://httpbin.org/ip'
proxy_list = 'Stepik_Parsing/proxy_list.txt'
verified_proxy_list = 'Stepik_Parsing/verified_proxy.txt'
vpl = []
with open(proxy_list) as file:
    pl = file.read().split('\n')
for ip in pl:
    if ip in vpl or not check_ip(ip):
        continue
    try:
        proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}'
                }
        resp = requests.get(url, proxies=proxy)
        print(resp.json(), 'Success connection')
        vpl.append(ip)
    except Exception as _ex:
        print(ip, '--Not work')
        continue
if vpl:
    with open(verified_proxy_list, 'w') as file:
        file.write('\n'.join(vpl))
        print(f'Create file {verified_proxy_list}')