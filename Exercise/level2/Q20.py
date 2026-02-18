'''Build a BankAccount class with owner and balance attributes. Implement deposit(),
withdraw() (block overdrafts), and get_balance(). Use __str__ to display the account.'''

class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        try:
            if self.balance < amount:
                raise Exception(f"You didn't have balance to withdraw {amount}")
            self.balance -= amount
            print(f"{amount} is withdraw succefully , you current balance is {self.balance}")
        except Exception as e:
            print(e)
    def get_balance(self):
        return f"Your current balance is {self.balance}"
    def __str__(self):
        print("...............Your Account Detials.................")
        print(f"Account Owner name : {self.name}")
        print(f"Account Balance : {self.balance}")
        return f"Have a good day"


acc = BankAccount("Tarun",100)

acc.deposit(1000)
print(acc.get_balance())
acc.withdraw(12000)
acc.withdraw(1000)
print(acc.get_balance())
print(acc)