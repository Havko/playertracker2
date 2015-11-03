# Import modules for CGI handling 
import cgi, cgitb 
import nflgame
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
def calcFant(player):
	fpoints = 0
	tdpoints = 0
	
	if player.guess_position == "QB":
		tdpoints = player.tds * 4
	else:
		tdpoints = player.tds * 6
		
	fpoints = tdpoints + (player.rushing_yds/10.0) + (player.receiving_yds/10.0) + (player.passing_yds/25.0) + (player_stats.twoptm * 2) - (player_stats.passing_ints * 2) - (player_stats.fumbles_lost * 2)
	return fpoints

player_name = form.getvalue('player_name')
games = nflgame.games(2015, week=1)
players = nflgame.combine(games)
player_stats = players.name(player_name)
playerPoints = calcFant(player_stats)

#players = nflgame.combine_game_stats(games)
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<link rel=%s type=%s href=%s>" % ("stylesheet", "text/css", "/projects/cgitest/styles.css")
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print """
	<form action="/cgi-bin/test.py" method="post">
	Player Name: <input type="text" name="player_name">  <br />


	<input type="submit" value="Submit" />
	</form>
	"""
print "<h4>%s %s %s TDs: %s Receiving Yards: %s Rushing Yards: %s Passing Yards: %s Two point conversions: %s Fumbles Lost: %s Interceptions: %s Total Fantasy Points: %s </h4>" % (player_stats.team, player_stats.guess_position, player_stats.name, player_stats.tds, player_stats.receiving_yds, player_stats.rushing_yds, player_stats.passing_yds, player_stats.twoptm, player_stats.fumbles_lost, player_stats.passing_ints, playerPoints  )
print "</html>"


	
	