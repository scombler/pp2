class Bank_Account:
    def __init__(self):
        self.owner = str(input("owner's name: "))
        self.balance = float(input("balance: "))
    
    def deposit(self):
        amount = float(input("deposit amount: "))
        self.balance += amount
    
    def withdraw(self):
        amount = float(input("the amount i wanna withdraw: ")) 
        if amount > self.balance:
            print('Low balance')
        else:
            self.balance -= amount
            print('Success')

a = Bank_Account()
a.withdraw()
a.deposit()
a.withdraw()