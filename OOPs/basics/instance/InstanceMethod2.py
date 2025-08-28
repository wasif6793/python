class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return f"New Balance: Rs. {self.balance}"

account = BankAccount("Wasif", 110)
print(account.deposit(2000))