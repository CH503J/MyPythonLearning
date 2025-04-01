# 一个函数中调用了另一个函数

def a():
    print("---2---")


def b():
    print("---1---")
    a()
    print("---3---")


b()
