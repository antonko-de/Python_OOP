from project.toy_store import ToyStore
from unittest import TestCase, main



class ToyStoreTests(TestCase):
    
    def setUp(self) -> None:
        self.toy_store = ToyStore()
        
    def test_init(self):
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })
    
    def test_add_toy_when_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("H", "Toy")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")
        
    def test_add_toy_when_toy_is_already_in_shelf(self):
        self.toy_store.add_toy("A", "Toy")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Toy")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")
        
    def test_add_toy_when_shelf_is_already_taken(self):
        self.toy_store.add_toy("A", "Toy")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Toy2")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")
    
    def test_add_toy_when_shelf_is_not_taken_and_toy_is_not_in_shelf(self):
        result = self.toy_store.add_toy("A", "Toy")
        self.assertEqual(result, "Toy:Toy placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": "Toy",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })
    
    def test_remove_toy_when_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("H", "Toy")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")
        
    
    def test_remove_toy_when_toy_in_that_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Toy")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")
        
    def test_remove_toy_when_toy_in_that_shelf_exists(self):
        self.toy_store.add_toy("A", "Toy")
        result = self.toy_store.remove_toy("A", "Toy")
        self.assertEqual(result, "Remove toy:Toy successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })
if __name__ == '__main__':
    main()