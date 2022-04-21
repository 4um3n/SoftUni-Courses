text = input()
emoticons = [text[i] + text[i + 1] for i in range(len(text)) if text[i] == ":" and i < len(text) - 1]
print('\n'.join(emoticons))
