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

    def problem_eight(self, number):
        number_block = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
        largest_product = 0
        for i in range(1, 988):
            product = 1
            for x in range(0, number):
                product = product * int(number_block[i+x])
            if product > largest_product:
                largest_product = product
        return largest_product

    def problem_nine(self):
        for c in range(1, 1000):
            for a in range(1, c):
                b = (c**2 - a**2)**(.5)
                if (a**2 + b**2 == c**2) and a + b +c == 1000:
                    return a*b*c








