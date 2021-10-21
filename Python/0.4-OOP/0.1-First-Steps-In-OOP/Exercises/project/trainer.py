from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemons = [p.name for p in self.pokemons]
        if pokemon_name not in pokemons:
            return f"Pokemon is not caught"

        self.pokemons.pop(pokemons.index(pokemon_name))
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        res = f"Pokemon Trainer {self.name}\n" \
              f"Pokemon count {len(self.pokemons)}\n"
        res += '\n'.join([f"- {p.pokemon_details()}" for p in self.pokemons])
        return res
