import requests
from .scratch import transfermarkt_url

def html_retrieve():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'https://www.transfermarkt.com/',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    html_code = requests.get(url = transfermarkt_url, headers=headers).text
    with open("sample_data.html", "w") as f:
         f.write(html_code)