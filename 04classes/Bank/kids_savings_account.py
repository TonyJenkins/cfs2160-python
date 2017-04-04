#!/usr/bin/env python3

# kids_savings_account.py
#
# Simple Bank Account class example: The Young Person's Savings Account.
#
# AMJ
# 2017-04-01

from deposit_account import DepositAccount

class KidsSavingsAccount (DepositAccount):

    def __init__ (self, account_holder, interest_rate):
        DepositAccount.__init__ (self, account_holder, interest_rate)

    def deposit (self, deposit_amount):
        try:
            if deposit_amount > 0 and self.balance + deposit_amount < 100.0:
                DepositAccount.deposit (self, deposit_amount)
        except TypeError:
            pass