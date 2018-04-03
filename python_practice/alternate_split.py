"""
For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every
2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
"""


def encrypt(text, n):
    if n == 0:
        return text
    var = text
    for x in range(n):
        var = var[1::2] + var[::2]
        return var


print(encrypt("This is a test!", 2))
