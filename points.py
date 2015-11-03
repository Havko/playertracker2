import nflgame
player_name = "B.Roethlisberger"
games = nflgame.games(2015, week=1)
players = nflgame.combine(games)
player_stats = players.name(player_name)

def calcFant(player):
	fpoints = 0
	tdpoints = 0
	rushPoints = 0
	recPoints = 0
	if player.guess_position == "QB":
		tdpoints = player.tds * 4
	else:
		tdpoints = player.tds * 6
		
	fpoints = tdpoints + (player.rushing_yds/10.0) + (player.receiving_yds/10.0) + (player.passing_yds/25.0) + (player_stats.twoptm * 2) - (player_stats.passing_ints * 2)
	return fpoints
playerPoints = calcFant(player_stats)
print playerPoints

