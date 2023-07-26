#! /usr/bin/env python3
# Name:        .py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo how to Define, call and
# pass parameters into a user function and optionally return data.
"""
    DocString:
"""
count = 0


# Example of a user function with parameter passing and
# defaults and annotations. Enforce named parameters (*, )
# Annotations not enforced (embedded comment used for parameters and
# preferred types of data).
def say_hello(greeting: str = "konnichiwa", recipient: str = "tomodachi"):
    # if isinstance(recipient, str):
    message = f"{greeting} {recipient}"
    print(message)
    return


say_hello("g'day", "mates")  # Positional parameter passing.
say_hello(greeting="hola", recipient="amigos")  # Named parameter passing
say_hello(recipient="dost", greeting="namaste")  # Named parameter passing (different order)
say_hello("bonjour", recipient="mes amis")  # Mixed parameter passing (positional->named)
say_hello("ciao", "amici")
say_hello("konnichiwa", 42)  # will produce an error
say_hello()  # default values are used
