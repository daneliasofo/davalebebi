class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("ახალი ბალანსი:", self.__balance)
        else:
            print("დადებითი თანხა")


acc = BankAccount()

acc.deposit(100)
acc.deposit(-50)