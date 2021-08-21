num1 = int(input())
num2 = int(input())

for number in range(num1, num2 + 1):
    odd_sum = 0
    even_sum = 0
    number = str(number)

    for index, num in enumerate(number):
        if index % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)

    if odd_sum == even_sum:
        print(f"{int(number)}", end=" ")
