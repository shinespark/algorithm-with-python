# coding: utf-8


def comb(n, r):
    if n == 0 or r == 0:
        return 1
    return comb(n, r - 1) * (n - r + 1) // r


def pascal(x):
    for n in range(0, x + 1):
        for r in range(0, n + 1):
            print(comb(n, r), end=" ")
        print('')


def comb1(n, m, a=None):
    if not a:
        a = []

    if m == 0:
        print(a)
    elif n == m:
        print(list(range(1, m + 1)) + a)
    else:
        comb1(n - 1, m, a)
        comb1(n - 1, m - 1, [n] + a)


def comb2(n, m):
    if m == 0:
        yield []
    elif n == m:
        yield list(range(1, m + 1))
    else:
        for a in comb2(n - 1, m):
            yield a
        for a in comb2(n - 1, m - 1):
            yield a + [n]


if __name__ == "__main__":
    pascal(10)
    comb1(5, 3)
    for x in comb2(5, 3):
        print(x)
