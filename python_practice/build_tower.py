"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

for example, a tower of 6 floors looks like below

[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]
"""


def tower_builder(n_floors):
    tower = []
    if n_floors == 1:
        tower.append('*')
    else:
        for x in range(n_floors):
            space = ' ' * (n_floors - x)
            if x == 0:
                tower.append(space + '*' + space)
            else:
                tower.append(space + ('*' * ((2 * x) + 1)) + space)

    for floor in tower:
        print(floor)


tower_builder(9)
