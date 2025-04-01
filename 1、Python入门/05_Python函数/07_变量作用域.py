def a():
    num = 100
    print(num)


# print(num)


num = 100


def a():
    global a
    a = 200
    print(num)


def b():
    print(num)


a()
b()
print(num)
print(a)