def is_palindrome(s):
    if not isinstance(s, str):
        raise Exception('Input should be a string.')
    if(len(s)) % 2 == 1:
        return False
    length = len(s) / 2
    for i in range(length):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

# is_palindrome(4) for exception
