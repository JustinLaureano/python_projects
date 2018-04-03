"""
Implement the function which takes an argument a sequence and returns a list of
items without any elements with the same value next to each other and
preserving the original order of elements.
"""


def unique_order(sequence):
    # Create list of sequence and return list without consecutive duplicates.
    seq_list = list(sequence)
    new_sequence = []
    for item in seq_list:
        if len(new_sequence) == 0:
            new_sequence.append(item)
        elif item != new_sequence[-1]:
            new_sequence.append(item)

    return new_sequence


print(unique_order("ABBCcADD"))  # ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_order([1, 2, 2, 3, 3]))  # [1, 2, 3]
