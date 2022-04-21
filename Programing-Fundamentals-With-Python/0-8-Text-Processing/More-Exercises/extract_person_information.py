for _ in range(int(input())):
    name, age = "", ""
    text = input()
    i = 0
    while i < len(text):
        if text[i] == "@":
            i += 1
            while i < len(text) and text[i] != "|":
                name += text[i]
                i += 1
        
        elif text[i] == "#":
            i += 1
            while i < len(text) and text[i] != "*":
                age += text[i]
                i += 1

        i += 1
    
    print(f"{name} is {age} years old.")
