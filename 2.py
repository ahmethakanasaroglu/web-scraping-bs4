## SCRAPE A SINGLE PAGE AND EXPORTING DATA TO .TXT

from bs4 import BeautifulSoup   # scraper type   # can pull data out of html and xml
import requests    # send requests to a website to google
import lxml     # parser   # bcs bs4 doesnt have own parser

"""
website = 'https://subslikescript.com/movie/Titanic-120338'

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())
"""



website = 'https://subslikescript.com/movie/Titanic-120338'

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())

box = soup.find('article',class_='main-article')  # altçizginin sebebi pythondaki classlarla karısmaması için

title = box.find('h1').get_text()
print(title)

transcript = box.find('div',class_='full-script').get_text(strip=True,separator=' ') # cekilen datada bosluklar yüzünden satırlarca devam ediyordu. data messy olmasın diye tek satıra boslukları düzelterek aldık. içine o yüzden 2 parametre girdik
print(transcript)

with open(f'{title}.txt','w') as file:  # cekilen transcript bilgisini txt'ye export ettik. formatlayarak variable atadık ismine. title + '.txt' de yapılabilirdi.
    file.write(transcript)


import chardet  # encoding hatalarını otomatik bulmaya yarar


"""
with open('Titanic (1997) - full transcript.txt', 'rb') as f:
    result = chardet.detect(f.read())
    print(result)
    
    encoding='result' olarak da with openin sonuna eklenebilir. metin içinde encode hatası almamak için  
"""