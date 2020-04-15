import requests
from bs4 import BeautifulSoup
import sys

def star(text):
  return str(
      len(soup.find(text='\n' + text + ' ').
          parent.
          next_sibling.
          find_all(class_="fa fa-star fa-star checked"))) + '\t'

def value(text):
  return str(
      list(soup.find(text='\n' + text + ' ').
           parent.
           next_sibling.
           find('span').
           children)[0]) + '\t'

print('link\tapartment friendly\tbarking\tchild friendly\tshedding level\tsize\tstinkiness\tbiting potential\toffice friendly\tstranger friendly\tdog friendly\tcat friendly\tadaptability\tfighting dog\tpet friendly\tgood for first time owners\thealth issues\tenergy level\texercise need\tdrooling tendency')
soup = None
with open('list.tsv') as file:
  for line in file.readlines():
    link = line.strip()
    page = requests.get('https://dogell.com' + link)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(link + '\t' +
          star('Apartment Friendly') +
          star('Barking') +
          star('Child Friendly') +
          star('Shedding Level') +
          value('Size') +
          value('Stinkiness') +
          value('Biting Potential') +
          value('Office Friendly') +
          star('Stranger Friendly') +
          star('Dog Friendly') +
          star('Cat Friendly') +
          star('Adaptability') +
          value('Fighting Dog') +
          star('Pet Friendly') +
          value('Good For First Time Owners') +
          star('Health Issues') +
          star('Energy Level') +
          star('Exercise Need') +
          star('Drooling tendency'))
    sys.stdout.flush()
