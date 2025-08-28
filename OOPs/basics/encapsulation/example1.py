class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def depost(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -=amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(10000)
acc.depost(2000)
acc.withdraw(9000)
print(acc.get_balance())