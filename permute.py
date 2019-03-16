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

def get_permutation_indices(lists):
    if lists == []:
        return [[]]
    lower_permutations = get_permutation_indices(lists[1:])
    permutations = []
    for i in range(len(lists[0])):
        permutations.extend([[i]+lst for lst in lower_permutations])
    return permutations

def get_permutations1(lists):
    indices = get_permutation_indices(lists)
    permutations = []
    for lst in indices:
        lst = [lists[i][j] for i,j in enumerate(lst)]
        permutations.append(lst)
    return permutations

lists = get_random_lists()
# print(lists)
# print(get_permutation_indices(lists))
print(len(get_permutations1(lists)))
