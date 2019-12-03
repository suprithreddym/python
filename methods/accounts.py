class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account Created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amoount):
        if 0 < amoount <= self.balance:
            self.balance -= amoount
        else:
            print("Amount should be between 0 and your account balance")
        self.show_balance()

    def show_balance(self):
        print("balance is {}".format(self.balance))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)

    tim.withdraw(500)

    tim.withdraw(2000)
