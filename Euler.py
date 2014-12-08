from fractions import gcd
import functools

class Euler(object):

    def __init__(self, name=None):
        pass

    #sum of all numbers divisable by 3 and 5 up to number
    def problem_one(self, number):
        total_sum = 0
        while number > 0:
            if (number % 3 == 0) or (number % 5 == 0):
                total_sum += number
                number -= 1
            else:
                number -= 1
        return total_sum

    #fib sum of evens up to a certain number
    def problem_two(self, number):
        start_number = 1
        current_number = 1
        sum_of_all_even = 0
        while current_number < number:
            if current_number % 2 == 0:
                sum_of_all_even += current_number
            current_number = current_number + start_number
            start_number = current_number - start_number
        return sum_of_all_even

    #largest palidrome that is created through
    #the product of two three digit numbers
    def problem_four(self):
        max_palidrome = 0
        for x in range(100, 999):
            for y in range(100, 999):
                if self.is_number_palidrome(x * y) and (x * y) > max_palidrome:
                    max_palidrome = x * y
        return max_palidrome

    def is_number_palidrome(self, number):
        return str(number) == str(number)[::-1]

    #smallest even multiple of all numbers up to number
    def problem_five(self, number):
        lcm = lambda x, y: x * y // gcd(x, y)
        current_even_multiple = 1
        for num in range(1, number):
            current_even_multiple = lcm(current_even_multiple, num)
        return current_even_multiple

    #sum square difference
    def problem_six(self, number):
        sum_of_squares = functools.reduce(lambda x, y: x + y**2, range(1, number + 1))
        squares_of_sums = (functools.reduce(lambda x, y: x + y, range(1, number + 1)))**2
        return squares_of_sums - sum_of_squares





