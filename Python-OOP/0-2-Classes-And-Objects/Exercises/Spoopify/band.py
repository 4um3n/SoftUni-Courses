class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.username} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.username}."

    def remove_album(self, album_name):
        for album in self.albums:
            if album.username == album_name:
                if album.published:
                    return f"Album has been published. It cannot be removed."

                self.albums.remove(album)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        info = [f"Band {self.name}"]
        info.extend([a.details() for a in self.albums])
        return '\n'.join(info)
