def find_max(numbers):
    if not numbers:
        return None  # Return None for an empty list
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Input a list of numbers
num_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Calculate the maximum using the custom function
result_custom = find_max(num_list)

# Display the result
if result_custom is not None:
    print(f"The maximum number in the list is (using custom function): {result_custom}")
else:
    print("The list is empty.")
