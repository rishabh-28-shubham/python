def custom_exponent(base, exponent):
    result = 1
    for _ in range(int(exponent)):
        result *= base
    return result

# Input the base and exponent
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))

# Calculate the exponentiation using the custom function
result = custom_exponent(base, exponent)

# Display the result
print(f"{base} raised to the power of {exponent} is (using custom function): {result}")
