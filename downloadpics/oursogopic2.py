import bs4
import requests
import os
from urllib.request import urlretrieve as urlr

pic_url = "http://oursogo.com/data/attachment/forum/201803/09/182742vb998qio383fiwl5.jpg.thumb.jpg"
url = "http://oursogo.com/forum.php?mod=viewthread&tid=2516439&extra=page=1"

r = requests.get(pic_url, stream=True)
with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)