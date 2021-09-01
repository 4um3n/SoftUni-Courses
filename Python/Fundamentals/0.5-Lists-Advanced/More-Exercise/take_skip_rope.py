text, digits, i = list(input()), [], 0
while i < len(text):
    if text[i].isdigit():
        digits.append(int(text.pop(i)))
        continue
    
    i += 1

take_digits = [digits[i] for i in range(len(digits)) if i % 2 == 0]
skip_digits = [digits[i] for i in range(len(digits)) if i % 2 == 1]
decoded_message = []

for t, s in zip(take_digits, skip_digits):
    for _ in range(t):
        if len(text) > 0:
            decoded_message.append(text.pop(0))
    
    for _ in range(s):
        if len(text) > 0:
            text.pop(0)

print("".join(decoded_message))
