class Song:
    def __init__(self, name, length, single):
        self.username = name
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.username} - {self.length}"
