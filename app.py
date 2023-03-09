import logging
import copy
from copy import deepcopy

from constants import PLAYERS
from constants import TEAMS

# logging
log = "debug.log"
logging.basicConfig(filename=log, level=logging.DEBUG)
#this list will be used 
new_teams = []

def clean_data():
    global all_players
    all_players = copy.deepcopy(PLAYERS)

    for player in all_players:
        player_height = player["height"].split()
        player["height"] = int(player_height[0])

        player_experience = player["experience"]
        if player_experience == "YES":
            player["experience"] = True
        else:
            player["experience"] = False
        all_players = all_players

def balance_teams():
    teams = TEAMS.copy()

    num_of_teams = int(len(TEAMS))
    num_of_players = int(len(all_players))
    num_players_team = int((num_of_players / num_of_teams))
      
    squads = []
    for i in range(0, num_of_players, num_players_team):
        squads.append(all_players[i:i + num_players_team])

    team_lists = []
    for i in range(num_of_teams):
      teams_name = teams[i]
      squad = squads[i]
      team_list = [{"team": teams_name, "players": squad}]
      team_lists.append(team_list)
      #logging.debug(team_lists)
    return team_lists

# DISPLAY
def display_stats(): 
  print("BASKETBALL TEAM STATS TOOL")
  print("---- MENU----")

  print("""
  Here are your choices:
        1) Display Team Stats
        2) Quit
  """)

  menu_option = input("Enter an option:  ") 

  if menu_option == "1":
    print("""
          1) Panthers
          2) Bandits
          3) Warriors
    """)

    team_option = input("Enter an option:  ")

    if team_option == "1":
      choosen_team = balance_teams()[0]
    elif team_option == "2":
      choosen_team = balance_teams()[1]
    elif team_option == "3":
      choosen_team = balance_teams()[2]
    else:
      want_to_continue = input("Sorry, not valid option. Do you want to continue? Y/N ")
      if want_to_continue.lower() == "y":
        display_stats()
      else:
        exit()

    for team in choosen_team:
        # Team's name as a string
        team_name = team["team"]
        player_names = team["players"]
        the_names = []
        for player_name in player_names:
          the_name = player_name["name"]
          the_names.append(the_name)

        # The player names as strings separated by commas
        all_names = ", ".join(the_names)

        # Total players on that team as an integer
        number_of_players = len(player_names)

    print("Team: {}".format(team_name))
    print("--------------------")
            
    print("Total players: {}".format(number_of_players))
      
    print("Players on Team: {}".format(all_names))

    want_to_continue = input("Do you want to continue? Y/N ")
    if want_to_continue.lower() == "y":
        display_stats()
    else:
        exit()
  elif menu_option == "2":
    exit()
  else:
      want_to_continue = input(
          "Sorry, not valid option. Do you want to try again? Y/N ")
      if want_to_continue.lower() == "y":
        display_stats()
      else:
        exit()

if __name__ == "__main__":
  clean_data()
  display_stats()

