# coding: utf-8
import time


def tarai(x, y, z):
    if x <= y:
        return y
    return tarai(tarai(x - 1, y, z), tarai(y - 1, z, x), tarai(z - 1, x, z))


table = {}  # メモ用の辞書


def tarai2(x, y, z):
    global table
    key = (x, y, z)
    if key not in table:
        if x <= y:
            table[key] = y
        else:
            table[key] = tarai(tarai(x - 1, y, z),
                               tarai(y - 1, z, x),
                               tarai(z - 1, x, z))
    return table[key]


# メモ化関数
def memorize(f):
    table = {}

    def func(*args):
        if args not in table:
            table[args] = f(*args)
        return table[args]
    return func


@memorize
def tarai3(x, y, z):
    if x <= y:
        return y
    return tarai(tarai(x - 1, y, z),
                 tarai(y - 1, z, x),
                 tarai(z - 1, x, y))


class Memorize:
    def __init__(self, func):
        self.table = {}
        self.f = func

    def __call__(self, *args):
        if args not in self.table:
            self.table[args] = self.f(*args)
        return self.table[args]


@Memorize
def tarai4(x, y, z):
    if x <= y:
        return y
    return tarai(tarai(x - 1, y, z),
                 tarai(y - 1, z, x),
                 tarai(z - 1, x, y))


#  def tarai5(x, y, z):
#      if x <= y:
#          return y
#      zz = z()
#      return tarai(tarai(x - 1, y, lambda: zz),
#                   tarai(y - 1, zz, lambda: x),
#                   lambda: tarai(zz - 1, x, lambda: y))


def tarai_lazy(x, y, xx, yy, zz):
    if x <= y:
        return y
    z = tarai(xx, yy, zz)
    return tarai_lazy(tarai6(x - 1, y, z),
                      tarai6(y - 1, z, x),
                      z - 1,
                      x,
                      y)


def tarai6(x, y, z):
    if x <= y:
        return y
    return tarai_lazy(tarai(x - 1, y, z),
                      tarai(y - 1, z, x),
                      z - 1, x, y)


if __name__ == "__main__":
    start = time.clock()
    print(tarai(12, 6, 0))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')

    start = time.clock()
    print(tarai2(12, 6, 0))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')

    start = time.clock()
    print(tarai3(12, 6, 0))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')

    start = time.clock()
    print(tarai4(12, 6, 0))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')

    #  start = time.clock()
    #  print(tarai5(12, 6, 0))
    #  end = time.clock()
    #  print("{0:f}".format(end - start) + 's')

    start = time.clock()
    print(tarai6(12, 6, 0))
    end = time.clock()
    print("{0:f}".format(end - start) + 's')
