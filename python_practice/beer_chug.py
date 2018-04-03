"""
Mike and Joe are fratboys that love beer and games that involve drinking. They
play the following game: Mike chugs one beer, then Joe chugs 2 beers, then
Mike chugs 3 beers, then Joe chugs 4 beers, and so on. Once someone can't
drink what he is supposed to drink, he loses.

Mike can chug at most A beers in total (otherwise he would pass out), while
Joe can chug at most B beers in total. Who will win the game?

Write the function game(A,B) that returns the winner, "Mike" or "Joe"
accordingly, for any given integer values of A and B.

Note: If either Mike or Joe cannot drink at least 1 beer, return the string
"Non-drinkers can't play".
"""


def game(a, b):
    score = {'mike': 0, 'joe': 0}
    counter = 0
    game = True

    if a < 1 or b < 1:
        return "Non-drinkers can't play"

    while game:
        for name, count in score.items():
            counter += 1

            if name == 'mike' and (score[name] + counter) <= a or name == \
                    'joe' and (score[name] + counter) <= b:
                score[name] += counter

            else:
                game = False

    if score['mike'] > score['joe']:
        return "Mike"

    else:
        return "Joe"


print(game(4, 2))  # Mike a
print(game(3, 2))  # Joe b
print(game(9, 1000))  # Joe b
print(game(0, 1))  # Non drinkers
