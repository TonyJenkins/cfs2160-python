#!/usr/bin/env python3

# deposit_amount_account.py
#
# Simple Bank Account class example: The Deposit Account.
#
# AMJ
# 2017-04-01

from bank_account import BankAccount

class DepositAccount (BankAccount):

    def __init__ (self, account_number, account_holder, interest_rate):
        BankAccount.__init__ (self, account_number, account_holder, False)
        self.interest_rate = interest_rate

    def add_interest (self):
        self.deposit (self.balance * self.interest_rate)
