import requests

Url = 'https://api.pokemonbattle.me/'
Version = 'v2'
Token = '498c7f1be585ec7432a20f4441a2349f'
Header = {'Content-Type' : 'application/json', 'trainer_token' : Token}

body_create = {
    "name": "Лини",
    "photo": "https://dolnikov.ru/pokemons/albums/005.png"
}

body_change_name = {
    "pokemon_id": "26856",
    "name": "Фремине",
    "photo": "https://dolnikov.ru/pokemons/albums/005.png"
}

body_pokeball = {
    "pokemon_id": "26856"
}

'''responce_create = requests.post(url = f'{Url}{Version}/pokemons', headers = Header, json = body_create)
print(responce_create.text)'''

responce_change_name = requests.put(url = f'{Url}{Version}/pokemons', headers = Header, json = body_change_name)
print(responce_change_name.text)

responce_pokeball = requests.post(url = f'{Url}{Version}/trainers/add_pokeball', headers = Header, json = body_change_name)
print(responce_pokeball.text)
