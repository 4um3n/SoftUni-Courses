class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))

        return f"value is not a float"

    @classmethod
    def from_roman(cls, roman_value):
        romans_mapper = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        prev = ""
        for char in roman_value:
            res += romans_mapper.get(char)
            if (prev + char) in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                res -= 2 * romans_mapper.get(prev)

            prev = char

        return cls(res)

    @classmethod
    def from_string(cls, string_value):
        if not isinstance(string_value, str) or not string_value.isalnum():
            return f"wrong type"

        return cls(int(string_value))
