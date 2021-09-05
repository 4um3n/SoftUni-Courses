text, rage_quit, current, digits = input(), "", "", ""
for i in range(len(text)):
    if not text[i].isdigit():
        current += text[i]
        continue
    
    if i < len(text) - 1 and text[i + 1].isdigit():
        digits += text[i]
        continue
    
    digits += text[i]
    rage_quit += current.upper() * int(digits)
    current, digits = "", ""

unique_symbols_count = len(set(rage_quit))
print(f"Unique symbols used: {unique_symbols_count}\n{rage_quit}")
