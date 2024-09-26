import random
from typing import Tuple


def generate_random_tuple():
    # Start with the first element as 0
    tuple_list = [0]

    # Determine how many 1s to include (between 2 and 3)
    num_ones = random.randint(2, 3)

    # Generate a list with the required number of 1s and the rest as 0s
    rest = [1] * num_ones + [0] * (4 - num_ones)

    # Shuffle the list to randomize the positions of 1s and 0s
    random.shuffle(rest)

    # Append the rest of the elements to the initial 0
    tuple_list.extend(rest)

    # Convert to tuple
    return tuple(tuple_list)

def generate_2d_array(rows, cols):
    return [[generate_random_tuple() for _ in range(cols)] for _ in range(rows)]



if __name__ == "__main__":
    playfield = [[(2, 0, 0, 1, 0), (0, 0, 1, 1, 0), (0, 0, 1, 1, 0)],
                 [(1, 0, 0, 1, 0), (0, 1, 1, 0, 1), (0, 1, 0, 0, 1)],
                 [(0, 1, 0, 1, 0), (0, 1, 1, 0, 0), (2, 1, 0, 0, 0)]]


    print(playfield[0][0][0])