def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False


print(is_palindrome('level'))
print(is_palindrome('snail'))