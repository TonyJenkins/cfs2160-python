#!/usr/bin/env python3

# bank_account.py
#
# Simple Bank Account class example.
#
# AMJ
# 2017-04-01

from random import randint

class BankAccount:

    def __init__ (self, account_holder, has_overdraft):
        self.account_number = self.generate_account_number ()
        self.account_holder = account_holder
        self.has_overdraft = has_overdraft

        self.__balance = 0.0
        self.is_active = True

    @property
    def balance (self):
        return self.__balance

    def deposit (self, deposit_amount):
        try:
            if deposit_amount > 0:
                self.__balance += deposit_amount
        except TypeError:
            pass

    def withdraw (self, withdraw_amount):
        try:
            if withdraw_amount >= self.__balance or has_overdraft:
                self.__balance -= withdraw_amount
        except TypeError:
            pass

    def deactivate (self):
        self.is_active = False

    def activate (self):
        self.is_active = True

    def generate_account_number (self):
        s = ''
        for i in range (9):
            s += str (randint (0, 9))

        return s

    def __str__ (self):
        return "Account: {:} Holder: {:} Balance: {:}".format (self.account_number, self.account_holder, self.balance)
