from bs4 import BeautifulSoup
import requests
import os

os.makedirs('./img/', exist_ok=True)

URL = "http://oursogo.com/forum.php?mod=viewthread&tid=2516439&extra=page=1"

html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_ig = soup.find_all('ignore_js_op')

for ig in img_ig:
    imgs = ig.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
