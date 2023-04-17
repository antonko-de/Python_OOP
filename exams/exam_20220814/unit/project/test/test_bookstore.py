from project.bookstore import Bookstore
from unittest import TestCase, main

class BookstoreTests(TestCase):
    
    def setUp(self) -> None:
        self.bookstore = Bookstore(15)
        
    def test_init(self):
        self.assertEqual(self.bookstore.books_limit, 15)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        
    def test_book_limit_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = -1
        self.assertEqual(str(ex.exception), "Books limit of -1 is not valid")
        
    def test_len_method(self):
        self.bookstore.receive_book("Harry Potter", 5)
        self.assertEqual(len(self.bookstore), 5)
    
    def test_receive_book(self):
        self.assertEqual(self.bookstore.receive_book("Harry Potter", 5), "5 copies of Harry Potter are available in the bookstore.")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"Harry Potter": 5})
        
    def test_receive_book_if_not_enough_space(self):
        self.bookstore.receive_book("Harry Potter", 15)
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Harry Potter", 5)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")  

    def test_sell_book(self):
        self.bookstore.receive_book("Harry Potter", 5)
        self.assertEqual(self.bookstore.sell_book("Harry Potter", 3), "Sold 3 copies of Harry Potter")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"Harry Potter": 2})

    def test_sell_books_if_not_enough_copies(self):
        self.bookstore.receive_book("Harry Potter", 5)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Harry Potter", 6)
        self.assertEqual(str(ex.exception), "Harry Potter has not enough copies to sell. Left: 5")

    def test_sell_books_if_book_not_available(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Harry Potter", 6)
        self.assertEqual(str(ex.exception), "Book Harry Potter doesn't exist!")
        
        
    def test_total_sold_books(self):
        self.bookstore.receive_book("Harry Potter", 5)
        self.bookstore.sell_book("Harry Potter", 3) 
        self.assertEqual(self.bookstore.total_sold_books, 3)
    
if __name__ == '__main__':
    main()