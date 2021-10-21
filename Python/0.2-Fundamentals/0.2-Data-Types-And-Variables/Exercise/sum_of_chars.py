iterations_count = int(input())
letters_sum = 0
for _ in range(iterations_count):
    letters_sum += ord(input())

print(f"The sum equals: {letters_sum}")
