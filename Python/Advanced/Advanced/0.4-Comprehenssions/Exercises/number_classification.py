numbers_data = [int(n) for n in input().split(", ")]
print(f"Positive: {', '.join([str(n) for n in numbers_data if n >= 0])}")
print(f"Negative: {', '.join([str(n) for n in numbers_data if n < 0])}")
print(f"Even: {', '.join([str(n) for n in numbers_data if not n % 2])}")
print(f"Odd: {', '.join([str(n) for n in numbers_data if n % 2])}")
