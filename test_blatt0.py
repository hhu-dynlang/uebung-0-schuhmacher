from blatt0 import pascal_array
from blatt0 import flatten
from blatt0 import fizz_buzz
from blatt0 import solve_equation
from blatt0 import myint, mybin
from blatt0 import is_palindrome;
import random

def test_is_palindrome():
    input = "lagerregal"
    assert is_palindrome(input) == True

def test_is_not_palindrome():
    input = "blabla"
    assert is_palindrome(input) == False

def test_pascal_5():
    assert pascal_array(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def test_pascal_1():
    assert pascal_array(1) == [[1]]

def test_flatten():
    assert flatten([[1, 'a'], [4,[567,['frt', 'g']]], 7]) == [1, 'a', 4, 567, 'frt', 'g', 7]

def test_flatten_already_flat():
    assert flatten([1,2,3,4,5,6]) == [1,2,3,4,5,6]

def test_fizz_buzz():
    assert fizz_buzz(20) == [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',13,14,'FizzBuzz',16,17,'Fizz',19,'Buzz']

def test_solve_equation():
    assert solve_equation(2, 3, 1) == -0.5

def test_int_to_bin():
    input = random.sample(range(1000), 10)
    for x in input:
        assert mybin(x) == bin(x)

def test_bin_to_int():
    input = [(i, bin(i)) for i in random.sample(range(1000), 10)]
    for i, bini in input:
        assert myint(bini) == i
