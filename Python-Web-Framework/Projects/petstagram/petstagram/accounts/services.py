import os

from petstagram.settings import BASE_DIR


def get_profile_pictures_directory(filename: str) -> os.path:
    return os.path.join("images", "profile_pictures", filename)


def get_default_profile_picture_path():
    return os.path.join("images", "profile_pictures", "default", "default.png")
