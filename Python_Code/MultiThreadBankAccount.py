import time
from random import randint
from threading import Lock,Thread


class Account():
    def __init__(self,Money,Name):
        self._Money = Money
        self._Name = Name
        self._lock = Lock();

    def deposit(self,Money,Number):
        print("%s try to make deposit $%d" % (Number,Money))
        time.sleep(randint(1,3))
        self._lock.acquire();
        print("%s has acquired the lock" % Number)
        try:
            new_Money = Money +self._Money
            time.sleep(0.05)
            self._Money = new_Money
        finally:
            print('{} has completed deposit, balance is ${:d}'.format(Number, self._Money))
            self._lock.release()

    def withdraw(self,Money,Number):
        print("%s try to make withdraw $%d" % (Number,Money))
        time.sleep(randint(1,3))
        self._lock.acquire();
        print("%s has acquired the lock" % Number)
        try:
            new_Money = self._Money - Money
            time.sleep(0.05)
            self._Money = new_Money
        finally:
            print('{} has completed withdraw, balance is ${:d}'.format(Number, self._Money))
            self._lock.release()




    @property
    def Money(self):
        return self._Money

    @property
    def Name(self):
        return self._Name

class AddMoneyThread(Thread):
    def __init__(self,Account,Money,Number):
        super().__init__()
        self._account = Account
        self._Money = Money
        self._Number = Number

    def run(self):
        self._account.deposit(self._Money,self._Number)


class CutMoneyThread(Thread):
    def __init__(self, Account, Money,Number):
        super().__init__()
        self._account = Account
        self._Money = Money
        self._Number = Number

    def run(self):
        self._account.withdraw(self._Money,self._Number)


def main():
    account = Account(10000,"Yicheng")
    threads = []
    for i in range(1000):
        money = randint(1,1000)
        if money % 2 ==0:
            t = AddMoneyThread(account, money,i)
        else:
            t = CutMoneyThread(account,money,i)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("%s\'s account balance is %d" % (account.Name,account.Money))


if __name__ == '__main__':
    main()