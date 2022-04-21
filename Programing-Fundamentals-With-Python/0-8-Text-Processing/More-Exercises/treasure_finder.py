keys = [int(n) for n in input().split()]
text= input()
while text != "find":
    keys_i = 0
    for i in range(len(text)):
        text = text[:i] + chr(ord(text[i]) - keys[keys_i]) + text[i + 1:]
        keys_i += 1
        if keys_i == len(keys):
            keys_i = 0    
    
    treasure, coordinates = "", ""
    ind = 0
    while ind < len(text):
        if text[ind] == "&":
            ind += 1
            while text[ind] != "&":
                treasure += text[ind]
                ind += 1

        elif text[ind] == "<":
            ind += 1
            while text[ind] != ">":
                coordinates += text[ind]
                ind += 1

        ind += 1
    
    print(f"Found {treasure} at {coordinates}")
    text = input()
