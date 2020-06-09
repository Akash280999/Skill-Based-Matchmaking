#Program for Skill based Matchmaking

#function to take inputs
def Takeinput():
    m = int(input("Number of players on each side: "))
    return m,m*m

#driver program
if __name__ == "__main__":
    players_on_each_side, total_no_of_players = Takeinput()
    print(players_on_each_side,total_no_of_players)
