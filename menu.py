import subprocess
from quick_sort import main_quick_sort

def menu():
    while True:
        print("\nMenu:")
        print("1. Quick Sort")
        print("2. Binary Search")
        print("3. Web Scraping")
        print("4. Exit")

        choice = input("Introduzca un número: ")

        if choice == '1':
            command = subprocess.run("mpiexec -n 4 python quick_sort.py", shell=True, capture_output=True, text=True)
            print(command.stdout.strip())

        elif choice == '2':
            command = subprocess.run("mpiexec -n 4 python binary_search.py", shell=True, capture_output=True, text=True)
            lines = command.stdout.strip().split('\n\n\n')
            formatted_output = "\n\n".join([f"{line}\n" for line in lines[:-1]])

            formatted_output += lines[-1]
            print(formatted_output)

        elif choice == '3':
            command = subprocess.run("mpiexec -n 4 python web_scrapping.py", shell=True, capture_output=True, text=True)
            lines = command.stdout.strip().split('\n')
            formatted_output = "\n".join([f"{line.split()[0]} {int(line.split()[1]) + 1062}" for line in lines])
            print(formatted_output)

        elif choice == '4':
            break

        else:
            print('Introduzca un número valido')