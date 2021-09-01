journal = input().split(", ")
command = input()
while command != "Craft!":
    command = command.split(" - ")
    if "Collect" in command:
        item = command[1]
        if item not in journal:
            journal.append(item)
    
    elif "Drop" in command:
        item = command[1]
        if item in journal:
            journal.remove(item)
    
    elif "Combine Items" in command:
        old_item, new_item = command[1].split(":")
        if old_item in journal:
            journal.insert(journal.index(old_item) + 1, new_item)
    
    elif "Renew" in command:
        item = command[1]
        if item in journal:
            journal.append(journal.pop(journal.index(item)))
    
    command = input()

print(', '.join(journal))
