#! /usr/bin/env python3
# Name:         
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This is an ultra-realistic online computer game with Tanks!

"""
    GOT - Game of Tanks!
"""

import tank
import sys


def main():
    # Instantiate/create 3 new Tank objects..
    earl_tank = tank.Tank('german', 'tiger')
    shae_tank = tank.Tank('american', 'sherman')
    craig_tank = tank.Tank('british', 'churchill')
    # And the game begins..
    earl_tank.accel(63)
    shae_tank.accel(41)
    craig_tank.rotate_left(289)
    craig_tank.accel(15)
    craig_tank.shoot()
    # And success..
    earl_tank.take_damage(54)
    shae_tank.take_damage(65)

    # Example of getters/setters usage
    print(f"Health of Earl's tank = {earl_tank.get_health()}")
    earl_tank.set_health(101)
    print(f"Health of Earl's tank = {earl_tank.get_health()}")


    # Can use the variable property access to the getter/setter
    earl_tank.tank_health =  200
    print(f"Health of Earl's tank = {earl_tank.tank_health}")

    print(f"Status of Earl's tank: {earl_tank}")
    return None

# Namespace trick.
if __name__ == "__main__":
    # Execute only if ran directly as a program.
    main()
    sys.exit(0)

