n = int(input())
letters = [chr(a) + chr(b) + chr(c)
           for a in range(97, 97 + n)
           for b in range(97, 97 + n)
           for c in range(97, 97 + n)]
print('\n'.join(letters))
