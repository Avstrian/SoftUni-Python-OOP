from itertools import permutations


def possible_permutations(start_list):
    all_permutations = list(permutations(start_list))
    listed_permutations = [list(el) for el in all_permutations]
    for el in listed_permutations:
        yield el
