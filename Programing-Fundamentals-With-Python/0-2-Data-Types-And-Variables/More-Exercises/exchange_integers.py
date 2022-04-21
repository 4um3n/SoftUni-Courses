a = int(input())
b = int(input())
print(f"Before:\n"
      f"a = {a}\n"
      f"b = {b}")

a, b = b, a
print(f"After:\n"
      f"a = {a}\n"
      f"b = {b}")
