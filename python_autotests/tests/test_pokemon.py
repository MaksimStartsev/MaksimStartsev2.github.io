import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6c37f41bd96cc93b2d3f538aea44224a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = "17455"

def test_status_code():
    response = requests.get(url= f'{URL}/trainers',headers=HEADER)
    assert response.status_code == 200

def test_name_trainers():
    response_get = requests.get(url= f'{URL}/trainers',headers=HEADER , params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Tre'

 


    