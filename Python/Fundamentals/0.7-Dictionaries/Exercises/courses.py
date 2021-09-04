command, courses = input(), {}
while command != "end":
    course, student = command.split(" : ")
    if course not in courses:
        courses[course] = []
    
    courses[course].append(student)
    command = input()
    
for c, students in sorted(courses.items(), key=lambda x: -len(x[1])):
    print(f"{c}: {len(students)}")
    for s in sorted(students):
        print(f"-- {s}")
