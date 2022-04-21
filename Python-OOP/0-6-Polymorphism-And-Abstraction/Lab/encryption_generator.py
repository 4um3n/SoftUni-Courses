class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other):
        encrypted_text = []

        for char in self.text:
            if not isinstance(other, int):
                raise ValueError(f"You must add a number.")

            encrypted_char_ord = ord(char) + other

            while encrypted_char_ord < 32:
                encrypted_char_ord += 95

            while encrypted_char_ord > 126:
                encrypted_char_ord -= 95

            encrypted_text.append(chr(encrypted_char_ord))

        return ''.join(encrypted_text)
