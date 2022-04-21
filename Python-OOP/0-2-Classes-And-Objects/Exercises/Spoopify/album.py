class Album:
    def __init__(self, name, *songs):
        self.username = name
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
        return f"Song {song.username} has been added to the album {self.username}."

    def remove_song(self, song_name):
        if self.published:
            return f"Cannot remove songs. Album is published."

        for song in self.songs:
            if song.username == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.username}."

        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.username} is already published."

        self.published = True
        return f"Album {self.username} has been published."

    def details(self):
        info = [f"Album {self.username}"]
        info.extend([f"== {s.get_info()}" for s in self.songs])
        return '\n'.join(info)
