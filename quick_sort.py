from mpi4py import MPI
from random import randint
import math

DATA = [3, 5, 7, 4, 6, 7, 11, 9, 2, 8, 3, 2]
print(DATA)

def partition(array:list, low:int, high:int) -> int:
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quick_sort(array:list, low:int, high:int) -> list:
  if low < high:
    pi = partition(array, low, high)
    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)

def parallel_quicksort(data:list, comm):
  root = 0
  max_processors = comm.size
  new_list = []
  bin_size = math.floor((max(data) - min(data)) / comm.size)
  
  for rank in range(max_processors):
      new_list.append([x for x in data if (x >= bin_size * rank + rank) and x <= (bin_size + bin_size * rank + rank)])
  
  v = comm.scatter(new_list, root)
  quick_sort(v, 0, len(v) - 1)
  
  g = comm.gather(v, root)
  if comm.rank==0:
    print([item for sublist in g for item in sublist])

def main_quick_sort():
  comm = MPI.COMM_WORLD
  parallel_quicksort(DATA, comm)

if __name__ == '__main__':
    main_quick_sort()