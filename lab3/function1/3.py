def solve():
    numheads = int(input())
    numlegs = int(input())
    r = (numlegs - 2 * numheads) / 2
    c = numheads - r
    print(c, "chickens")
    print(r, "rabbits")

solve()