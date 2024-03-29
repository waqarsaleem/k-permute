# Recursive computation of all k-length permutations given k lists where the
# i-th element in each permutation is from the i-th list.

import random

def get_random_lists():
    lists = []
    num_lists = random.randrange(2, 10)
    for _ in range(num_lists):
        list_size = random.randrange(2, 10)
        lists.append(random.sample(range(100), list_size))
    return lists

# TODO: optmize using a generator
def advance_indices(indices, limits):
    size = len(indices)
    i = -1
    indices[i] += 1
    while indices[i] == limits[i] and i != -size:
        indices[i] = 0
        i -= 1
        indices[i] += 1
    if i == -size and indices[i] == limits[i]:
        return []
    return indices

def get_permutations(lists):
    limits, indices = zip(*[(len(lst),0) for lst in lists])
    permutations = []
    permutations.append([lists[i][j] for i,j in enumerate(indices)])
    # := is syntax for "assignment expression" whcih requires python 3.8. It
    # saves some lines of code.
    # advance_indices can be opitmized through a generator.
    while indices := advance_indices(indices, limits):
        permutations.append([lists[i][j] for i,j in enumerate(indices)])
    return permutations

lists = get_random_lists()
print([len(lst) for lst in lists])
print(len(get_permutations2(lists)))
