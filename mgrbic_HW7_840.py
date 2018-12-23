class BankAccount(object):

    def __init__(self, amount = 0):
        try:
            if amount < 0:
                raise ValueError
            else:
                self.totAmount = amount
        except ValueError:
            print("Illegal balance")

    def withdraw(self, amt):
        try:
            if amt > self.totAmount:
                raise ValueError
            else:
                self.totAmount -= amt
        except ValueError:
            print("Overdraft")

    def deposit(self, amt):
        try:
            if amt < 0:
                raise ValueError
            else:
                self.totAmount += amt
        except ValueError:
            print("Negative deposit")

    def balance(self):
        return self.totAmount
