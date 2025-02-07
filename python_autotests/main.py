import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6c37f41bd96cc93b2d3f538aea44224a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Rocky",
    "photo_id": 16
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''pokemon_id = response_create.json()['id']
print (pokemon_id)'''


body_change = {
    "pokemon_id": "278392",
    "name": "Balboa",
    "photo_id": 16
}

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''


body_catch = {
    "pokemon_id": "278392"
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)