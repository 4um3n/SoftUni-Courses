class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                p.guild = "Unaffiliated"
                self.players.remove(p)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        res = [f"Guild: {self.name}"]

        if self.players:
            res.extend([p.player_info() for p in self.players])

        return '\n'.join(res)
