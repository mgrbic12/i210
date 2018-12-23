class BankAccount(object):

    def __init__(self, amount = 0):
        self.totAmount = amount

    def withdraw(self, amt):
        if self.totAmount - amt < 0:
            print("Not enough money")
        else:
            self.totAmount -= amt

    def deposit(self,amt):
        self.totAmount += amt

    def balance(self):
        return self.totAmount
        
        
#test/main

##x = BankAccount(700)
##print(x.balance())
##x.withdraw(70)
##print(x.balance())
##x.deposit(7)

