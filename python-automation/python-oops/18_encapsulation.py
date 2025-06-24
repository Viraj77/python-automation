class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def show_balance(self):
        print(f"{self.owner}'s balance is: {self.__balance}")

# Creating object
acc = Account("Viraj", 10000)
acc.show_balance()
# print(acc.__balance)  # This will cause an error because it's private