"""A simple attempt to model a random dice roll."""
from random import randint


class Dice():
    """Initialize the dice."""
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        """roll a die one time."""
        print(randint(1, self.sides))

    def dice_rolls(self, rolls):
        """Defines how many times to roll the dice."""
        x = 0
        while x < rolls:
            Dice(self.sides).roll_dice()
            x += 1


die_6 = Dice(6)
die_10 = Dice(10)
die_20 = Dice(20)


die_6.dice_rolls(5)
print('---')
die_10.dice_rolls(5)
print('---')
die_20.dice_rolls(5)
