import os
import re
import json

current_path = os.getcwd()
users_file_path = os.path.join(current_path, 'DB', 'users.txt')
credentials_file_path = os.path.join(current_path, 'DB', 'user_credentials_db.txt')


def register_validator(**user):
    user = {k: v.get() for k, v in user.items()}
    error = []
    for k, v in user.items():
        if not v and k != 'is_admin':
            error.append(f"Enter {' '.join(k.split('_'))}!")

    if error:
        return '\n'.join(error)

    for k, v in user.items():
        if k == "password":
            digits = re.findall(r"\d", v)
            upper_letters = re.findall(r"[A-Z]+", v)
            lower_letters = re.findall(r"[a-z]+", v)

            if len(v) < 8:
                error.append(f"Password must be at least 8 symbols long!")
            if not digits:
                error.append(f"Password must contain one or more digits!")
            if not upper_letters:
                error.append(f"Password must contain upper case letters!")
            if not lower_letters:
                error.append(f"Password must contain lower case letters!")

            if error:
                return '\n'.join(error)

    with open(users_file_path, 'r') as file:
        if user['username'] in file.read():
            return f"Username is already registered!"

    with open(credentials_file_path, 'a') as file:
        file.write(f"{user['username']}, {user['password']}\n")

    del user['password']
    user.update({'products': []})

    with open(users_file_path, 'a', newline='\n') as file:
        file.write(json.dumps(user))
        file.write(f"\n")

    return False


def login_validator(username, password):
    with open(credentials_file_path, 'r') as file:
        text = [line for line in file.read().split('\n') if line]
        for line in text:
            current_user, current_pass = line.split(', ')
            if current_user == username and password == current_pass:
                return True

        return False


def is_user_admin(username):
    with open(users_file_path, 'r') as file:
        for line in file.read().split('\n'):
            if line:
                line = json.loads(line)
                if username == line['username'] and line['is_admin']:
                    return True
    return False
