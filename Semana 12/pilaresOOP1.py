
class BankAccount:
    def __init__ (self, balance):
        self.balance =  balance

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self,balance,min_balance):
        self.balance = balance
        self.min_balance = min_balance

    def withdraw_money(self,amount):
        if (self.balance - amount) < self.min_balance:
            raise ValueError ("Unable to perform transaction. Withdrawal would put balance below minimum allowed.")
        self.balance -= amount


try:
    account1 = SavingsAccount(40,20)
    account2 = SavingsAccount(45,20)

    account1.withdraw_money(25)
    print(account1.balance)
    account2.withdraw_money(25)
    account2.withdraw_money(20)
    print(account2.balance)
except ValueError as ex:
    print(ex)