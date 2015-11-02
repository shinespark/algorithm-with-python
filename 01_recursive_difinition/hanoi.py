# coding: utf-8


def hanoi(n, from_, to, via):
    if n == 1:
        print('{0} => {1}'.format(from_, to))
    else:
        hanoi(n - 1, from_, via, to)
        print('{0} => {1}'.format(from_, to))
        hanoi(n - 1, via, to, from_)


if __name__ == "__main__":
    hanoi(3, 'a', 'b', 'c')
