#!/usr/bin/env python3

# bank.py
#
# Simple Bank Account class example: The Bank.
#
# AMJ
# 2017-04-01

from current_account import CurrentAccount
from deposit_account import DepositAccount
from kids_savings_account import KidsSavingsAccount


class Bank:

    def __init__ (self):
        self.accounts = []

    @property
    def assets (self):

        total = 0

        for a in self.accounts:
            total += a.balance

        return total

    def add_account (self, account):

        self.accounts.append (account)

    def interest (self):

        for a in self.accounts:
            try:
                a.add_interest ()
            except AttributeError:
                pass

if __name__ == '__main__':

    b = Bank ()

    dep_1 = DepositAccount ('John Smith', 0.15)
    dep_2 = DepositAccount ('Jane Smith', 0.20)
    cur_1 = CurrentAccount ('Fred Jones', True)
    kid_1 = KidsSavingsAccount ('Lisa Jones', 0.05)

    print (dep_1)

    dep_1.deposit (100)
    dep_2.deposit (130)
    cur_1.deposit (60)
    kid_1.deposit (50)

    print (kid_1)

    b.add_account (dep_1)
    b.add_account (dep_2)
    b.add_account (cur_1)
    b.add_account (kid_1)

    print (b.assets)
    b.interest ()
    print (b.assets)

