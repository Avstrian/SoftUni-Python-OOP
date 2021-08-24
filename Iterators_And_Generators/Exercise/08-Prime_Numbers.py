def get_primes(numbers):
    for n in numbers:
        if not n == 0 and not n == 1:
            prime = True

            for i in range(2, n):
                if n % i == 0:
                    prime = False
            if prime:
                yield n
