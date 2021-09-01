notes = []
command = input()
while command != "End":
    command = command.split("-")
    importance, note = int(command[0]), command[1]
    notes.append((importance, note))
    command = input()

notes = [n for i, n in sorted(notes, key=lambda x: x[0])]
print(notes)