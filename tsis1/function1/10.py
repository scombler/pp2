def like_set(mainlist):
    newlist = []
    for x in mainlist:
        if x not in newlist:
            newlist.append(x)
    return newlist

mainlist = input().split()

print(like_set(mainlist))