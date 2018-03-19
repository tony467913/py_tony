import bs4
import requests
import os
from urllib.request import urlretrieve as urlr

pic_url = "http://oursogo.com/data/attachment/forum/201803/09/182742vb998qio383fiwl5.jpg.thumb.jpg"
url = "http://oursogo.com/forum.php?mod=viewthread&tid=2516439&extra=page=1"

urlr(pic_url, './img/img01.jpg')