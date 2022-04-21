numbers = [int(input()) for _ in range(int(input()))]
command = input()
filtered_numbers = []

if command == "even":
    filtered_numbers = [num for num in numbers if num % 2 == 0]
elif command == "odd":
    filtered_numbers = [num for num in numbers if num % 2 == 1]
elif command == "negative":
    filtered_numbers = [num for num in numbers if num < 0]
elif command == "positive":
    filtered_numbers = [num for num in numbers if num >= 0]

print(filtered_numbers)