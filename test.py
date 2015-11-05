# Import modules for CGI handling 
import cgi, cgitb 
import nflgame
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

playersArr = []
player_name = form.getvalue('player_name')

games = nflgame.games(2015, week=1)
players = nflgame.combine(games)
player_stats = players.name(player_name)


#players = nflgame.combine_game_stats(games)
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<link rel=%s type=%s href=%s>" % ("stylesheet", "text/css", "/projects/cgitest/styles.css")
print "<script type=%s src=%s></script>" % ("text/javascript", "/projects/cgitest/playertracker.js")
print "<title>Player Tracker</title>"
print "</head>"
print "<body>"
print """
	<form action="/cgi-bin/test.py" method="post">
	Player Name: <input type="text" name="player_name">  <br />


	<input type="submit" value="Submit" />
	</form>
	
	"""
playersArr = player_name.split(',')
def calcFant(player):
	fpoints = 0
	tdpoints = 0
	
	if player.guess_position == "QB":
		tdpoints = player.tds * 4
	else:
		tdpoints = player.tds * 6
		
	fpoints = tdpoints + (player.rushing_yds/10.0) + (player.receiving_yds/10.0) + (player.passing_yds/25.0) + (player.twoptm * 2) - (player.passing_ints * 2) - (player.fumbles_lost * 2)
	return fpoints

def playerOutput(playersList):
	for p in playersList:
		stats = players.name(p)
		pPoints = calcFant(stats)
		print "<h4>%s %s %s TDs: %s Receiving Yards: %s Rushing Yards: %s Passing Yards: %s Two point conversions: %s Fumbles Lost: %s Interceptions: %s Total Fantasy Points: %s </h4>" % (stats.team,  stats.guess_position, stats.name, stats.tds, stats.receiving_yds, stats.rushing_yds, stats.passing_yds, stats.twoptm, stats.fumbles_lost, stats.passing_ints, pPoints)
		
playerOutput(playersArr)

print "</html>"


	
	


	
	