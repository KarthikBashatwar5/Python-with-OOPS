class Bankacc:
    acc_holder="Karthik"
    acc_no="59002345678"
    balance=5000
    def deposit(self,money):
        money=int(input(money))
        self.balance=self.balance +money
        print("Balance:",self.balance)
    def withdrawal(self,cash):
        cash=int(input(cash))
        self.balance=self.balance-cash
        print("Balance after withdrawal:",self.balance)
    def display(self):
        print("Balance:",self.balance)
s = Bankacc()
s.deposit("Enter deposit amount:")
print("Account Holder:",s.acc_holder)
print("Account No:",s.acc_no)
print("Balance:",s.balance)
