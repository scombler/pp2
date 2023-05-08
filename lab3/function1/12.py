def histogram(seq):
    for x in seq:
        print("*" * x)

seq = list(map(int, input().split()))
histogram(seq)
