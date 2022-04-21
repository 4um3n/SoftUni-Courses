def get_primes(sequence: list):
    def is_prime(n):
        if n < 2:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    for number in sequence:
        if is_prime(number):
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1])))
