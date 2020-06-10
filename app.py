# Program for Skill based Matchmaking

import itertools  # standard library for iterating and creating combinations or permutations

# class for performing OOPs concepts
class SBM(object):

    # constructor for pre initialization
    def __init__(self):
        self.player_name_with_score = {}        # stores player name as key and score as values
        self.players_on_each_side = 0           # given by user
        self.total_no_of_players = 0            # incremented each time user provides input and until blank encountered
        self.teamA = []
        self.teamB = []
        self.matches = {}                       # stores all possible matches including repeatations
        self.sorted_players = []                # creates a copy of sorted players best to worst
        self.difference_score = {}              # for checking quality of matches

    # function to print the players in sorted order of scores
    def output(self):
        try:
            print("Sorted List of players (best to worst):")
            print("_" * 30)
            print('{:15} ==> {:>10}'.format("Player name", "Score"))
            print("-" * 30)
            for name, score in sorted(self.player_name_with_score.items(), key=lambda item: item[1],
                                      reverse=True):            # sorting the list of players using score from best to low  # returns a list of tuples
                print('{:15} ==> {:10d}'.format(name, score))
                self.sorted_players.append(name)
            print("-" * 30)
            return self.sorted_players
        except Exception as e:
            print("Error encountered in output() function")
            print(e)

    # function to find the average scores for each team in every match
    def find_average_score(self,team):
        try:
            sum = 0
            for player in team:
                score = self.player_name_with_score[player]
                sum += score
            avg = sum / self.players_on_each_side
            return avg
        except Exception as e:
            print("Error encountered in find_average_score() function")
            print(e)

    # function to create the matches with no repeatation of previous played matches
    def form_matches(self):
        try:
            j = 0
            while j < len(self.teamA):      # stores all the possible matches for future removal of repeating matches
                for lines_teamB in self.teamB[j]:
                    self.matches[self.teamA[j]] = lines_teamB       # storing all possible teams of A as a key and all possible teams of B as value
                j += 1

            self.teamA = []
            self.teamB = []

            self.teamA = list(self.matches.keys())
            self.teamB = list(self.matches.values())

            for key in self.teamA:  # removes duplicate matches of repeating teams which already played before as opponent
                if key in self.teamB:              # if team A of any match found in TeamB then store the index and delete it from teamB as well as from matches
                    index = self.teamB.index(key)
                    del self.matches[self.teamA[index]]
                    del self.teamA[index]
                    del self.teamB[index]

            print("Matches played:")
            j = 0
            while j < len(self.teamA):
                avg1 = self.find_average_score(self.teamA[j])       # calculates average score of teamA
                avg2 = self.find_average_score(self.teamB[j])       # calculates average score of teamB
                print("Match " + str(j + 1) + ": " + str(self.teamA[j]) + " " + str(avg1) + "  vs  " + str(self.teamB[j]) + " " + str(avg2))
                diff = avg1 - avg2
                self.difference_score["Match " + str(j+1)] = abs(diff)      # storing the difference as values for checking the quality of a match
                j += 1
        except Exception as e:
            print("Error encountered in form_matches() function")
            print(e)

    # function to create teams for the match
    def create_team(self):
        try:
            # check if teams can be formed or not
            # if no of players are odd then equal teams cannot be formed
            # if no of players if less than the players on each side of the teams => teams can't be formed
            if (self.total_no_of_players % 2 == 0) and (self.total_no_of_players > self.players_on_each_side):
                values = list(
                    itertools.combinations(self.sorted_players, self.players_on_each_side)
                )  # makes different combinations of all team players along with equal players on each side

                for i in range(len(values)):  # loop finds opponent team members
                    emp = []                  # stores all the opponent teams to be played with; matches with the player in each index in "values"
                    j = -1                    # started with -1 because it increments as soon as it enters the loop
                    while j < len(values) - 1:      # iterate and exclude the team playing in team A while adding the rest of the players
                        j += 1
                        if j == i:
                            self.teamA.append(values[i])
                            continue
                        flag = 0
                        for value in values[i]:  # for excluding the player if present in the tuple
                            if value not in values[j]:  # if all the current players not found in rest of the teams then increment else decrement
                                flag += 1
                            else:
                                flag -= 1
                        if flag == self.players_on_each_side:  # if all the players in team A which are currently playing are not present in rest of the combination of teams then append
                                                               # flag value increments till the value of players of each side
                            emp.append(values[j])
                    self.teamB.append(emp)              # finally append all the possible opponent players in teamB which maps the index of each players in local variable "values"
                                                        # stores list of list
            else:
                if self.total_no_of_players >= self.players_on_each_side:
                    print("Number of players should be more than the no of team members. Cannot make teams")
                else:
                    print("Odd no of players. Cannot make teams")
                raise Exception
        except Exception as e:
            print("Error encountered inside create_team()")
            print(e)

    # function to find the quality of each match which is the difference of scores of each team in every match and display in sorted order
    def quality_check(self):
        try:
            print("-" * 50)
            values = sorted(self.difference_score.items(), key=lambda item: item[1])        # sorting the dictionary and storing in local variable "values";
                                                                                            # returns a list of tuples
            print("Sorted Order of matches to be played based on quality:")
            for value in values[:len(values)-1]:        # leaving the last element for formatting
                print(value[0] + " , ", end="")
            print(values[len(values)-1][0])         # prints the last element
            print("-" * 50)
        except Exception as e:
            print("Error encountered in quality_check() function")
            print(e)

    # function to take inputs
    def takeinput(self):

        print(" **** Leave the player name blank when you are done adding player **** ")
        print("\nEnter player names with their score")
        self.total_no_of_players = 0

        while True:
            try:
                name = input("Name of player " + str(self.total_no_of_players + 1) + ": ")
                if name == "":            # stops taking any futher inputs when blank encountered and terminates the loop
                    print("\t\t\t********* End of input *********")
                    return self.total_no_of_players, self.player_name_with_score
                score = int(input("Score: "))
                self.player_name_with_score[name] = score
                self.total_no_of_players += 1              # counts the total players each time user gives input
            except Exception as e:
                print("Error encountered while taking values")
                print(e)

# driver program
if __name__ == "__main__":
    flag = True
    while flag:
        try:
            obj = SBM()
            # creating local copies of variables for testcases
            obj.players_on_each_side = int(input("Enter number of players on each side: "))
            total_no_of_players, player_name_with_score = obj.takeinput()
            sorted_players = obj.output()
            obj.create_team()
            obj.form_matches()
            obj.quality_check()
            inputt = input("Press 'Y' to exit or any other key to continue from beginning: ")
            if inputt in {'y', 'Y'}:
                flag = False
        except Exception as e:
            print("Error encountered in driver program. Program starts from beginning")
            print(e)
    else:
        print("\t\t\t********* Thank You *********")