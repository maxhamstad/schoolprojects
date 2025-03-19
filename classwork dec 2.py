def main():
    filename = 'Nov804.txt' 
    #filename = 'superbowl.txt'
    infile = open(filename, 'r')
    #to read in one line of
    team_names = infile.readline()
    
    #team_name_list = team_names.split()
    #team1 = team_name_list[0]
    #team2 = team_name_list[1]
    #one line of code for the syntax above
    
    team1, team2 = team_names.split()
    team1_score = 0
    team2_score = 0
    
    #read in all the remaining lines
    for line in infile:
        team_name, points = line.split()
        if team_name == team1:
            team1_score += int(points) #points was string, needs to be int
        elif team_name == team2:
            team2_score += int(points)
        else:
            raise Exception(f"{team_name} doesn't match one of our team names!")
        
        print(f"{team1}: {team1_score}, {team2}: {team2_score}")
    #we exit the loop when the file is done
    infile.close()
    print("Game over")
    if team1_score > team2_score:
        print(f"{team1} wins!")
    elif team2_score > team1_score:
        print(f"{team2} wins1")
    else:
        print("tie game?")
            
main()