key = int(input())
message_length = int(input())
message_decrypted = ""

for i in range(message_length):
    char = input()
    char = chr(ord(char) + key)

    message_decrypted += char

print(f"{message_decrypted}")
