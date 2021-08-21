text = input()
vowels_sum = 0

for char in text:
    vowels_value = 0

    if char == "a":
        vowels_value = 1
    elif char == "e":
        vowels_value = 2
    elif char == "i":
        vowels_value = 3
    elif char == "o":
        vowels_value = 4
    elif char == "u":
        vowels_value = 5

    vowels_sum += vowels_value

print(vowels_sum)
