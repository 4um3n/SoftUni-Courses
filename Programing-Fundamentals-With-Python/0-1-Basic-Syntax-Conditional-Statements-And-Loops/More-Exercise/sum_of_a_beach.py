string = input().lower()
count = 0
second_string = string

while True:
    original_len = len(string)

    if "sand" in string:
        digits = 4
        second_string = string.replace("sand", "")
        string = second_string
        count += (original_len - len(string)) / digits
    elif "water" in string:
        digits = 5
        second_string = string.replace("water", "")
        string = second_string
        count += (original_len - len(string)) / digits
    elif "fish" in string:
        digits = 4
        second_string = string.replace("fish", "")
        string = second_string
        count += (original_len - len(string)) / digits
    elif "sun" in string:
        digits = 3
        second_string = string.replace("sun", "")
        string = second_string
        count += (original_len - len(string)) / digits
    else:
        break

print(int(count))
