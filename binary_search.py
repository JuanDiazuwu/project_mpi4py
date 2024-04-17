def binary_search(arr:list, low:int, high:int, x:int) -> int:
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)
	else:
		return -1

def main():
    data = [8, 7, 2, 1, 0, 9, 6, 10]
    search_number = 10
    result = binary_search(data, 0, len(data) - 1, search_number)

    if result != -1:
        print(f"Element is present at index {str(result)}")
    else:
        print("Element is not present in array")

if __name__ == '__main__':
    main()