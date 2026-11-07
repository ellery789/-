from itertools import permutations

for p in permutations(range(1, 9)):
    print(" ".join(map(str, p)))
