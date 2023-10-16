def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
search_target = 12
result = binary_search(my_list, search_target)
if result != -1:
    print(f"Element {search_target} found at index {result}.")
else:
    print(f"Element {search_target} not found in the list.")