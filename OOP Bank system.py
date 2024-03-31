class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no1 = acc

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited.")
        print("Total balance is Rs.",self.balance)

    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited.")
        print("Total balance is Rs.",self.balance)

    #show current balance
    def get_balance(self):
        return self.balance()

acc1 = Account(10000,12345)
print(acc1.balance)
print(acc1.account_no)



