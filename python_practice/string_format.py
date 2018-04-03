"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for
the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""


def namelist(names):
    new_string = ''
    if len(names) == 0:
        return ''

    for item in names:

        for value in item.values():
            if len(names) == 1:
                return value
            elif item == names[-1]:
                new_string += '& {}'.format(value)

            elif item == names[-2]:
                new_string += '{} '.format(value)
            else:
                new_string += '{}, '.format(value)
    return new_string


test_names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},
              {'name': 'Ed'}]

print(namelist(test_names))
