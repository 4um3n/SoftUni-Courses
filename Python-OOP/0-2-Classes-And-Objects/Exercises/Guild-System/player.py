class Player:
    def __init__(self, name, hp, mp):
        self.username = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = f"Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f"Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.username}"

    def player_info(self):
        info = [f"Name: {self.username}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        info.extend([f"==={k} - {v}" for k, v in self.skills.items()])
        return '\n'.join(info)
