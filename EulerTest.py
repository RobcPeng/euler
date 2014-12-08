import unittest
from Euler import Euler

class EulerTest(unittest.TestCase):

	euler_object = Euler()

	def test_problem_one(self):
		self.assertEqual(self.euler_object.problem_one(999), 233168)

	def test_problem_two(self):
		self.assertEqual(self.euler_object.problem_two(4000000),4613732)
"""
	def test_problem_three(self):
		self.assertEqual(self.euler_object.problem_three(600851475143),0)
"""
	def test_is_number_palidrome(self):
		self.assertEqual(self.euler_object.is_number_palidrome(1001), True)

if __name__ == '__main__':
	unittest.main()