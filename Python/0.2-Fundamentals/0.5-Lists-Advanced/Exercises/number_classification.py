numbers = [int(n) for n in input().split(", ")]
print(f"Positive: {', '.join(str(n) for n in numbers if n >= 0)}\n"
        f"Negative: {', '.join(str(n) for n in numbers if n < 0)}\n"
        f"Even: {', '.join(str(n) for n in numbers if n % 2 == 0)}\n"
        f"Odd: {', '.join(str(n) for n in numbers if n % 2 == 1)}")
