import unittest
import app

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = app.SBM()
        cls.obj.players_on_each_side = 2
        cls.obj.player_name_with_score = {'Akash': 57, 'Vikash': 83, 'Sonu': 43, 'Kartik': 67, 'Rishab': 99,
                                           'Rahul': 61}

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
        # print(self.obj.player_name_with_score)
        pass

if __name__ == '__main__':
    unittest.main()
