def newton_sqrt(number, guess=1.0, tolerance=1e-6):
    while True:
        new_guess = 0.5 * (guess + number / guess)
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess

# Input a number
num = float(input("Enter a number to find its square root: "))

# Calculate the square root using Newton's method
result = newton_sqrt(num)

# Display the result
print(f"The square root of {num} is approximately {result:.6f}") .
