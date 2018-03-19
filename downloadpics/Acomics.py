from bs4 import BeautifulSoup
import requests
import os

os.makedirs('./img/', exist_ok=True)

URL = "http://18h.animezilla.com/manga/784/%s"

html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_p = soup.find_all('p')

for p in img_p:
    imgs = p.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)