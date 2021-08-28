string = input().split(", ")

if string[-1] == "wolf":
    print(f"Please go away and stop eating my sheep")
else:
    sheep_index = [abs(index) for index in range(-1, -len(string), -1) if string[index - 1] == "wolf"]
    print(f"Oi! Sheep number {sheep_index[0]}! You are about to be eaten by a wolf!")
