class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


'''•	Test if the worker is initialized with the correct name, salary, and energy
•	Test if the worker's energy is incremented after the rest method is called
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called	
•	Test if the get_info method returns the proper string with correct values
'''
import unittest

class WorkerTests(unittest.TestCase):
    
    def setUp(self) -> None:
        self.worker = Worker('Ivo', 8000, 10)
        
    def test_if_worker_init_correct(self):
        
        result = [x for x in (self.worker.name, self.worker.salary, self.worker.energy)]
        expected_result = ['Ivo', 8000, 10]
        
        self.assertListEqual(result, expected_result)
        
        
    
    def test_energy_is_incremented_after_rest(self):
        
        self.worker.rest()
        result = self.worker.energy
        excepted_result = 11
        
        self.assertEqual(result, excepted_result)
        
    def test_working_with_0_or_less_energy(self):
        
        with self.assertRaises(Exception) as context:
            self.worker.energy = 0
            self.worker.work()
        
        expected = 'Not enough energy.'
        
        self.assertEqual(str(context.exception), expected)
        
    def test_is_worker_salary_increased_after_working(self):
        
        self.worker.work()
        result = self.worker.money
        expected_result  = self.worker.salary
        
        self.assertEqual(result, expected_result)
    
    def test_is_energy_decreased_after_work(self):
        
        self.worker.energy = 10
        self.worker.work()
        result = self.worker.energy
        expected_result = 9
        
        self.assertEqual(result, expected_result)
    
    def test_is_get_info_working_correctly(self):
        
        self.worker.money = 1000
        result = self.worker.get_info()
        expected = 'Ivo has saved 1000 money.'
        
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

