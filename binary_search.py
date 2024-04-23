from mpi4py import MPI
import random

def binary_search(arr, low, high, x):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()



    data = []
    for i in range(100):
        data.append(2 * i + 1)  # Genera números impares del 1 al 199

    search_number = 80


    # Dividimos el arreglo entre los procesos
    local_data_size = len(data) // size

    # índices de inicio y fin para los datos locales
    start_index = rank * local_data_size
    end_index = (rank + 1) * local_data_size
    local_data = data[start_index:end_index]


    print("---------------------------------")
    print(f"Rank {rank}: Subarreglo desde el índice {start_index} hasta el índice {end_index - 1}:\n{local_data}")



    result = binary_search(local_data, 0, len(local_data) - 1, search_number)
    gathered_results = comm.gather(result, root=0)
    #print(gathered_results)

    # Imprimir resultados en el proceso 0
    if rank == 0:
        final_result = -1          
        for i, result in enumerate(gathered_results):
            if result != -1:  
                final_result = i * local_data_size + result
                break  

        if final_result != -1:
            print("\n")
            print(f"El elemento {search_number} SI está presente en el índice {final_result}.")
        else:
            print("\n")
            print(f"El elemento {search_number} NO está presente en el arreglo.")
    



if __name__ == '__main__':
    main()
