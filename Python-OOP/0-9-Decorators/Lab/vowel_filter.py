def vowel_filter(function):
    def wrapper():
        vowels = 'ayouei'
        letters = function()
        return [let for let in letters if let in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
