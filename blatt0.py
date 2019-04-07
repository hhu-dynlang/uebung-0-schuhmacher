import math

def is_palindrome(s):
    if not isinstance(s, str):
        raise Exception('Input should be a string.')
    if len(s) % 2 == 1:
        return False
    length = int(len(s) / 2)
    for i in range(length):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

# s == s[::-1]
# is_palindrome(4) for exception

def pascal_array(n):
    if not isinstance(n, int):
        raise Exception('Input should be int.')
    if n < 1:
        raise Exception('Input should be larger than 0.')
    arr = []
    last_added = []
    for i in range(n):
        arr_to_add = []
        for j in range(i+1):
            if j-1 < 0 or j+1 > i:
                arr_to_add += [1]
            else:
                to_add = last_added[j-1] + last_added[j]
                arr_to_add += [to_add]
        arr += [arr_to_add]
        last_added = arr_to_add
    return arr
            
#def print_pascal(n):
#    arr = pascal_array(n)
#    spaces = n
#    for i in range(n):
#        for k in range(spaces):
#            print(' ', end='')
#        for j in range(i+1):
#            print(arr[i][j], end='')
#            print(' ', end='')
#        print()
#        spaces -= 1

#print_pascal(5)

def flatten(L):
    if not isinstance(L, list):
        raise Exception('Input should be a list.')
    New_L = []
    for i in range(len(L)):
        if isinstance(L[i], list):
            New_L += flatten(L[i])
        else:
            New_L += [L[i]]
    return New_L

#flatten(5)
#flatten('hallo')   both for exceptions

def solve_equation(a,b,c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        if not isinstance(a, float) or not isinstance(b, float) or not isinstance(c, float):
            raise Exception('Input must be numbers.')
    return (-b+math.sqrt(b*b-4*a*c))/(2*a)

#solve_equation(3,'A',5)

def fizz_buzz(n):
    if not isinstance(n, int):
        raise Exception('Input must be int.')
    if n < 1:
        raise Exception('Input must be greater than 0')
    L = []
    for i in range(n):
        if (i+1)%3 == 0 and (i+1)%5 == 0:
            L += ['FizzBuzz']
        elif (i+1)%3 == 0:
            L += ['Fizz']
        elif (i+1)%5 == 0:
            L += ['Buzz']
        else:
            L += [i+1]
    return L
            
#fizz_buzz(-4)
#fizz_buzz('sd')    Exceptions

def myint(x):
    if not isinstance(x, str):
        raise Exception('Input must be string format.')
    if not x[0] == '0' or not x[1] == 'b':
        raise Exception('Input must start with 0b.')
    res = 0
    power = 1
    length = len(x)
    for i in range(length-2):
        if x[length-i-1] > '1':
            raise Exception('Input must be binary')
        if x[length-i-1] == '1':
            res += power
        power *= 2
    return res

#myint(5)
#myint('0x101')
#myint('0b130')       

def mybin(n):
    if not isinstance(n, int):
        raise Exception('Input must be Integer.')
    if n < 0:
        raise Exception('Input must be positive.')
    res = '0b'
    res_order = ''
    if n == 0:
        res_order += '0'
    while not n == 0:
        res_order += str(n%2)
        n = int(n/2)
    res += res_order[::-1]
    return res

#mybin('s')
#mybin(-1)  Exceptions
