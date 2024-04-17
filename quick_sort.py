def partition(array:list, low:int, high:int) -> int:
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(array:list, low:int, high:int) -> list:
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

def main():
    data = [8, 7, 2, 1, 0, 9, 6]
    print(f'Unsorted Array: {data}')
    quickSort(data, 0, len(data)-1)
    print(f'Sorted Array: {data}')

if __name__ == '__main__':
    main()