string_data = input()
string = [index for index in range(len(string_data)) if ord(string_data[index]) in range(65, 91)]
print(string)
