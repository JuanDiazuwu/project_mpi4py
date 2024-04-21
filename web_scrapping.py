import requests
from mpi4py import MPI
from bs4 import BeautifulSoup
from random import randint

URL = "https://pokeapi.co/api/v2/pokemon/"

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def scrape_pokemon_data(aleatori_number):
    update_url = URL + str(aleatori_number)
    response = requests.get(update_url).json()
    pokemon_name = response.get('forms')[0].get('name')
    return pokemon_name

def main():
    random_pokemon_number = randint(1, 151)
    random_pokemon_number = comm.scatter([random_pokemon_number]*size, root=0)
    pokemon_data = scrape_pokemon_data(random_pokemon_number)
    all_pokemon_data = comm.gather(pokemon_data, root=0)

    if rank == 0:
        for data in all_pokemon_data:
            print(data)

if __name__ == '__main__':
    main()
