n = int(input())
word = input()
text_list = [input() for _ in range(n)]
print(text_list)
filtered_text_list = [text for text in text_list if word in text]
print(filtered_text_list)