import requests
import os
from mpi4py import MPI
from random import randint

def scrape_pokemon_data(aleatori_number):
    update_url = URL + str(aleatori_number)
    response = requests.get(update_url).json()
    pokemon_name = response.get('forms')[0].get('name')
    return pokemon_name

def main():
    random_pokemon_number = randint(1, 151)
    pokemon_data = scrape_pokemon_data(random_pokemon_number)
    print(pokemon_data, os.getpid())

if __name__ == '__main__':
    URL = "https://pokeapi.co/api/v2/pokemon/"

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    main()
