######################################################################
# Program: Football League Table System                              #
# Author:                                                            #
######################################################################
# Description:                                                       #
#                                                                    #
######################################################################

##################
# Import Modules #
##################

import copy

####################
# Global Variables #
####################

# Each team is a dictionary containing a string 'name' and integer values for
# 'points', games 'played', goal scored 'gs', goals conceded 'gc', and games 'won'
emptyTeam = { "name": "" , "points": 0, "played":0, "gs": 0, "gc": 0, "won": 0 }

# The stats for all teams are stored in the 'teams' variable
teams = {}


# The games list holds each game as a list that contains two string elements
# The first string element contains the team i.d.'s separated by a ':'
# The first team in the first string is the 'home' team, the second is the away team
# The second string in a game inner list contains the score separated by a ':'
# The first score is for the home team and the second is for the away team
games = [   
        ]

with open(r"teams.dat") as datFile:
    data = [data.split()[0] for data in datFile]
team_1 = { "name": data[0] , "points": 0, "played":0, "gs": 0, "gc": 0, "won": 0 }
team_2 = { "name": data[1] , "points": 0, "played":0, "gs": 0, "gc": 0, "won": 0 }
team_3 = { "name": data[2] , "points": 0, "played":0, "gs": 0, "gc": 0, "won": 0 }
team_4 = { "name": data[3] , "points": 0, "played":0, "gs": 0, "gc": 0, "won": 0 }
team_5 = { "name": data[4] , "points": 0, "played":0, "gs": 0, "gc": 0, "won": 0 }

def readGames():
    f_game=[]
    with open(r"games.dat") as datFile:
        game = [data.split()[0] for data in datFile]
        for j in range(len(game)):
            fix = game[j].split(",")[0]
            res = game[j].split(",")[1]
           
            games.append([fix,res])
        

def displayTeams():
    readGames()
    print(games)
    for i in range(len(games)):
       
        
        game=games[i][0]
        result=games[i][1]
        team_arr = game.split(':')
        result_arr = result.split(":")
        
        # Winning
        if(int(result_arr[0])>int(result_arr[1])):
            if(int(team_arr[0])==1):
                team_1['points']+=3
                team_1['played']+=1
                team_1['gs']+=int(result_arr[0])
                team_1['gc']+=int(result_arr[1])
                team_1['won']+=1
                
            if(int(team_arr[0])==2):
                team_2['points']+=3
                team_2['played']+=1
                team_2['gs']+=int(result_arr[0])
                team_2['gc']+=int(result_arr[1])
                team_2['won']+=1
                
            if(int(team_arr[0])==3):
                team_3['points']+=3
                team_3['played']+=1
                team_3['gs']+=int(result_arr[0])
                team_3['gc']+=int(result_arr[1])
                team_3['won']+=1
            if(int(team_arr[0])==4):
                team_4['points']+=3
                team_4['played']+=1
                team_4['gs']+=int(result_arr[0])
                team_4['gc']+=int(result_arr[1])
                team_4['won']+=1
            if(int(team_arr[0])==5):
                team_5['points']+=3
                team_5['played']+=1
                team_5['gs']+=int(result_arr[0])
                team_5['gc']+=int(result_arr[1])
                team_5['won']+=1
        elif(int(result_arr[1])>int(result_arr[0])):
            if(int(team_arr[1])==1):
                team_1['points']+=3
                team_1['played']+=1
                team_1['gs']+=int(result_arr[1])
                team_1['gc']+=int(result_arr[0])
                team_1['won']+=1
            if(int(team_arr[1])==2):
                team_2['points']+=3
                team_2['played']+=1
                team_2['gs']+=int(result_arr[1])
                team_2['gc']+=int(result_arr[0])
                team_2['won']+=1
                
            if(int(team_arr[1])==3):
                team_3['points']+=3
                team_3['played']+=1
                team_3['gs']+=int(result_arr[1])
                team_3['gc']+=int(result_arr[0])
                team_3['won']+=1
            if(int(team_arr[1])==4):
                team_4['points']+=3
                team_4['played']+=1
                team_4['gs']+=int(result_arr[1])
                team_4['gc']+=int(result_arr[0])
                team_4['won']+=1
            if(int(team_arr[1])==5):
                team_5['points']+=3
                team_5['played']+=1
                team_5['gs']+=int(result_arr[1])
                team_5['gc']+=int(result_arr[0])
                team_5['won']+=1
        # Losing
        if(int(result_arr[0])<int(result_arr[1])):
            if(int(team_arr[0])==1):
                
                team_1['played']+=1
                team_1['gs']+=int(result_arr[0])
                team_1['gc']+=int(result_arr[1])
                team_1['won']+=1
                
            elif(int(team_arr[0])==2):
                
                team_2['played']+=1
                team_2['gs']+=int(result_arr[0])
                team_2['gc']+=int(result_arr[1])
                team_2['won']+=1
                
            if(int(team_arr[0])==3):
                
                team_3['played']+=1
                team_3['gs']+=int(result_arr[0])
                team_3['gc']+=int(result_arr[1])
                team_3['won']+=1
            if(int(team_arr[0])==4):
                
                team_4['played']+=1
                team_4['gs']+=int(result_arr[0])
                team_4['gc']+=int(result_arr[1])
                team_4['won']+=1
            if(int(team_arr[0])==5):
                
                team_5['played']+=1
                team_5['gs']+=int(result_arr[0])
                team_5['gc']+=int(result_arr[1])
                team_5['won']+=1
        elif(int(result_arr[1])<int(result_arr[0])):
            if(int(team_arr[1])==1):
                
                team_1['played']+=1
                team_1['gs']+=int(result_arr[1])
                team_1['gc']+=int(result_arr[0])
                
            if(int(team_arr[1])==2):
               
                team_2['played']+=1
                team_2['gs']+=int(result_arr[1])
                team_2['gc']+=int(result_arr[0])
                
                
            if(int(team_arr[1])==3):
                
                team_3['played']+=1
                team_3['gs']+=int(result_arr[1])
                team_3['gc']+=int(result_arr[0])
                
            if(int(team_arr[1])==4):
                
                team_4['played']+=1
                team_4['gs']+=int(result_arr[1])
                team_4['gc']+=int(result_arr[0])
                
            if(int(team_arr[1])==5):
                
                team_5['played']+=1
                team_5['gs']+=int(result_arr[1])
                team_5['gc']+=int(result_arr[0])
               
        # Drawing 
        else:
            if(int(team_arr[0])==1):
                team_1['points']+=1
                team_1['played']+=1
                team_1['gs']+=int(result_arr[0])
                team_1['gc']+=int(result_arr[1])
                
            if(int(team_arr[0])==2):
                team_2['points']+=1
                team_2['played']+=1
                team_2['gs']+=int(result_arr[0])
                team_2['gc']+=int(result_arr[1])
                
                
            if(int(team_arr[0])==3):
                team_3['points']+=1
                team_3['played']+=1
                team_3['gs']+=int(result_arr[0])
                team_3['gc']+=int(result_arr[1])
                
            if(int(team_arr[0])==4):
                team_4['points']+=1
                team_4['played']+=1
                team_4['gs']+=int(result_arr[0])
                team_4['gc']+=int(result_arr[1])
                
            if(int(team_arr[0])==5):
                team_5['points']+=1
                team_5['played']+=1
                team_5['gs']+=int(result_arr[0])
                team_5['gc']+=int(result_arr[1])
                
            if(int(team_arr[1])==1):
                team_1['points']+=1
                team_1['played']+=1
                team_1['gs']+=int(result_arr[1])
                team_1['gc']+=int(result_arr[0])
                
            if(int(team_arr[1])==2):
                team_2['points']+=1
                team_2['played']+=1
                team_2['gs']+=int(result_arr[1])
                team_2['gc']+=int(result_arr[0])
                
                
            if(int(team_arr[1])==3):
                team_3['points']+=1
                team_3['played']+=1
                team_3['gs']+=int(result_arr[1])
                team_3['gc']+=int(result_arr[0])
                
            if(int(team_arr[1])==4):
                team_4['points']+=1
                team_4['played']+=1
                team_4['gs']+=int(result_arr[1])
                team_4['gc']+=int(result_arr[0])
                
            if(int(team_arr[1])==5):
                team_5['points']+=1
                team_5['played']+=1
                team_5['gs']+=int(result_arr[1])
                team_5['gc']+=int(result_arr[0])
                
            




########################
# Function Definitions #
########################

############################################################
# Function: setupResetTeams()                              #
# Author: Andy Symons &                                    #
############################################################
# Description: This function sets up or resets the 'teams' #
# dictionary of dictionaries to a start of season          #
# initialisation                                           #
############################################################
# Parameters: No parameters                                #
############################################################
# Return Value: No return value                            #
############################################################

def setupResetTeams():
    
    # For each team from 1 through 5
    # A 'for' loop is used here rather than a while loop as this is a counting scenario
    for i in range(1, 6):
        # copy the 'emptyTeam' to the teams dictionary using the key integer 'i'
        teams[i] = copy.deepcopy(emptyTeam)
        # Set the name of the team to 'Team ' plus the string cast of the integer 'i'
        teams[i]["name"] = data[i-1]
        

############################################################
# Function: sortTeams                                      #
# Author: A. Symons                                        #
############################################################
# Description: This function sorts the team index into     #
# descending order based upon an order parameter           #
############################################################
# Parameters: index: A list containing integers in an      #
#                    initial order                         #
#             order: An integer indicating which team      #
#                    variable is used to base the order on #
############################################################
# Return Value: A list containing the index list in its    #
# new order                                                #
############################################################
displayTeams()
def sortTeams(index, order):
     
    teams[1]=team_1
    teams[2]=team_2
    teams[3]=team_3
    teams[4]=team_4
    teams[5]=team_5
    
    # for each item in list up to second to last item
    # A for loop is utilised here and not a while loop, as this is a counting scenario
    for i in range(0, len(index) - 1):
        # for each item in list starting at 'i' plus one, up to last item
        # A for loop is utilised here and not a while loop, as this is a counting scenario
        
        for j in range(i+1, len(index)):
            # Set the values used to sort to zero
            iVal = 0
            jVal = 0
            # A if-elif-else selection construct is used here as there are three options
            # If option is '1', order based on the 'points'
            if order == 1:
                iVal = teams[index[i]]["points"]
                jVal = teams[index[j]]["points"]
            # if option is '2', order based on 'goal difference'
            elif order == 2:
                # Calculate the goal difference for team 'i' and team 'j'
                iVal = teams[index[i]]["gs"] - teams[index[i]]["gc"]
                jVal = teams[index[j]]["gs"] - teams[index[j]]["gc"]
            # Else, the order is '3' and ordered based on games 'won'
            else:
                iVal = teams[index[i]]["won"]
                jVal = teams[index[j]]["won"]
            
            # A simple 'if' selection statement is used here as there is only one selective code block
            # if the value for team 'i' is less than the value for team 'j'
            if iVal < jVal:
                # Swap the index values at indexes 'i' and 'j'
                index[i], index[j] = index[j], index[i]
    
    # Return the re-ordered list
    return index





############################################################
# Function: displayTable                                   #
############################################################
# Description                                              #
#                                                          #
############################################################
# Parameters: index is the order the teams should be       #
#             displayed in                                 #
############################################################
# Return Value: No return value                            #
#                                                          #
############################################################
def displayTable(index):
    print("---------------------------------------------------------------------")
    print("Team Name        | Games Played |  Points  |  Goal Difference  |  Games Won |")
    print("----------------------------------------------------------------------")
    for j in range(len(teams)):
        
        team = teams[index[j]]['name']
        play = teams[index[j]]['played']
        point = teams[index[j]]['points']
        gd = int(teams[index[j]]['gs'])-int(teams[index[j]]['gc'])
        won = teams[index[j]]['won']
        print(team.split(':')[1]+"("+team.split(':')[0]+")","     | \t ",play,"  \t |    ",point,"   | \t   ",gd,"  \t|     ",won,"    |  " )
        print("---------------------------------------------------------------------")
       

    
################
# Main Section #
################

# Call the setupResetTeams() function to initialise the 'teams' dictionary of dictionaries
setupResetTeams()

# Your 'games' processing code goes here...


# Create an initial index from 1 to number of teams
teamOrder = [x for x in range(1, len(teams) + 1)]
# Sort index based on games 'won'
teamOrder = sortTeams(teamOrder, 3)
# Sort index based on 'goal difference'
teamOrder = sortTeams(teamOrder, 2)
# Sort index based on 'points'
teamOrder = sortTeams(teamOrder, 1)



# Call the displayTable function to display the league table









menu = {}
menu['1']="View League Table" 
menu['2']="Manage Games"

menu['3']="Exit"
while True: 
    options=menu.keys()
    sorted(options)
    for entry in options: 
        print (entry, menu[entry])

    selection=input("Please Select:") 
    if selection =='1':
        displayTable(sortTeams(teamOrder, 1))
    elif selection == '2': 
        game = {}
        game['1']="Add Game Result" 
        game['2']="Edit Game Result"
        game['B']="Back to Main Menu"
        options=game.keys()
        sorted(options)
        for entry in options: 
            print (entry, game[entry])
        selection=input("Please Enter your choice:")
        if selection=='2':
            
            home = input('Enter home team id[1-5] : ')
            
            if int(home) >= 1 and int(home)<=5:
                away = input('Enter away team id[1-5] : ')
                if int(away) >=1 and int(away)<=5:
                    if int(home)!=int(away):
                        status = 0
                        index = 0
                        for i in range(len(games)):
                                game=games[i][0]
                                new_game=str(home)+":"+str(away)
                                if game==new_game:
                                    status = 1
                                    index=i
                        if status==1:
                            change_id = input('Do you want to change the ID Y/N : ')
                            if change_id == 'Y' or change_id == 'y':
                                e_home = input("Enter new home ID")
                                if int(e_home) >= 1 and int(e_home)<=5:
                                  e_away = input('Enter away team id[1-5] : ')
                                  if int(e_away) >=1 and int(e_away)<=5:
                                      if int(e_away) != int(e_home):
                                        e_game=str(e_home)+":"+str(e_away)
                                        check = 0
                                        for j in range(len(games)):
                                            egame=games[j][0]
                                            if egame == e_game:
                                                check=1
                                        if check == 1:
                                            print("The fixtures already exist")
                                        else:  
                                            games[index][0]=e_game
                                            with open("games.dat", "w") as txt_file:
                                                for line in games:
                                                    txt_file.write(line[0]+","+line[1] + "\n")
                                            print(games)
                                      else:
                                          print("Home and away ID cannot be the same")
                                  else:
                                      print("Enter valid away id")
                                else:
                                    print("Enter Valid home ID")
                            else:
                                change_score = input('Do you want to change the score Y/N : ')
                                if change_score == 'Y' or change_score == 'y':
                                    
                                    eh_res = input("Input home score : ")
                                    if int(eh_res)>=0:
                                        ea_res = input("Input aways score : ")
                                        if int(ea_res)>=0:
                                                enew_res=str(eh_res)+":"+str(ea_res)
                                                games[index][1]=enew_res
                                                with open("games.dat", "w") as txt_file:
                                                    for line in games:
                                                        txt_file.write(line[0]+","+line[1] + "\n")
                                                print(games)
                                        else:
                                            print("Score should be a non negative number")
                                    else:
                                        print("Score should be a non negative number")
                                else:
                                    print("No changes made on result")
                        else:
                            print('The Game does not exist')
                    else:
                        print("A team cannot play against itself")

                else:
                    print("Away ID should be between 0-5")   
                    
            else:
                print("Home ID should be between 0-5")
        if selection=='1':
                meet=[]
                home = input('Enter home team id[1-5] : ')
            
                if int(home) >= 1 and int(home)<=5:
                    away = input('Enter away team id[1-5] : ')
                    if int(away) >=1 and int(away)<=5:
                        if int(home)!=int(away):
                            status = 0
                    
                            for i in range(len(games)):
                                    game=games[i][0]
                                    new_game=str(home)+":"+str(away)
                                    if game==new_game:
                                        status = 1
                            if status==0:
                                new_game=str(home)+":"+str(away)
                                meet.append(new_game)
                                h_res = input("Input home score : ")
                                if int(h_res)>=0:
                                    a_res = input("Input aways score : ")
                                    if int(a_res)>=0:
                                            new_res=str(h_res)+":"+str(a_res)
                                            meet.append(new_res)
                                            with open("games.dat", "a") as txt_file:
                                                    txt_file.write("\n"+meet[0]+","+meet[1] )

                                            print(games)
                                    else:
                                        print("Score should be a non negative number")
                                else:
                                    print("Score should be a non negative number")
                            else:
                                print("This teams have already meat")
                        else:
                            print("A team cannot play against itself")

                    else:
                        print("Away ID should be between 0-5")   
                        
                else:
                    print("Home ID should be between 0-5")
                
               
    elif selection == '3':
        exit=input("Are you sure you want to quit Y/N : ")
        if exit=='Y' or exit=='y':
             break
        elif exit=='N' or exit=='n':
             print('Back to main menu')
    else: 
        print ("Unknown Option Selected!" )