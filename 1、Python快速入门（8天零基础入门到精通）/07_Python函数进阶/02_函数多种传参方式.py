"""
函数的多种传参方式
1. 位置参数
2. 关键字参数
3. 不定长参数
4. 缺省参数
"""


# 1. 位置参数
def test1(a, b, c):
    print(a, b, c)


test1(1, 2, 3)
print("=========================")


# 2. 关键字参数
def test2(a, b, c):
    print(a, b, c)


test2(108, c=100, b=99)
print("=========================")


# 3.不定长参数
# 位置传递
def test3(*a):
    print(a)


test3(1, 2, 3, 4, 5, 6, 7, 8, 9)


# 关键字传递
def test3_1(**a):
    print(a)


test3_1(a=1, b=2, c=3)
print("=========================")


# 4. 缺省参数
def test4(a, b, c=100):
    print(a, b, c)


test4(1, 2)
test4(1, 2, 3)
