number = [int(char) for char in input()]
number.sort(reverse=True)
print("".join([str(digit) for digit in number]))

