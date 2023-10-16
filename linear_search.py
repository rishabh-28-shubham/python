def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
my_list = [2, 4, 6, 8, 10]
search_target = 6
result = linear_search(my_list, search_target)
if result != -1:
    print(f"Element {search_target} found at index {result}.")
else:
    print(f"Element {search_target} not found in the list.")