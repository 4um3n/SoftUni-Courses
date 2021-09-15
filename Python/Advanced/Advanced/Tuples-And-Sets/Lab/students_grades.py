students = {}
for _ in range(int(input())):
    name, grade = input().split()
    if name not in students:
        students[name] = []

    students[name].append(float(grade))

students = {n: {'grades': [f"{x:.2f}" for x in g], "average": sum(g) / len(g)} for n, g in students.items()}
[print(f"{n} -> {' '.join(g['grades'])} (avg: {g['average']:.2f})") for n, g in students.items()]
