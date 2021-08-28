numbers = input().split(", ")
beggar = int(input())
beggar_sums_list = []
for iteration in range(beggar):
    current_list = []
    for index in range(0, len(numbers) + 1, beggar):
        index += iteration
        if index < len(numbers):
            current_list.append(int(numbers[index]))

    beggar_sums_list.append(sum(current_list))

print(beggar_sums_list)
