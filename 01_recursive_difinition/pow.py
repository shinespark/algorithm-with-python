# coding: utf-8
import math
import time


def pow1(x, n):
    value = 1
    while n > 0:
        value *= x
        n -= 1

    return value


def pow2(x, n):
    if n == 0:
        return 1

    value = pow2(x, n // 2)
    value *= value

    if n % 2 == 1:
        value *= x

    return value


def pow3(x, n):
    value = 1
    while n > 0:
        if n & 1:  # odd
            value *= x
        n >>= 1
        x *= x

    return value


if __name__ == "__main__":
    start = time.clock()
    print(math.pow(2, 8))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')

    start = time.clock()
    print(pow1(2, 8))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')

    start = time.clock()
    print(pow2(2, 8))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')

    start = time.clock()
    print(pow3(2, 8))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')

    start = time.clock()
    print(2 ** 8)
    end = time.clock()
    print("{0:f}".format(end - start) + 's')
