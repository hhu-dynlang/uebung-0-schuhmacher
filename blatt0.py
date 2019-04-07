def is_palindrome(s):
    if not isinstance(s, str):
        raise Exception('Input should be a string.')
    if len(s) % 2 == 1:
        return False
    length = len(s) / 2
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
