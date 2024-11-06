import requests

def fetch_planet_data():
    planets = []

    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    data = response.json()['bodies']

    #process each planet info
    for planet in data:
        if planet['isPlanet']:
            name = planet.get('englishName')
            mass = planet.get('mass').get('massValue')
            orbit_period = planet.get('sideralOrbit')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
            planets.append({'name':name, 'mass':mass, 'orbital_period': orbit_period})
    return planets

def find_longest_orbital_period(planets):
    longest_orbit = max(planets, key=lambda x:x['orbital_period'])
    return longest_orbit

planets = fetch_planet_data()
longest_orbit = find_longest_orbital_period(planets)
print(f"The planet with the longest orbital period is {longest_orbit['name']} with a orbital period of {longest_orbit['orbital_period']} days.")