import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		input = "1 1 +"
		result = rpn.calculate(input)
		print("Testing add")
		print(input)
		print(result)
		self.assertEqual(2, result)
	def test_multiply(self):
		input = "3 4 *"
		result = rpn.calculate(input)
		print("Testing multiply")
		print(input)
		print(result)
		self.assertEqual(12, result)
	def test_subtract(self):
		input = "5 3 -"
		result = rpn.calculate(input)
		print("Testing subtract")
		print(input)
		print(result)
		self.assertEqual(2, result)
	def test_toomanythings(self):
		input = "1 2 3 +"
		print("Testing invalid input")
		print(input)
		with self.assertRaises(TypeError):
			rpn.calculate(input)
	def test_divide(self):
		input = "6 2 /"
		result = rpn.calculate(input)
		print("Testing divide")
		print(input)
		print(result)
		self.assertEqual(3, result)
	def test_exponent(self):
		input = "2 3 ^"
		result = rpn.calculate(input)
		print("Testing exponent")
		print(input)
		print(result)
		self.assertEqual(8, result)
