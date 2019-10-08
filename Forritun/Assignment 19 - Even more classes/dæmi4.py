class Account():
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return 'Balance: {:.2f}'.format(self.balance)


class SavingsAccount(Account):
    def __init__(self, balance, interest=1.05, bonus=0.1):
        super().__init__(balance)
        self.interest=interest
        self.bonus=bonus
    def update_balance(self):
        self.balance=self.balance*(self.interest+self.bonus)


class DebitAccount(Account):
    def __init__(self,balance ,interest=1.02):
        super().__init__(balance)
        self.interest=interest
    
    def update_balance(self):
        self.balance=self.balance*self.interest


    
s1 = SavingsAccount(300)
d1 = DebitAccount(1100)

print(s1)
print(d1)
assert str(s1) == "Balance: 300.00"
assert str(d1) == "Balance: 1100.00"