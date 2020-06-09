# Program for Skill based Matchmaking

# function to take inputs
def takeinput():
    m = int(input("Enter number of players on each side: "))
    player_name_with_score = {}
    print("Enter " + str(m * m) + " players names with their score")
    count = 1
    while True:
        if (count > (m * m)):
            break

        name = input("Name of player " + str(count) + ": ")
        score = int(input("Score: "))
        if (name == "" and score == ""):
            break
        elif (name == "" or score == ""):
            print("Enter all player values to proceed.")
            break

        player_name_with_score[name]=score
        count += 1
    return m, m * m,player_name_with_score

# driver program
if __name__ == "__main__":
    players_on_each_side, total_no_of_players, player_name_with_score = takeinput()
    print(players_on_each_side, total_no_of_players)
    print(player_name_with_score)
