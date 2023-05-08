class String():
    def __init__(self):
        self.str = " "

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())

output = String()
output.getString()
output.printString()