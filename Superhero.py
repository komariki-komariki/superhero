import requests

smart = {}
superheroes = ['Hulk', 'Captain America', 'Thanos']

def search_id (name):
    url_search = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{name}')
    id_number = url_search.json()['results'][0]['id']
    url = requests.get(f'https://superheroapi.com/api/2619421814940190/{id_number}/powerstats')
    smart.setdefault(url.json()['name'], int(url.json()['intelligence']))

def search_hero():
    for superhero in superheroes:
        search_id(superhero)

def most_intelligent():
    search_hero()
    return f'Самый умный - {max(smart, key=smart.get)}'

print(most_intelligent())