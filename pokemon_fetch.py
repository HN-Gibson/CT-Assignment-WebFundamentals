import requests
import json

def get_pokemon_data (pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    json_data = response.text

    data = json.loads(json_data)

    name = data['name']
    print(f'Name: {name}')

    for ability in data['abilities']:
        print (f'Ability: {ability['ability']['name']}')

    return

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for name in pokemon_list:    
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        json_data = response.text

        data = json.loads(json_data)

        pokemon_weight = data['weight']
        total_weight += pokemon_weight
    return total_weight/len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

for name in pokemon_names:
    get_pokemon_data(name)

average_weight = calculate_average_weight(pokemon_names)

print (f"Average Weight: {average_weight}")

