import requests
import pandas as pd
import json

cookie = "ARRAffinity=9b8797b8dd2a0cb8ff15d74c3dc393b1083a16ce953e8cf29e4026f776fd7cf9; _ga=GA1.2.1645136139.1615888320; _gid=GA1.2.1422364552.1615888320"

def generate_header(cookie):
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://172.18.12.4',
        'Connection': 'keep-alive',
        'Referer': 'http://emrani.net/hafez?action=list',
        'Cookie': cookie
    }


response = requests.get("http://emrani.net/hafez/api/hafez/list?start=0&count=500", headers=generate_header(cookie))

df = pd.json_normalize(json.loads(response.text))
df = df[['id', 'poem']]
df.to_csv('poem.csv')