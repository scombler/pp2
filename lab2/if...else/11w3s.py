# nested if : when we can have if statements inside if statements, this is called nested if statements:
x = 26

if x > 10:
    print("above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")