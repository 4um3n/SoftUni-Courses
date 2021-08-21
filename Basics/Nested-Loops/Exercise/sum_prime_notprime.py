number = input()
prime_sum = 0
non_prime_sum = 0

while number != "stop":
    number = int(number)
    is_prime = True

    if number < 0:
        print(f"Number is negative.")
        number = input()
        continue

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                non_prime_sum += number
                is_prime = False
                break
        if is_prime:
            prime_sum += number

    number = input()

print(f"Sum of all prime numbers is: {prime_sum}\n"
      f"Sum of all non prime numbers is: {non_prime_sum}")
