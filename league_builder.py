import csv

# 2. Make sure the script doesn't execute when imported; put all of your logic and
# function calls inside of an if __name__ == "__main__": block.
if __name__ == "__main__":

# 3. Create variables and programming logic to divide the 18 players into three
# teams: Sharks, Dragons and Raptors. Make sure the teams have the same number of
# players on them, and that the experience players are divided equally across the
# three teams.

    #define valiables
    experienced = { "sharks": 0, "dragons" : 0, "raptors" : 0 }
    teams = { "sharks": [], "dragons" : [], "raptors" : [] }

    # Open csv file, read into ordeed dictionary
    with open('soccer_players.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        # Iterate players and place into dictionary
        for row in reader:
            # See which team has the least experienced players
            if row['Soccer Experience'] == 'YES':
                team = min(experienced, key=experienced.get)
                experienced[team] += 1
                teams[team].append([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']])
            # See which team has the least players
            else:
                team_sizes = {k: len(v) for k, v in teams.items()}
                team = min(team_sizes, key=team_sizes.get)
                teams[team].append([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']])


# 4. Create a text file named teams.txt that includes the name of a team, followed
# by the players on that team. List all three teams and their players.

# 5. In the list of teams, include the team name on one line, followed by a
# separate line for each player. Include the player's name, whether the player has
# experience playing soccer, and the player's guardian names. Separate each bit of
# player information by a comma. For example, the text file might start something
# like this:
# Sharks
# Frank Jones, YES, Jim and Jan Jones
# Sarah Palmer, YES, Robin and Sari Washington
# Joe Smith, NO, Bob and Jamie Smith

    # Output to  teams file
    # Iterate though teams, then players
    # Write to file the each team, then player details
    file = open("teams.txt","w")
    for team, players in teams.items():
        file.write(team + "\n")
        for player in players:
            file.write(", ".join(player) + "\n")
    file.close()


# Create 18 text files ("welcome" letters to the players' guardians). You'll
# create 1 text file for each player. Use the player’s name as the name of the
# file, in lowercase and with underscores and ending in .txt. For example,
# kenneth_love.txt. Make sure that each file begins with the text "Dear"
# followed by the guardian(s) name(s). Also include the additional required
# information: player's name, team name, and date & time of first practice.

    # Create a template for the letters.
    letter = "Dear {},\n\n{} has been selected to play on the team: {}, in this years youth soccer league.\n\nPractice starts Saturday, 4th February at 10am at the town soccer field. Please be on time.\n\nCoach Py."
    # Iterate though teams and players, creating indervidual files based on template
    for team, players in teams.items():
        for player in players:
            file = open(player[0].replace(" ", "_").lower()+".txt","w")
            file.write(letter.format(player[2], player[0], team))
            file.close()

# Done
