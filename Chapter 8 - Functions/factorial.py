import math


def mystery(n):
    result = 1
    for i in range(result, n + 1):
        result *= i
        print(result)
    return result


print("Using math Factorial", math.factorial(5))

print("Using mystery:", mystery(5))
