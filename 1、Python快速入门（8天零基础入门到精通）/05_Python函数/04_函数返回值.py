"""
函数的返回值
"""


# def add(a, b):
#     return a + b
#
#
# r = add(5, 6)
#
# print(r)


# 无return语句的函数返回值
def hi():
    print("你好")


result = hi()
print(f"无return语句的函数返回值是：{result}")
print(f"无return语句的函数返回值类型是：{type(result)}")
