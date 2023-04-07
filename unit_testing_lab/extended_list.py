class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)
    
    
import unittest

class IntegerListTests(unittest.TestCase):
        
        def setUp(self) -> None:
            self.int_list = IntegerList(1, 2, 3, 4, 5)
            
        def test_constructor(self):
            
            result = self.int_list.get_data()
            expected = [1, 2, 3, 4, 5]
            
            self.assertListEqual(result, expected)
        
        def test_if_add_returns_corect(self):
            
            result = self.int_list.add(6)
            expected = [1, 2, 3, 4, 5, 6]
            
            self.assertListEqual(result, expected)
            
        def test_if_add_raises_an_error_if_val_not_int(self):
            
            with self.assertRaises(Exception) as context:
                self.int_list.add("foo")
                
            result = str(context.exception)
            expected = "Element is not Integer"
            
            self.assertEqual(result, expected)
            
        def test_if_remove_index_works_correctly(self):
            
            result = self.int_list.remove_index(0)
            expected = 1
            
            self.assertEqual(result,  expected)
            
        def test_if_get_works_correctly(self):
            
            result = self.int_list.get(1)
            expected = 2
            
            self.assertEqual(result, expected)
                
        def test_if_error_is_raised_when_get_index_out_of_range(self):
            
            with self.assertRaises(Exception) as context:
                self.int_list.get(len(self.int_list.get_data()) + 2)
            
            result = str(context.exception) 
            expected = "Index is out of range"
            self.assertEqual(result, expected)
            
        def test_if_insert_works_correctly(self):
            
            self.int_list.insert(2, 0)
            result = self.int_list.get(2)
            expected = 0
            
            self.assertEqual(result, expected)
            
        def test_when_insert_index_is_out_of_range(self):
            
            with self.assertRaises(Exception) as context:
                self.int_list.insert(len(self.int_list.get_data()) + 2, 0)
                
            result = str(context.exception)
            expected = "Index is out of range"
            
            self.assertEqual(result, expected)
            
        def test_when_insert_val_is_not_int(self):
            
            with self.assertRaises(Exception) as context:
                self.int_list.insert(0, 'foo')
                
            result = str(context.exception)
            expected = "Element is not Integer"
            
            self.assertEqual(result, expected)
            
        
        def test_get_biggest(self):
            
            expected = max(self.int_list.get_data())
            result = self.int_list.get_biggest()
            
            self.assertEqual(result, expected)
            
        def test_get_index(self):
            
            expected = 1
            result = self.int_list.get_index(2)
            
            self.assertEqual(result, expected)
            
            
            

if __name__ == '__main__':
    unittest.main()