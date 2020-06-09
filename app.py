# Program for Skill based Matchmaking

# function to print the players in sorted order of scores
def output(player_name_with_score):
    print("Sorted List of players (best to worst):")
    print("_________________")
    print("Player name\t| Score")
    for i in sorted(player_name_with_score.items(), reverse=True):
        print(i[0] + "\t|" + str(i[1]))
    print("-----------------")


# function to take inputs
def takeinput():
    try:
        m = int(input("Enter number of players on each side: "))
        player_name_with_score = {}
        print("Enter " + str(m * m) + " players names with their score")
        count = 1
        while True:
            if (count > (m * m)):
                break

            name = input("Name of player " + str(count) + ": ")
            score = int(input("Score: "))
            if (name == ""):
                print("Enter all player name to proceed.")
                break
            player_name_with_score[name] = score
            count += 1
        return m, m * m, player_name_with_score
    except Exception:
        print("Error encountered while taking values")


# driver program
if __name__ == "__main__":
    try:
        players_on_each_side, total_no_of_players, player_name_with_score = takeinput()
        output(player_name_with_score)
    except Exception:
        print("Error encountered in driver program")
