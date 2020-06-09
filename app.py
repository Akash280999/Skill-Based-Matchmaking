# Program for Skill based Matchmaking

import itertools    #for iterating and creating combinations

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
            print("_" * 30)
            print('{:15} ==> {:>10}'.format("Player name", "Score"))
            print("-" * 30)
            for name, score in sorted(self.player_name_with_score.items(), key=lambda item: item[1], reverse=True):
                print('{:15} ==> {:10d}'.format(name, score))
            print("-" * 30)
        except Exception as e:
            print("Error encountered in output() function")
            print(e)
            exit()

    #function to create teams for the match
    def create_team(self):
        # empty_list = self.player_name_with_score.keys()
        # print(list(itertools.combinations(empty_list, self.players_on_each_side)))
        pass

    # function to take inputs
    def takeinput(self):

        self.players_on_each_side = int(input("Enter number of players on each side: "))
        # **** Leave the player name blank when you are done adding player ****
        print("Enter player names with their score")
        self.total_no_of_players=1

        while True:
            try:
                name = input("Name of player " + str(self.total_no_of_players) + ": ")
                if name == "":
                    break
                score = int(input("Score: "))
                self.player_name_with_score[name] = score
                self.total_no_of_players += 1
            except Exception as e:
                print("Error encountered while taking values")
                print(e)
                exit()

# driver program
if __name__ == "__main__":
    try:
        obj = SBM()
        obj.takeinput()
        obj.output()
        obj.create_team()
    except Exception as e:
        print("Error encountered in driver program")
        print(e)
        exit()
