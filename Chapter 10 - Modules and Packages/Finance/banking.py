#! /usr/bin/env python3
# Name:         mBA - mini Banking App
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This program defines several functions for a banking app

"""
    Manages bank account with deposits and withdrawals
"""

import sys

def deposit(balance):
    """" Deoposit money into bank and return new bank balance"""
    amount = float(input("Enter amount to be deposited: "))
    balance += amount
    print(f"Deposited the amount of \N{euro sign}{amount:.2f}")
    return balance

def withdraw(balance):
    """" Withdraw money into bank and return new bank balance"""
    amount = float(input("Enter amount to be withdrawn: "))
    balance -= amount
    print(f"Withdrawn the amount of \N{euro sign}{amount:.2f}")
    return balance

def main():
    bank_balance = 0
    print(f"Welcome to mBA - mini Banking App")

    while True:
        menu = f"""
                mBA App
                _______
                Current Balance \N{euro sign}{bank_balance}
                1. Deposit money.
                2. Withdraw money.
        """
        print(menu)
        option = input("What would you like to do? (1-2, q=quit)")
        if option == '1':
            bank_balance = deposit(bank_balance)
        elif option == '2':
            bank_balance = withdraw(bank_balance)
        elif option.lower() == 'q':
            break
        else:
            print("Invalid option. Try again")

    print("Thanks for using the mini Banking App")
    return None

# Namespace trick
if __name__ == "__main__":
    main()
    sys.exit(0) #Explicit exit and return code of 0 (zero errors)