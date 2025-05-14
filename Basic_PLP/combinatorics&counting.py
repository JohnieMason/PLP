# Counting principles:
# i Permutations and combinations: Essential for calculating the number of possible states or outcomes(in search problems or optimizations)
# ii pigeonhole principle: useful idea when you want to prove existence of a perticular outcome given enough constraints.
# Applications in algorithms: Estimating the size of problem spaces, Designing algorithms that efficiently cover all cases without brute-forcing every possibility.
# using python itertools, we can generate all possible arrangements or selection of set items

import itertools
elements = ['a', 'b', 'c']
# All permutations of the list:
permutations = list(itertools.permutations(elements))
print("permutations of ['a', 'b', 'c']:", permutations)

# All  combinations of 2 elements:
combinations = list(itertools.combinations(elements, 2))
print("Combinations of 2 from ['a', 'b', 'c']:", combinations)
