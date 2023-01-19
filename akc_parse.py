from bs4 import BeautifulSoup
from os import listdir
from pathlib import Path
import json

metrics = ['adaptability_level', 'affectionate_with_family', 'barking_level', 'coat_grooming_frequency', 'good_with_young_children', 'drooling_level', 'energy_level', 'good_with_other_dogs', 'mental_stimulation_needs', 'openness_to_strangers', 'playfulness_level', 'shedding_level', 'trainability_level', 'watchdogprotective_nature']

print('breed', end='')
for metric in metrics:
    print(',' + metric, end='')
print()

breeds = listdir('akc')
for breed in breeds:
    print(breed, end='')
    content = Path('akc/' + breed).read_text()
    soup = BeautifulSoup(content, 'html.parser')
    tag = soup.find('div', {'data-js-component': 'breedPage'})
    js = json.loads(tag['data-js-props'])
    # print(js['settings']['breed_data']['traits'].keys())
    traits = js['settings']['breed_data']['traits'][breed]['traits']
    for metric in metrics:
        print(',' + str(traits[metric]['score']), end='')
    print()
