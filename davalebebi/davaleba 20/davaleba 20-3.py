class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("არ არის საკმაარისი")

    def get_balance(self):
        return self.__balance


acc = BankAccount()

acc.deposit(500)
acc.withdraw(200)
acc.withdraw(400)

print("Balance:", acc.get_balance())