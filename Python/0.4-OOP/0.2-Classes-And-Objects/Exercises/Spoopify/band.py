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
        for i in range(len(self.albums)):
            if self.albums[i].username == album_name:
                if self.albums[i].published:
                    return f"Album has been published. It cannot be removed."

                break
        else:
            return f"Album {album_name} is not found."

        self.albums.pop(i)
        return f"Album {album_name} has been removed."

    def details(self):
        info = f"Band {self.name}\n"
        info += '\n'.join([a.details() for a in self.albums])
        return info
