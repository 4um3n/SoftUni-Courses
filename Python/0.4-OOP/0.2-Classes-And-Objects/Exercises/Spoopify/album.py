class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if self.published:
            return f"Cannot add songs. Album is published."

        elif song.single:
            return f"Cannot add {song.username}. It's a single"

        elif song in self.songs:
            return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.username} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return f"Cannot remove songs. Album is published."

        for i in range(len(self.songs)):
            if self.songs[i].username == song_name:
                break
        else:
            return f"Song is not in the album."

        self.songs.pop(i)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = f"Album {self.name}\n"
        info += '\n'.join([f"== {s.get_info()}" for s in self.songs])
        return info
