# Recursive computation of all k-length permutations given k lists where the
# i-th element in each permutation is from the i-th list.

import random

def get_random_lists():
    lists = []
    num_lists = random.randrange(2, 5)
    for _ in range(num_lists):
        list_size = random.randrange(2, 5)
        lists.append(random.sample(range(100), list_size))
    return lists

def get_permutations(lists):
    if lists == []:
        return [[]]
    lower_permutations = get_permutations(lists[1:])
    permutations = []
    for n in lists[0]:
        permutations.extend([[n]+lst for lst in lower_permutations])
    return permutations

lists = get_random_lists()
print(lists)
print(get_permutations(lists))
