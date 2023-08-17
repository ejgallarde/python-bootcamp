class InvalidInputError(Exception):
    pass


def validate_input(value):
    if value < 0:
        raise InvalidInputError("Negative values are not allowed.")


try:
    user_input = float(input("Please enter a number: "))
    validate_input(user_input)
except InvalidInputError as e:
    print(f"Error: {e}")
    print("Please enter a positive number or zero next time.")
except ValueError:
    print("Error: Invalid format. Please enter a valid number.")
else:
    print("Input is valid!")
finally:
    print("Validation process completed.")
