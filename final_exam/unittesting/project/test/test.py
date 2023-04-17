from project.tennis_player import TennisPlayer
from unittest import TestCase, main

class TennisPlayerTests(TestCase):
    
    def setUp(self) -> None:
        self.player = TennisPlayer('Daniel Morgan', 24, 10.00)
        
    
    def test_init(self):
        self.assertEqual(self.player.name, 'Daniel Morgan')
        self.assertEqual(self.player.age, 24)
        self.assertEqual(self.player.points, 10.00)
        self.assertEqual(self.player.wins, [])
               

    def test_name_setter(self):
        self.player.name = 'Daniel'
        self.assertEqual(self.player.name, 'Daniel')
        
    def test_name_setter_invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = 'a'
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")
    
    def test_name_setter_2_chars(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = 'as'
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!") 
   
    def test_age_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 17
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")
        
        self.player.age = 18
        self.assertEqual(self.player.age, 18)
        
    def test_add_new_win(self):
        self.player.add_new_win('Wimbledon')
        self.assertListEqual(self.player.wins, ['Wimbledon'])
        
    def test_add_new_win_already_added(self):
        self.player.add_new_win('Wimbledon')
        result =  self.player.add_new_win('Wimbledon')
        expected = "Wimbledon has been already added to the list of wins!"
        self.assertEqual(result, expected)
        
    def test_less_than(self):
       other_player = TennisPlayer('Pepi', 25, 15)
       result = self.player < other_player
       expected = 'Pepi is a top seeded player and he/she is better than Daniel Morgan'
       self.assertEqual(result, expected)
       
    def test_less_than_other_way(self):
         other_player = TennisPlayer('Pepi', 25, 5)
         result = self.player < other_player
         expected = 'Daniel Morgan is a better player than Pepi'
         self.assertEqual(result, expected)        
    
    def test_str(self):
        self.player.add_new_win('Wimbledon')
        self.player.add_new_win('US Open')
        self.assertEqual(str(self.player), 'Tennis Player: Daniel Morgan\nAge: 24\nPoints: 10.0\nTournaments won: Wimbledon, US Open')
        
    

if __name__ == "__main__":
    main()