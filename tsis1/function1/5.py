from itertools import permutations
def next(user):
    p_user = permutations(user)
    for x in list(p_user):
        print(x)

user = input()

next(user)