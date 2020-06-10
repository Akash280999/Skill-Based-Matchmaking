import unittest
import app

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = app.SBM()

    def test_take_input(self):
        # for this test cases user need to provide input
        # leave the input of the name blank at any point of time
        self.assertRaises(TypeError, self.obj.takeinput())

    def test_take_input_no_of_players(self):
        # for this test cases user need to provide input
        # Enter the the details as usual and leave blank for end of input
        self.assertEqual(self.obj.takeinput(), (self.obj.total_no_of_players, self.obj.player_name_with_score))
        print("Total no of players =", self.obj.total_no_of_players)
        print("Player name with score dictionary :", self.obj.player_name_with_score)

    def test_output(self):
        # player_name_with_score dictionary is uninitialised
        pass

if __name__ == '__main__':
    unittest.main()
