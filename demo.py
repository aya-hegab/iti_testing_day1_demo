"""
Unit testing: we are also say component testing.

Test case:
smallest unit of testing
assert methods to check for actions ad responses

Test Suite:
collection of multiple tests or test cases

Test Report
a full report contains the failure or succeeded

ex: Senario 
your company is hired by a bank to develop online banking application
#  requirement analysis

1- Login valid credentials
2- deposit
3- withdraw
4- transfer


1-> login component
login id & password

test cases:
1- enter valid ID & password -> happy senario case
2- enter invalid id & password
3- empty login ID & click login

Adv unit testing
1- developers looking to learn what functionality is provided by a unit 
    and how to use it can look at the unit tests to gain a basic understanding of the unit API.

unit testing allows the programmer to refactor code at a later date,


Unit Testing Disadvantages
1- unit testing can't be expected to catch every error in a program.
 it is not possible to evaluate all execution pathes even in the most trivial program

unittest

the unittest framework produce 3 possible outputs:- OK, FAILED, and ERROR

OK: when all the tests pass

FAILED: When an AssertionError exception is raised (assertion is unseccful), the output FAILED

ERROR: When ALL the test cases did not pass and it raises an excption other than Assertion

"""

import unittest

# assert 3*8 == 24, "should be 24"

# def test_case_multiply_1():
#     assert 5*10 == 50, "should be 50"

# def test_case_multiply_2():
#     assert 5*11 == 5, "should be 55"

# def test_case_multiply_3():
#     assert 5*12 == 60, "should be 60"

# test_case_multiply_1()
# test_case_multiply_2()
# test_case_multiply_3()

# class myTestCases(unittest.TestCase):
#     def test_one(self):
#         self.assertTrue(100 > 99, 'should be true')

#     def test_two(self):
        # self.assertEqual(40+60,100, "should be 100")
    
#     def test_upper(self):
#         self.assertEqual('iti'.upper(), "ITI")

#     def test_isupper(self):
#         self.assertTrue('ITI'.isupper())
#         self.assertFalse('ITI'.islower())

# if __name__ == "__main__":
#     unittest.main()

# class calc:
#     def add(x,y):
#         return x+y
    
#     def subtract(x,y):
#         return x-y
    
#     def multiple(x,y):
#         return x*y
    
#     def divide(x,y):
#         if y==0:
#             raise ValueError("Can't divide by zero!")
#         return x/y

class Rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width*self.height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        rectangle = Rectangle(3,3)
        self.assertEqual(rectangle.get_area(),6, 'Inncorrect area')

if __name__ == "__main__":
    unittest.main()
    
    
