## SCRAPING MULTIPLE LINKS WITHIN THE SAME PAGE

"""
from bs4 import BeautifulSoup
import requests
import lxml


website = 'https://subslikescript.com/movies'

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())
box = soup.find('article',class_='main-article')  # altçizginin sebebi pythondaki classlarla karısmaması için

links = []
for link in box.find_all('a',href = True):   # looped for a list
    links.append(link['href'])

print(links)

## we generate .txt file for each with reduced codes
for link in links:
    website = f'https://subslikescript.com/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')  # altçizginin sebebi pythondaki classlarla karısmaması için

    title = box.find('h1').get_text()
    transcript = box.find('div',class_='full-script').get_text(strip=True,separator=' ') # cekilen datada bosluklar yüzünden satırlarca devam ediyordu. data messy olmasın diye tek satıra boslukları düzelterek aldık. içine o yüzden 2 parametre girdik

    with open(f'{title}.txt','w',encoding='utf-8') as file:  # cekilen transcript bilgisini txt'ye export ettik. formatlayarak variable atadık ismine. title + '.txt' de yapılabilirdi.
        file.write(transcript)
"""


## SCRAPING MULTIPLE LINKS WITHIN THE MULTIPLE PAGES

from bs4 import BeautifulSoup
import requests
import lxml


website = 'https://subslikescript.com/movies_letter-A'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())

# pagination
pagination = soup.find('ul',class_='pagination')
pages = pagination.find_all('li',class_='page-item')
last_page = pages[-2].text

links = []  # we replaced that right here: outside the loop. bcs if it would be in loop it will return empty for every iteration
for page in range(1,int(last_page)+1)[:3]:      # totally 147 pages r too long, we limitation with first 3 pages
    # https://subslikescript.com/movies_letter-A?page=1
    website = 'https://subslikescript.com/movies_letter-A?page='+str(page)    # website = f'https://subslikescript.com/movies_letter-A?page={page}' de olurdu.
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')


    box = soup.find('article',class_='main-article')  # altçizginin sebebi pythondaki classlarla karısmaması için

    for link in box.find_all('a',href = True):   # looped for a list
        links.append(link['href'])

    print(links)

    ## we generate .txt file for each with reduced codes
    for link in links:

        try:
            print(link)
            website = f'https://subslikescript.com/{link}'
            result = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('article', class_='main-article')  # altçizginin sebebi pythondaki classlarla karısmaması için

            title = box.find('h1').get_text()
            transcript = box.find('div',class_='full-script').get_text(strip=True,separator=' ') # cekilen datada bosluklar yüzünden satırlarca devam ediyordu. data messy olmasın diye tek satıra boslukları düzelterek aldık. içine o yüzden 2 parametre girdik

        except:
            print("---------Link is not working---------")
            print(link)

        with open('last_one.txt','w',encoding='utf-8') as file:  # cekilen transcript bilgisini txt'ye export ettik. formatlayarak variable atadık ismine. title + '.txt' de yapılabilirdi.
            file.write(transcript)



























