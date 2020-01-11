import datetime
import pytz


class Account:

    @staticmethod
    def _curent_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._curent_time(), balance)]
        print("Account Created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._curent_time(), amount))

    def withdraw(self, amoount):
        if 0 < amoount <= self.__balance:
            self.__balance -= amoount
            self._transaction_list.append((Account._curent_time(), -amoount))
        else:
            print("Amount should be between 0 and your account balance")
        self.show_balance()

    def show_balance(self):
        print("balance is {}".format(self.__balance))

    def show_transaction(self):
        for date,amount in self._transaction_list:
            if amount>0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *=-1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)

    tim.withdraw(500)

    tim.withdraw(2000)

    tim.show_transaction()

    steph = Account("steph", 800)
    steph.__balance=200
    steph.deposit(100)
    steph.withdraw(100)
    steph.show_transaction()
    steph.show_balance()
    print(steph.__dict__)
    steph._Account__balance=40 #mangling
    steph.show_balance()

