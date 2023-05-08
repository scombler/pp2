def spy_game(seq):
    for x in range(len(seq) - 2):
        if seq[x] == seq[x + 1] == 0 and seq[x + 2] == 7:
            return True
        elif seq[x] == seq[x + 1] == 0 and seq[x + 2] != 7:
            return False
        elif seq[x] == 0 and seq[x + 1] != 0:
            return False
    return seq

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))