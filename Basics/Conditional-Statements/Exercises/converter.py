num_to_convert = float(input())
unit_in = input()
unit_out = input()

if unit_in == "m":
    if unit_out == "cm":
        num_to_convert *= 100
    elif unit_out == "mm":
        num_to_convert *= 1000

if unit_in == "cm":
    if unit_out == "m":
        num_to_convert /= 100
    elif unit_out == "mm":
        num_to_convert *= 10

if unit_in == "mm":
    if unit_out == "m":
        num_to_convert /= 1000
    elif unit_out == "cm":
        num_to_convert /= 10

print(f"{num_to_convert:.3f}")