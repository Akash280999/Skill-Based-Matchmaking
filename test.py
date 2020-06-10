import unittest
import app

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = app.SBM()
        cls.obj.players_on_each_side = 2
        cls.obj.total_no_of_players = 6
        cls.obj.player_name_with_score = {'Akash': 57, 'Vikash': 83, 'Sonu': 43, 'Kartik': 67, 'Rishab': 99,
                                           'Rahul': 61}
        cls.obj.sorted_players = ['Rishab', 'Vikash', 'Kartik', 'Rahul', 'Akash', 'Sonu']
        cls.obj.teamA = [('Rishab', 'Vikash'), ('Rishab', 'Kartik'), ('Rishab', 'Rahul'), ('Rishab', 'Akash'), ('Rishab', 'Sonu'), ('Vikash', 'Kartik'), ('Vikash', 'Rahul'), ('Vikash', 'Akash'), ('Vikash', 'Sonu'), ('Kartik', 'Rahul'), ('Kartik', 'Akash'), ('Kartik', 'Sonu'), ('Rahul', 'Akash'), ('Rahul', 'Sonu'), ('Akash', 'Sonu')]
        cls.obj.teamB = [[('Kartik', 'Rahul'), ('Kartik', 'Akash'), ('Kartik', 'Sonu'), ('Rahul', 'Akash'), ('Rahul', 'Sonu'), ('Akash', 'Sonu')], [('Vikash', 'Rahul'), ('Vikash', 'Akash'), ('Vikash', 'Sonu'), ('Rahul', 'Akash'), ('Rahul', 'Sonu'), ('Akash', 'Sonu')], [('Vikash', 'Kartik'), ('Vikash', 'Akash'), ('Vikash', 'Sonu'), ('Kartik', 'Akash'), ('Kartik', 'Sonu'), ('Akash', 'Sonu')], [('Vikash', 'Kartik'), ('Vikash', 'Rahul'), ('Vikash', 'Sonu'), ('Kartik', 'Rahul'), ('Kartik', 'Sonu'), ('Rahul', 'Sonu')], [('Vikash', 'Kartik'), ('Vikash', 'Rahul'), ('Vikash', 'Akash'), ('Kartik', 'Rahul'), ('Kartik', 'Akash'), ('Rahul', 'Akash')], [('Rishab', 'Rahul'), ('Rishab', 'Akash'), ('Rishab', 'Sonu'), ('Rahul', 'Akash'), ('Rahul', 'Sonu'), ('Akash', 'Sonu')], [('Rishab', 'Kartik'), ('Rishab', 'Akash'), ('Rishab', 'Sonu'), ('Kartik', 'Akash'), ('Kartik', 'Sonu'), ('Akash', 'Sonu')], [('Rishab', 'Kartik'), ('Rishab', 'Rahul'), ('Rishab', 'Sonu'), ('Kartik', 'Rahul'), ('Kartik', 'Sonu'), ('Rahul', 'Sonu')], [('Rishab', 'Kartik'), ('Rishab', 'Rahul'), ('Rishab', 'Akash'), ('Kartik', 'Rahul'), ('Kartik', 'Akash'), ('Rahul', 'Akash')], [('Rishab', 'Vikash'), ('Rishab', 'Akash'), ('Rishab', 'Sonu'), ('Vikash', 'Akash'), ('Vikash', 'Sonu'), ('Akash', 'Sonu')], [('Rishab', 'Vikash'), ('Rishab', 'Rahul'), ('Rishab', 'Sonu'), ('Vikash', 'Rahul'), ('Vikash', 'Sonu'), ('Rahul', 'Sonu')], [('Rishab', 'Vikash'), ('Rishab', 'Rahul'), ('Rishab', 'Akash'), ('Vikash', 'Rahul'), ('Vikash', 'Akash'), ('Rahul', 'Akash')], [('Rishab', 'Vikash'), ('Rishab', 'Kartik'), ('Rishab', 'Sonu'), ('Vikash', 'Kartik'), ('Vikash', 'Sonu'), ('Kartik', 'Sonu')], [('Rishab', 'Vikash'), ('Rishab', 'Kartik'), ('Rishab', 'Akash'), ('Vikash', 'Kartik'), ('Vikash', 'Akash'), ('Kartik', 'Akash')], [('Rishab', 'Vikash'), ('Rishab', 'Kartik'), ('Rishab', 'Rahul'), ('Vikash', 'Kartik'), ('Vikash', 'Rahul'), ('Kartik', 'Rahul')]]

    def test_take_input(self):
        # for this test case user need to provide input
        # leave the input of the name blank at any point of time
        self.obj.player_name_with_score.clear()
        self.assertRaises(TypeError, self.obj.takeinput())

    def test_take_input_no_of_players(self):
        # for this test case user need to provide input
        # Enter the the details as usual and leave blank for end of input
        self.obj.player_name_with_score.clear()
        self.assertEqual(self.obj.takeinput(), (self.obj.total_no_of_players, self.obj.player_name_with_score))
        print("Total no of players =", self.obj.total_no_of_players)
        print("Player name with score dictionary :", self.obj.player_name_with_score)

    def test_output(self):
        # checks the sorted list of players w.r.t. scores (best to worst)
        self.obj.sorted_players.clear()
        self.assertEqual(self.obj.output(), ['Rishab', 'Vikash', 'Kartik', 'Rahul', 'Akash', 'Sonu'])

    def test_output_2(self):
        self.obj.player_name_with_score.clear()
        # if any user has invalid score or any string
        self.obj.player_name_with_score = {'Akash': None, 'Vikash': 83, 'Sonu': 43, 'Kartik': 67, 'Rishab': 99,
                                          'Rahul': 61}
        self.assertRaises(TypeError, self.obj.output())

        self.obj.player_name_with_score.clear()
        self.obj.player_name_with_score = {'Akash': "ok", 'Vikash': 83, 'Sonu': 43, 'Kartik': 67, 'Rishab': 99,
                                           'Rahul': 61}
        self.assertRaises(TypeError, self.obj.output())

    def test_create_team(self):
        # if number of players is less than players on each side
        self.obj.players_on_each_side = 3
        self.obj.total_no_of_players = 2
        self.assertRaises(Exception, self.obj.create_team())

        # if number of players is odd
        self.obj.total_no_of_players = 5
        self.assertRaises(Exception, self.obj.create_team())

    def test_create_team_2(self):
        # teamA and teamB has all the repeating teams at this point of time
        self.assertEqual(self.obj.create_team(), (self.obj.teamA, self.obj.teamB))
        print("Team A =", self.obj.teamA)
        print("Team B = ", end="")
        for i in self.obj.teamB:
            print(str(i) + "\t")

    def test_form_matches(self):
        # self.matches = {('Rishab', 'Vikash'): ('Akash', 'Sonu'), ('Rishab', 'Kartik'): ('Akash', 'Sonu'), ('Rishab', 'Rahul'): ('Akash', 'Sonu'), ('Rishab', 'Akash'): ('Rahul', 'Sonu'), ('Rishab', 'Sonu'): ('Rahul', 'Akash'), ('Vikash', 'Kartik'): ('Akash', 'Sonu'), ('Vikash', 'Rahul'): ('Akash', 'Sonu'), ('Vikash', 'Akash'): ('Rahul', 'Sonu'), ('Vikash', 'Sonu'): ('Rahul', 'Akash'), ('Kartik', 'Rahul'): ('Akash', 'Sonu'), ('Kartik', 'Akash'): ('Rahul', 'Sonu'), ('Kartik', 'Sonu'): ('Rahul', 'Akash'), ('Rahul', 'Akash'): ('Kartik', 'Sonu'), ('Rahul', 'Sonu'): ('Kartik', 'Akash'), ('Akash', 'Sonu'): ('Kartik', 'Rahul')}
        # got the value after executing lines 52 - 56 in app.py
        # contains all repeating matches of members who already played together with same opponent team

        # function returns a dictionary of match number and its quality (closeness of two scores of two teams in a match)
        self.assertEqual(self.obj.form_matches(), {'Match 1': 41.0, 'Match 2': 33.0, 'Match 3': 30.0, 'Match 4': 26.0, 'Match 5': 12.0, 'Match 6': 25.0, 'Match 7': 22.0, 'Match 8': 18.0, 'Match 9': 4.0, 'Match 10': 14.0, 'Match 11': 10.0, 'Match 12': 4.0})

        # self.matches = {('Rishab', 'Vikash'): ('Akash', 'Sonu'), ('Rishab', 'Kartik'): ('Akash', 'Sonu'), ('Rishab', 'Rahul'): ('Akash', 'Sonu'), ('Rishab', 'Akash'): ('Rahul', 'Sonu'), ('Rishab', 'Sonu'): ('Rahul', 'Akash'), ('Vikash', 'Kartik'): ('Akash', 'Sonu'), ('Vikash', 'Rahul'): ('Akash', 'Sonu'), ('Vikash', 'Akash'): ('Rahul', 'Sonu'), ('Vikash', 'Sonu'): ('Rahul', 'Akash'), ('Kartik', 'Rahul'): ('Akash', 'Sonu'), ('Kartik', 'Akash'): ('Rahul', 'Sonu'), ('Kartik', 'Sonu'): ('Rahul', 'Akash')}
        # got the value after executing lines 64 - 69 in app.py
        # after removing all repeating matches of members who already played together with same opponent team

    def test_find_average_score(self):
        # should pass number of players as parameters == players_on_each_side
        self.obj.players_on_each_side = 2
        self.assertEqual(self.obj.find_average_score(('Kartik', 'Sonu')), 55.0)

        self.obj.players_on_each_side = 3
        self.assertEqual(self.obj.find_average_score(('Kartik', 'Sonu', 'Rahul')), 57.0)


if __name__ == '__main__':
    unittest.main()
