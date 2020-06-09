# Program for Skill based Matchmaking

# class for performing OOPs concepts
class SBM:

    # constructor for pre initialization
    def __init__(self):
        self.player_name_with_score = {}
        self.players_on_each_side = 0
        self.total_no_of_players = 0

    # function to print the players in sorted order of scores
    def output(self):
        try:
            print("Sorted List of players (best to worst):")
            print("____________________")
            print("Player name | Score")
            print("--------------------")
            for i in sorted(self.player_name_with_score.items(), reverse=True):
                print(i[0] + " |" + str(i[1]))
            print("--------------------")
        except Exception:
            print("Error encountered in output() function")

    # function to take inputs
    def takeinput(self):
        try:
            self.players_on_each_side = int(input("Enter number of players on each side: "))
            self.total_no_of_players = self.players_on_each_side * self.players_on_each_side
            print("Enter " + str(self.total_no_of_players) + " players names with their score")
            count = 1
            while True:
                if count > self.total_no_of_players:
                    break

                name = input("Name of player " + str(count) + ": ")
                score = int(input("Score: "))
                if name == "":
                    print("Enter all player name to proceed.")
                    break
                self.player_name_with_score[name] = score
                count += 1
        except Exception:
            print("Error encountered while taking values")


# driver program
if __name__ == "__main__":
    try:
        obj = SBM()
        obj.takeinput()
        obj.output()
    except Exception:
        print("Error encountered in driver program")
