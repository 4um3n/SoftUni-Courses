bar = lambda n, i: f"100% Complete!\n[{'%' * n}{'.' * i}]" if n == 10 else f"{n * 10}% [{'%' * n}{'.' * i}]\nStill loading..." 
a = int(input()) // 10
b = 10 - a
print(bar(a, b))
