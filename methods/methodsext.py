import datetime
import pytz


class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactionlist = []
        print("Account Created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transactionlist.append((Account._current_time(), amount))

    def withdraw(self, amoount):
        if 0 < amoount <= self.balance:
            self.balance -= amoount
            self.transactionlist.append((Account._current_time(), -amoount))
        else:
            print("Amount should be between 0 and your account balance")
        self.show_balance()

    def show_balance(self):
        print("balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transactionlist:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (localtime was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)

    tim.withdraw(500)

    tim.withdraw(2000)

    tim.show_transactions()
