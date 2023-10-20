def find_primes(n):
    primes = []
    num = 2

    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
        num += 1

    return primes

n = 10
prime_list = find_primes(n)
print(f"The first {n} prime numbers are:", prime_list)
