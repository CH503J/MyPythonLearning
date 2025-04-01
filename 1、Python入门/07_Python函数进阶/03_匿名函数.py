"""
匿名函数
1. 将函数作为参数传递给别的函数
2. lambda匿名函数
"""


# 1. 将函数作为参数传递给别的函数
def test1(test2):
    re = test2(100, 50)
    print(re)


def test2(x, y):
    re = x + y
    return re


def test3(x, y):
    re = x - y
    return re


test1(test2)
test1(test3)


# 2. lambda匿名函数
def test4(test5):
    re = test5(1, 3)
    return re


f = test4(lambda x, y: x + y)
print(f)
