s = input()
p = s[::-1]
if hash(s) == hash(p):
    print("yeah, it's a palindrome!")
else:
    print("nah, it ain't palindrome :(")

# hash() -> return the hash value for the given object.
# two objects that compare equal must also have the same hash value, but the reverse is not necessarily true.

x = reversed(s)
r = "".join(x)
print(r)
if s == r:
    print("yeah, it's a palindrome!")
else:
    print("nah, it ain't palindrome :(")

# the reversed() function returns a reversed iterator object.