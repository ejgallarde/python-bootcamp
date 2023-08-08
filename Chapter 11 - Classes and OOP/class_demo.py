# Class - a blueprint of the real-world OBJECT

# Principles of OOP - Object-oriented programming
# Encapsulation
# Abstraction
# Polymorphism

class Dog:
    # class variables - owned by the class and not of the instantiated object, but may access si object instance
    number_of_feet = 4

    def __init__(self, name, color, breed, hungry):
        self.name = name  # instance variable
        self.dog_color = color
        self.breed = breed
        self.hungry = hungry

    def bark(self):
        return "woof"


my_dog = Dog("Dagul", "brown", "azkal", True)  # process of creating an instance of the class
any_variable = Dog('', '', '', False)
