# Name:         inventory.py
# Authors:      LT9
#               Leander Dalofin
#               Earl John  Gallarde
#               Samantha Coleen Mercado
#               Julius Cris Salinas
# Version:      2.0
# Last Updated: Aug 3, 2023
# Description:  Inventory Management System for Tech Mart

"""
    Welcome to the Tech Mart Inventory System!
    This program focuses on the basic components of an inventory system.
    Below are the following functionalities of the system:
    1. Adding products to the inventory
    2. Updating the quantity of a given product
    3. Removing products from the inventory
    4. Displaying inventory status
    5. Alerts when stock fall below threshold
    6. Calculate total value of inventory.
"""


# Future variables - Commented out for now
# Additional product info
# units_of_measurement    # str
# date_added = ''         # datetime
# added_by = ''
# date_updated = ''       # datetime
# updated_by = ''
# supplier_id = ''
# expiration_date = ''    # datetime
# discount = 0.0          # product discount based on expiration date
# rating = ''             # product rating in stars


def validate_input(prompt, expected_type):
    """
    Prompts the user for input and validates its type and value.

    The function will continue to prompt the user until they provide a valid input.

    Args:
        prompt (str): The message displayed to the user when asking for input.
        expected_type (str): The type of input expected. This can be 'str', 'int', or 'float'.

    Returns:
        str or int or float: The user's input, converted to the expected type. If the expected
        type is 'str', the input is returned as is. If the expected type is 'int' or 'float',
        the function ensures the input is non-negative before returning it.

    Raises:
        ValueError: If the input provided cannot be converted to the expected type.

    Note:
        The function will catch ValueError exceptions and prompt the user to try again if their
        input cannot be converted to the expected type. If the expected type is 'int' or 'float'
        and the input is negative, the function will also prompt the user to try again.
    """
    while True:
        user_input = input(prompt)
        try:
            if expected_type == 'str':
                return user_input
            elif expected_type == 'int':
                user_input = int(user_input)
                if user_input < 0:
                    print("Input cannot be negative. Please try again.")
                else:
                    return user_input
            elif expected_type == 'float':
                user_input = float(user_input)
                if user_input < 0.0:
                    print("Input cannot be negative. Please try again.")
                else:
                    return user_input
            else:
                print("Expected type not recognized. Please try again.")
        except ValueError:
            print("Input does not match expected type. Please try again.")


def enter_product_details():
    """
    Prompts the user to enter details for a product and validates the input.

    The function will prompt the user for the following product details:
        - Product ID: A string that is converted to uppercase.
        - Product Name: A string.
        - Price: A float.
        - Quantity: An integer.
        - Sales Info: A string.
        - Threshold: An integer.

    All inputs are validated using the validate_input function. Each input
    type is specified as a second argument to the validate_input function.

    Returns:
        tuple: A tuple containing the product ID, product name, price, quantity, sales info, and threshold.

    Note:
        It's assumed that the validate_input function takes two arguments: a prompt and a type.
        The function should throw an error or otherwise indicate if the user's input is not of the correct type.
    """
    product_id = validate_input("Enter product ID: ", "str").upper()
    product_name = validate_input("Enter product name: ", "str")
    price = validate_input("Enter price: ", "float")
    quantity = validate_input("Enter quantity: ", "int")
    sales_info = validate_input("Enter sales info: ", "str")
    threshold = validate_input("Enter threshold: ", "int")

    return product_id, product_name, price, quantity, sales_info, threshold


def enter_updates_to_product(product_id):
    """
    Prompts the user to enter new details for an existing product and validates the input.

    The function will prompt the user for the following product details:
        - Product Name: A string.
        - Price: A float.
        - Quantity: An integer.
        - Sales Info: A string.
        - Threshold: An integer.

    All inputs are validated using the validate_input function. Each input
    type is specified as a second argument to the validate_input function.

    Args:
        product_id (str): The ID of the product to update.

    Returns: tuple: A tuple containing the product ID and the updated product name, price, quantity, sales info,
    and threshold.

    Note:
        It's assumed that the validate_input function takes two arguments: a prompt and a type.
        The function should throw an error or otherwise indicate if the user's input is not of the correct type.
    """
    name = validate_input("Enter NEW product name: ", "str")
    price = validate_input("Enter NEW price: ", "float")
    quantity = validate_input("Enter NEW quantity: ", "int")
    sales_info = validate_input("Enter NEW sales info: ", "str")
    threshold = validate_input("Enter NEW threshold: ", "int")

    return product_id, name, price, quantity, sales_info, threshold


def add_product(product, inventory):
    """
    Adds a product to the inventory.

    Args:
        product (tuple): A tuple containing the product details. The order of details in the tuple
                         should match the structure of the inventory list.
        inventory (list): A list of tuples, where each tuple contains the details of a product.

    Returns:
        list: The updated inventory list with the new product added.

    Note:
        This function assumes that the product and inventory arguments are compatible, i.e.,
        each product is a tuple of details and the inventory is a list of such tuples.
    """
    inventory.append(product)
    return inventory


def print_report_header():
    """
    Prints the header for the inventory report.

    The header includes the names of the product details: Product ID, Product Name, Price, Quantity, Sales Info,
    and Threshold. Each detail name is printed in a formatted manner to create a table-like structure.
    """
    print(
        f"{'Product ID':<10} | {'Product Name':<30} | {'Price':>10} | {'Quantity':<10} | {'Sales Info':<30} | {'Threshold':<10}")
    print('-' * 120)


def print_product_info(product):
    """
    Prints the details of a single product in a formatted manner.

    Args:
        product (tuple): A tuple containing the product details. The order of details in the tuple is assumed to be:
                         Product ID, Product Name, Price, Quantity, Sales Info, Threshold.
    """
    product_id, product_name, price, quantity, sales_info, threshold = product
    print(
        f"{str(product_id):<10} | {product_name:<30} | {price:>10.2f} | {str(quantity):<10} | {sales_info:<30} | {str(threshold):<10}")


def generate_report(inventory):
    """
    Generates and prints a formatted report of the inventory.

    The report includes a header, followed by one line for each product in the inventory.
    Each product's details are printed in a formatted manner to align with the header.

    Args:
        inventory (list): A list of tuples, where each tuple contains the details of a product.
    """
    print_report_header()
    for product in inventory:
        print_product_info(product)


def is_product_available(prod_id, inventory):
    """
    Checks if a product is available in the inventory.

    Args:
        prod_id (str): The ID of the product to search for.
        inventory (list): A list of tuples, where each tuple contains the details of a product.

    Returns:
        bool: True if the product is found in the inventory, False otherwise.

    Note:
        If the product is found, the function also prints the details of the product in a formatted manner.
    """
    for product in inventory:
        if product[0] == prod_id:
            return True
        else:
            print(f"Product ID: {prod_id} is not found.")
            return False


def get_product(prod_id, inventory):
    """
    Retrieves a product from the inventory.

    Args:
        prod_id (str): The ID of the product to search for.
        inventory (list): A list of tuples, where each tuple contains the details of a product.

    Returns:
        tuple: The product information if found, None otherwise.
    """
    for product in inventory:
        if product[0] == prod_id:
            return product

    print(f"Product ID: {prod_id} is not found.")
    return None


def update_product(updates, inventory):
    """
    Updates the details of a product in the inventory.

    Args: updates (tuple): A tuple containing the updated product details. The order of details in the tuple is
    assumed to be: Product ID, Product Name, Price, Quantity, Sales Info, Threshold. inventory (list): A list of
    tuples, where each tuple contains the details of a product.

    Returns:
        bool: True if the product is found and updated, False otherwise.

    Note:
        If the product is found and updated, the function also prints the updated details of the product.
    """
    prod_id, name, price, quantity, sales_info, threshold = updates
    for i, product in enumerate(inventory):
        if product[0] == prod_id:
            inventory[i] = (prod_id, name, price, quantity, sales_info, threshold)
            print("\nProduct updated.")
            print_product_info(inventory[i])
            return True


def remove_product(prod_id, inventory):
    """
    Removes a product from the inventory based on the provided product ID.

    Args:
        prod_id (str): The ID of the product to remove.
        inventory (list): A list of tuples, where each tuple contains the details of a product.

    Returns:
        bool: Always returns True if the function call is successful.

    Note: This function does not verify if the product is in the inventory before attempting to remove it. If the
    product ID is not found in the inventory, it will raise a ValueError. Make sure to call is_product_available()
    before calling this function or handle the exception properly.
    """
    to_remove = ''
    for product in inventory:
        if product[0] == prod_id:
            to_remove = product
            break
    inventory.remove(to_remove)
    return True


def calculate_inventory_value(inventory):
    """
    Calculates and prints the total value of the inventory.

    The function calculates the total value of each product (price * quantity) and adds these up to get the total
    inventory value. The details of each product and its total value are printed in a formatted manner.

    Args:
        inventory (list): A list of tuples, where each tuple contains the details of a product.
    """
    print(f"{'Product ID':<10} | {'Product Name':<30} | {'Price':>10} | {'Quantity':<10} | {'Product Value':<30}")
    print('-' * 100)
    total_inventory_value = 0
    for product in inventory:
        prod_id, name, price, quantity, _, _ = product
        total_product_value = price * quantity
        total_inventory_value += total_product_value
        print(f"{prod_id:<10} | {name:<30} | {price:>10} | {quantity:<10} | {total_product_value:<30}")
    print('-' * 100)
    print(f"{'TOTAL':>70} | {total_inventory_value:>10.2f} |")


def alert_to_restock(product):
    """
    Checks if a product's quantity is below its threshold and sends an alert to restock if necessary.

    The function takes as input a tuple containing product information. The tuple should have the following structure:
    - The first element is the product ID (string).
    - The second element is the product name (string).
    - The third element is ignored.
    - The fourth element is the current quantity (integer).
    - The fifth element is ignored.
    - The sixth element is the threshold quantity (integer).

    If the current quantity is less than the threshold quantity, the function prints a message alerting to restock
    the product.

    Args: product (tuple): A tuple containing product information, including the product ID, product name,
    current quantity, and threshold quantity.

    Returns:
        None
    """
    prod_id, name, _, quantity, _, threshold = product
    if quantity < threshold:
        print(f"{prod_id}: {name} has {quantity} units left and is below the threshold of {threshold}. Restock ASAP")


def main():
    """
    Runs the main program loop for the inventory management system.

    The program provides the following options to the user:
    1. Add Product: Asks the user to enter details for a new product and adds it to the inventory.
    2. Update Product: Asks the user for the ID of a product and the new details, then updates the product in the
    inventory.
    3. Remove Product: Asks the user for the ID of a product and removes it from the inventory.
    4. Generate Report: Prints a formatted report of the current inventory.
    5. Calculate Total Inventory Value: Calculates and prints the total value of the current inventory.
    6. Exit: Exits the program.

    The user is repeatedly asked to choose an option until they choose to exit. If the user enters an invalid command,
    they are asked to try again.
    """
    print('Hello, Tech Mart User!')
    inventory = []

    command = validate_input("""
        What would you like to do?

        1. Add Product
        2. Update Product
        3. Remove Product
        4. Generate Report
        5. Calculate Total Inventory Value
        6. Exit

        Enter a value from 1 to 6: 
    """, 'int')
    while command != 6:
        if command == 1:
            print("***** ADD PRODUCT *****")
            new_product = enter_product_details()
            print("The following values have been entered:")
            print_report_header()
            print_product_info(new_product)

            product = get_product(new_product[0], inventory)
            if product:
                print("Product exists. Unable to add same product.")
                print_report_header()
                print_product_info(product)
            else:
                add_product(product, inventory)
                print("The following product has been found:")
        elif command == 2:
            print("***** UPDATE PRODUCT *****")
            product_id = validate_input("Enter the product ID to update: ", "str").upper()
            is_update_successful = False
            product = get_product(product_id, inventory)
            if product:
                updates = enter_updates_to_product(product_id)
                is_update_successful = update_product(updates, inventory)
            if is_update_successful:
                print(f"The following product has been updated: {product_id}")
                print("UPDATED INVENTORY")
                generate_report(inventory)
                alert_to_restock(get_product(product_id, inventory))

        elif command == 3:
            print("***** REMOVE PRODUCT *****")
            product_id = validate_input("Enter the product ID to remove: ", "str").upper()
            is_remove_prod_successful = False
            if is_product_available(product_id, inventory):
                is_remove_prod_successful = remove_product(product_id, inventory)
            if is_remove_prod_successful:
                print(f"The following product has been removed: {product_id}")
                print("UPDATED INVENTORY")
                generate_report(inventory)
        elif command == 4:
            print("***** GENERATE REPORT *****")
            generate_report(inventory)
        elif command == 5:
            print("***** CALCULATE INVENTORY VALUE *****")
            calculate_inventory_value(inventory)
        elif command == 6:
            print("***** EXITING *****")
            print("Thank you for using Tech Mart. Goodbye!")
        else:
            print(f"Action: {command} is not recognized. Please try again.")

        command = validate_input("""
        What would you like to do?

        1. Add Product
        2. Update Product
        3. Remove Product
        4. Generate Report
        5. Calculate Total Inventory Value
        6. Exit

        Enter a value from 1 to 6: 
        """, 'int')


if __name__ == "__main__":
    main()
