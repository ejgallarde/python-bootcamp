#! /usr/bin/env python3
# Name:         
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  

"""
    Withdraw, deposit, and display banking info

"""

import sys
import banking
def display_info(bal, scode):
    """ Display Bank info """
    print(f"Current balance = \N{euro sign}{bal:.2f}, sort code = {scode}")
    return None

def main():
    bank_balance = 34_500.97
    sort_code = '80-45-37'
    print("Welcome to MBA - Minions Banking App")
    name = input("Enter your name: ").title()

    while True:
        menu = f"""
                    Menu Options
                    _______
                    Current Balance \N{euro sign}{bank_balance}
                    1. Check balance.
                    2. Deposit money.
                    3. Withdraw money.
                    q - Quit
            """

        print(menu)
        option = input("What would you like to do? (1-3, q=quit)")
        if option == '1':
            display_info(bank_balance, sort_code)
        elif option == '2':
            bank_balance = banking.deposit(bank_balance)
            pass
        elif option == '3':
            bank_balance = banking.withdraw(bank_balance)
            pass
        elif option.lower() == 'q':
            break
        else:
            print("Invalid option. Try again")

    print(f"Thanks {name} for using the Minions Banking App")
    return None

# Namespace trick
if __name__ == "__main__":
    # Only execute if directly ran as a program
    # Ignore if imported as a module
    main()
    sys.exit(0) #Explicit exit and return code of 0 (zero errors)