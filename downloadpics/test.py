from bs4 import BeautifulSoup
import requests

URL = "http://oursogo.com/forum.php?mod=viewthread&tid=2516439&extra=page=1"

html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_ig = soup.find_all('ignore_js_op')
print(img_ig)
