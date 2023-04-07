class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


'''
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping
'''

import unittest

class CatTests(unittest.TestCase):
    
    def setUp(self) -> None:
      self.cat = Cat('Angel')
      
    
    def test_cat_size_increased_after_eating(self):
        
        self.cat.eat()
        result = self.cat.size
        expected  = 1
        
        self.assertEqual(result, expected)
        
    def test_is_cat_fed_after_eating(self):
        
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        
    def test_if_cat_cannot_eat_after_fed(self):
        
        self.cat.eat()
        
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        
        expected = 'Already fed.'
            
        self.assertEqual(str(context.exception), expected)
    
    def test_if_cat_cannot_sleep_if_not_fed(self):
        
        self.cat.fed = False
        
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        
        result = str(context.exception)
        expected = 'Cannot sleep while hungry'
        
        self.assertEqual(result,expected)
        
    def test_if_cat_not_sleepy_after_eating(self):
        self.cat.eat()
        self.cat.sleep()
        
        self.assertFalse(self.cat.sleepy)
        

if __name__ == '__main__':
    unittest.main()