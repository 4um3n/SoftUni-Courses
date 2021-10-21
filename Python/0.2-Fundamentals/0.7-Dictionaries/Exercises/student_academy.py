students = {}
for _ in range(int(input())):
    student, appraisal = input(), float(input())
    if student not in students:
        students[student] = []
    
    students[student].append(appraisal)

students = {s: sum(a) / len(a) for s, a in students.items() if sum(a) / len(a) >= 4.50}
for s, a in sorted(students.items(), key=lambda x: -x[1]):
    print(f"{s} -> {a:.2f}")
