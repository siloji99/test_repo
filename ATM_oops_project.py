class atm():
    def __init__(self):
         self.choice1 = 1
         self.choice2 = 2
         self.choice3 = 3
    def credit(self):
        if choice1 == '1':
            amount = float(input("Enter amount to credit: "))
        elif amount <= 0:
            print("Please enter a positive amount.")
        else:
            balance += amount
            print(f"${amount} credited to your account.")
    def withdraw(self):
        if choice2 == '2':
            amount = float(input("Enter amount to debit: "))
        elif amount <= 0:
            print("Please enter a positive amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"${amount} debited from your account.")
    def bal(self):
        if choice3 == '3':
            print(f"Your current balance is: ${balance}")
sbi = atm
sbi.credit(1)

add my changes
