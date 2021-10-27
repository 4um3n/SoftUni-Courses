class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.username} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.username} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.username} to the guild {self.name}"

    def kick_player(self, player_name):
        for p in self.players:
            if p.username == player_name:
                p.guild = "Unaffiliated"
                self.players.remove(p)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        info = [f"Guild: {self.name}"]

        if self.players:
            info.extend([p.player_info() for p in self.players])

        return '\n'.join(info)
