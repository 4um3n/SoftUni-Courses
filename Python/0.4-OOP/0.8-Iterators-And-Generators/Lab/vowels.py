class vowels:
    VALID_VOWELS = ["a", "e", "i", "o", "u", "y"]

    def __init__(self, text: str) -> None:
        self.text = text
        self.vowels = [letter for letter in self.text if letter.lower() in self.VALID_VOWELS]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.vowels):
            self.index = 0
            raise StopIteration

        self.index += 1
        return self.vowels[self.index - 1]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
