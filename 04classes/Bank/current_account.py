#!/usr/bin/env python3

# current_account.py
#
# Simple Bank Account class example: The Current Account.
#
# AMJ
# 2017-04-01

from bank_account import BankAccount

class CurrentAccount (BankAccount):

    def __init__ (self, account_holder, has_overdraft):
        BankAccount.__init__ (self, account_holder, has_overdraft)
