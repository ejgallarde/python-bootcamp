#! /usr/bin/env python3
# Name:         bookstore.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This exercise carries out some basic operations on variables.

"""
    This exercise carries out some basic operations on variables.
    Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
    $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
    60 copies?
"""
import math

cover_price = 24.95
discount = 0.4
shipping_cost = 3
additional_shipping_cost = 0.75
orders = 60

total_order_cost = orders * cover_price * (1 - discount)
print(total_order_cost)

total_shipping_cost = shipping_cost + additional_shipping_cost * (orders - 1)
print(total_shipping_cost)

total_cost = total_order_cost + total_shipping_cost
rounded_total_cost = round(total_cost, 2)
print(f"${rounded_total_cost}")

myPi = 3.14e0
print(myPi)

print('$', myPi)
