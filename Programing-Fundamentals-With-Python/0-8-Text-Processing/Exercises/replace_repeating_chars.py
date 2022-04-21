text = input()
changed_text = [text[i] for i in range(len(text)) if i == 0 or text[i] != text[i - 1]]
print(''.join(changed_text))
