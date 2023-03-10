s = input()
upper = 0 
lower = 0
for i in s:
    if ord(i) >= 65 and ord(i) <= 90:  # by ascii code: [A-Z] = [65-90]
        upper += 1
    elif ord(i) >= 97 and ord(i) <= 122: # by ascii code: [a-z] = [97-122]
        lower += 1
print("number of uppercase letters:", upper)
print("number of lowercase letters:", lower)

# ord() -> it returns the number representing the unicode code of a specified character.