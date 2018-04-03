"""
an isogram is a word that has no repeating letters, consecutive or
non-consecutive. Implement a function that determines whether a string that
only contains letters is an isogram.
"""


def is_isogram(string):
    letters = {}
    for letter in string:
        if letter.lower() not in letters and letter.isalpha():
            letters[letter.lower()] = 1
        elif letter.lower() in letters and letter.isalpha():
            letters[letter.lower()] += 1
        else:
            return False

    for value in letters.values():
        if value > 1:
            return False
    return True


print(is_isogram('moseZz'))
print(is_isogram('VaSe'))