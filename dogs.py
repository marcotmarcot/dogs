import requests
from bs4 import BeautifulSoup
import sys

def star(text):
  return str(
      len(soup.find(text='\n' + text + ' ').
          parent.
          next_sibling.
          find_all(class_="fa fa-star fa-star checked")))

def value(text):
  return str(
      list(soup.find(text='\n' + text + ' ').
           parent.
           next_sibling.
           find('span').
           children)[0])

print('link\tapartment friendly\tbarking\tchild friendly\tshedding level\tsize\tstinkiness\tbiting potential')
with open('list.tsv') as file:
  for line in file.readlines():
    link = line.strip()
    page = requests.get('https://dogell.com' + link)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(link + '\t' +
          star('Apartment Friendly') + '\t' +
          star('Barking') + '\t' +
          star('Child Friendly') + '\t' +
          star('Shedding Level') + '\t' +
          value('Size') + '\t' +
          value('Stinkiness') + '\t' +
          value('Biting Potential'))
    sys.stdout.flush()
