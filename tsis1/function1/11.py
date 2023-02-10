def palindrome(s):
    p = s[::-1]
    if s == p:
        print("yeah, it's a palindrome")
    else:
        print("no, it isn't a palimdrome")

s = input()

palindrome(s)