class Euler(object):
	
	def __init__(self, name = None):
		pass

	def problem_one(self, number):
		total_sum = 0
		while number > 0:
			if (number % 3 == 0) or (number % 5 == 0):
				total_sum += number
				number -= 1
			else:
				number -= 1
		return total_sum

	def problem_two(self, number):
		start_number = 1
		current_number = 1
		sum_of_all_even = 0
		while current_number < number:
			if (current_number % 2 == 0):
				sum_of_all_even += current_number
			current_number = current_number + start_number
			start_number = current_number - start_number
		return sum_of_all_even

'''				
	def problem_three(self, number):
		current_factor = 1
		largest_prime_factor = 0
		while current_factor < (number / 2):
			print (largest_prime_factor)
			if (current_factor % 2 == 0) or (current_factor % 3 == 0):
				current_factor += 1
			elif (number % current_factor == 0):
				largest_prime_factor = current_factor
				current_factor += 1
			else:
				current_factor += 1
		return largest_prime_factor
'''

	def problem_four(self):
		pass

	def is_number_palidrome(self, number):
		return number.str() == number.str().reverse()

