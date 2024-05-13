import requests
import pytest

Url = 'https://api.pokemonbattle.me/'
Version = 'v2'
Token = '498c7f1be585ec7432a20f4441a2349f'
Header = {'Content-Type':'application/json', 'trainer_token':Token}
Trainer_id = 4002

def test_pokemons_status_code():
    responce = requests.get(url = f'{Url}{Version}/pokemons', params = {'trainer_id' : Trainer_id})
    assert responce.status_code == 200

def test_part_of_responce():
    responce_get = requests.get(url = f'{Url}{Version}/pokemons', params = {'trainer_id' : Trainer_id})
    assert responce_get.json()['data'][0]['name'] == 'Лини'

def test_trainers_status_code():
    responce = requests.get(url = f'{Url}{Version}/trainers', params = {'city' : '%','level' : '3,4','name' : '5','sort' : 'asc_price'} )
    assert responce.status_code == 200

def test_trainers_responce():
    responce = requests.get(url = f'{Url}{Version}/trainers', params = {'trainer_id' : Trainer_id} )
    assert responce.json()['data'][0]['trainer_name'] == 'Арлекино'