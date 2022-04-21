text = input()
print(''.join([ch for ch in text if ch.isdigit()]))
print(''.join([ch for ch in text if ch.isalpha()]))
print(''.join([ch for ch in text if not ch.isdigit() and not ch.isalpha()]))
