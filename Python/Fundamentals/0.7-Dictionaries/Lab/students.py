modules = {}
command = ' '.join(input().split("_"))
while command not in modules:
    student, student_id, module = command.split(":")
    if module not in modules:
        modules[module] = {}
    
    modules[module].update({student: student_id})
    command = ' '.join(input().split("_"))

for s, i in modules[command].items():
    print(f"{s} - {i}")
