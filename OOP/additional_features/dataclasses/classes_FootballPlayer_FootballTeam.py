from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, repr=False, compare=False)

    def add_players(self, player):
        self.players.append(player)


# Test №1
player = FootballPlayer('Kylian', 'Mbappe', 180000000)

print(player)
print(player.name)
print(player.surname)
print(player.value)

# Test №2
player1 = FootballPlayer('Jude', 'Bellingham', 120000000)
player2 = FootballPlayer('Vinicius', 'Junior', 120000000)
player3 = FootballPlayer('Kylian', 'Mbappe', 180000000)

print(player1 == player2)
print(player1 == player3)
print(player1 > player3)
print(player1 < player3)

# Test №3
team = FootballTeam('PSG')

print(team)
print(team.name)
print(team.players)

team.add_players(FootballPlayer('Kylian', 'Mbappe', 180000000))

print(team.players)

# Test №4
team1 = FootballTeam('PSG')
team2 = FootballTeam('PSG')
team3 = FootballTeam('Arsenal')

print(team1 == team2)
print(team1 != team2)
print(team1 == team3)
print(team1 != team3)
