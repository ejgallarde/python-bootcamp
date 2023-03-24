#! /usr/bin/env python3
# Name:         
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This module describes a Class of Tank.

"""
    Tank class
"""

class Tank:

    #Class is made up of attributes and behaviors
    def __init__(self, country, model):
        # Sometimes called the constructor
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'x': 0, 'y': 0, 'z': 0}
        self._shells = 20
        self._health = 100
        # No return because this method is implicitly called.

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed += decrease
        return None

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, amount):
        self._health -= amount
        return None

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health
        return None

    # Create a new Variable Property that interfaces to two MEthods!
    #tank_health = property(get_health, set_health)

    # Alternatively we could use decorators to wrap two different methods
    # with same name but different behaviour.
    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    def tank_health(self, newhealth):
        self._health = newhealth
        return None

    # Example of Operator Overloading.
    def __add__(self, other):
        return self._health + other._health

    # Example of Duck Typing - teaching Tanks how to Quack like a str!
    def __str__(self):
        return f"Health={self._health}, Speed={self._speed}, Shells={self._shells}"

    def __del__(self):
        # Destructor method.
        print("Boom, tank destroyed")
        return None

