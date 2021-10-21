import os
from os import path


def create_file(file_path):
    open(file_path, "w").close()


def add_content_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(f"{content}\n")


def replace_text_in_file(file_path, old_text, new_text):
    if not path.exists(file_path):
        print(f"An error occurred")
        return

    with open(file_path, "r+") as file:
        text = file.read()
        text = text.replace(old_text, new_text, text.count(old_text))
        file.truncate(0)
        file.seek(0)
        file.write(text)


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"An error occurred")


files_dir_path = path.join(os.getcwd(), "Files")
command = input()
while command != "End":
    command = command.split("-")
    file_name = command[1]
    file_location = path.join(files_dir_path, file_name)

    if "Create" in command:
        create_file(file_location)

    elif "Add" in command:
        content_data = command[2]
        add_content_to_file(file_location, content_data)

    elif "Replace" in command:
        old_string, new_string = command[2], command[3]
        replace_text_in_file(file_location, old_string, new_string)

    elif "Delete" in command:
        delete_file(file_location)

    command = input()
