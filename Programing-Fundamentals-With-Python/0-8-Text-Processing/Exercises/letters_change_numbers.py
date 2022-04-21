words = input().split()
possitions = [chr(let) for let in range(ord("A"), ord("Z") + 1)]
result = 0
for word in words:
    first_l = word[0]
    last_l = word[-1]
    n = int(word[1:len(word) - 1])
    if first_l.isupper():
        n = n / (possitions.index(first_l.upper()) + 1)
    else:
        n *= possitions.index(first_l.upper()) + 1
    
    if last_l.isupper():
        n -= possitions.index(last_l.upper()) + 1
    else:
        n += possitions.index(last_l.upper()) + 1 
    
    result += n

print(f"{result:.2f}")
