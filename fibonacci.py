# coding: utf-8
import time


# 二重再帰
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# 末尾再帰
def fib2(n, a1=1, a2=0):
    if n < 1:
        return a1
    return fib2(n - 1, a1 + a2, a1)


# 繰り返し
def fib3(n):
    a1, a2 = 1, 0
    while n > 0:
        a1, a2 = a1 + a2, a1
        n -= 1
    return a1


if __name__ == "__main__":
    start = time.clock()
    print(fib(10))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')

    start = time.clock()
    print(fib2(10))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')

    start = time.clock()
    print(fib3(10))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')
