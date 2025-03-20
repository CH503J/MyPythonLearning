"""
函数如何传参呢？
"""


def add(i, j):
    return i + j


a = 10
b = 20
print(add(a, b))


def virus(thermal):
    if 37.3 >= thermal >= 36.5:
        return print(f"欢迎来到XXX，清楚您的健康码及72小时核酸证明，并配合测量体温! \n 体温测量中，您的体温是{thermal}度，体温正常请进！")
    else:
        return print(f"欢迎来到XXX，清楚您的健康码及72小时核酸证明，并配合测量体温! \n 体温测量中，您的体温是{thermal}度，我要报警给你抓起来")


virus(35)
