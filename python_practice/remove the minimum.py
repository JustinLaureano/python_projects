def remove_smallest(numbers):
    # return lowest_rating
    if len(numbers) == 0:
        return []

    else:
        updated_ratings = numbers  # copy of list
        instances = 0
        positions = []
        lowest_rating = min(updated_ratings)  # finds the lowest rating

        for pos, rating in enumerate(updated_ratings):
            if rating == lowest_rating:
                instances += 1
                positions.append(pos)  # keeps track of rating spot in list

        del updated_ratings[positions[0]]
        return updated_ratings


# test cases
print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([2, 2, 1, 2, 1]))
print(remove_smallest([1, 2, 3, 1, 1]))
print(remove_smallest([]))
