from bs4 import BeautifulSoup
import requests
import os

os.makedirs('./img/', exist_ok=True)
x=000
y=1
downloadlist=[1964529,]
#html = requests.get(URL).text
#soup = BeautifulSoup(html, 'lxml')
#img_p = soup.find_all('p')
z=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
for y in z: #total pages
    URL = "http://www.177pic.info/html/2018/03/1925689.html/%s" % y
    print(URL)
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'lxml')
    img_p = soup.find_all('p')
    y=y+1
    for p in img_p:
        imgs = p.find_all('img')
        for img in imgs:
            url = img['src']
            r = requests.get(url, stream=True)
            image_name = "0%s" %x
            #image_name = url.split('/')[-1]
            with open('./img/%s' % image_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)
            print('Saved %s' % image_name)
            x=x+1 
