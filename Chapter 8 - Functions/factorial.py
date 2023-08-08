import math


def mystery(n):
    result = 1
    for i in range(result, n + 1):
        result *= i
        print(result)
    return result


print("Using math Factorial", math.factorial(5))

print("Using mystery:", mystery(5))

int1 = 1
int2 = 1
float1 = 1.0
float2 = 1.0
print(int1 is int2)
print(float1 is float2)
print(5 == 5.0)
print(5 is 5.0)


def foo(x):
    print("point 2:", id(x))
    x.append(4)
    print("point 3:", id(x))


L = [1, 2, 3]
print("point 1:", id(L))
foo(L)
print("point 4:", id(L))
