first_w, second_w = input().split()
first_w, second_w = list(first_w), list(second_w)
result = 0
while 0 < len(first_w) and 0 < len(second_w):
    result += ord(first_w[0]) * ord(second_w[0])
    first_w.pop(0)
    second_w.pop(0)

first_w = [ord(f) for f in first_w]
second_w = [ord(s) for s in second_w]
result += sum(first_w) + sum(second_w)
print(result)
