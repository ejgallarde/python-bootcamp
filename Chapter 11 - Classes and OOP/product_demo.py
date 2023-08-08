class Product:
    def __init__(self, _id, name, price, qty, threshold):
        self.product_id = _id
        self.product_name = name
        self.price = price
        self.quantity = qty
        self.threshold = threshold

    def describe(self):
        print(f'This is a {self.product_name} product with {self.price} and {self.quantity}.')
        return


apple = Product(100, 'Apple', 40.50, 100, 10)
apple.describe()

inventory = []
with open("products.csv", "rt") as products:
    for product_line in products.readline():
        attribute_value = product_line.split(',')
        prod = Product(attribute_value[0], attribute_value[1], attribute_value[2], attribute_value[3], attribute_value[4])
        inventory.append(prod)
