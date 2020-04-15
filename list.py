import requests
from bs4 import BeautifulSoup

for i in range(1, 33):
  page = requests.get('https://dogell.com/en/dog-breeds?sort=name&page=' + str(i))
  soup = BeautifulSoup(page.content, 'html.parser')
  results = soup.find_all(class_='button show-details-btn')
  for result in results:
    print(result['href'])
