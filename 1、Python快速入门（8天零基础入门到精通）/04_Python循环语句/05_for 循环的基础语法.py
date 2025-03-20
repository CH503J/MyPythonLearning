"""
for 循环的基础语法
"""

# 在这段代码中，a就是一个临时变量，
# for a in name 就是把name变量中的每个值拿出来赋值给a
# 然后用print将a打印出来，当name中的值被取完，for循环就结束了
# 所以a是临时变量，生存周期随for循环开始而开始，随for循环结束而结束
name = "python"
for a in name:
    print(a)

name = "itheima is a brand of itcast"
num = 0
for a in name:
    if a == "a":
        num += 1

print(f"{name}中一共有{num}个a")

"""
range()的基本使用
"""
# range语法1
for a in range(10):
    print(a)

# range语法2
for a in range(5, 10):
    print(a)

# range语法3
for a in range(5, 10, 2):
    print(a)

"""
定义一个数字变量num，内容随意，使用range()语句，获取从1到num的序列，使用for循环统计有多少偶数
"""
num = range(1, 100)
count = 0

for a in num:
    if a % 2 == 0:
        count += 1

print(f"num中有{count}个偶数")

"""
for循环中临时变量的作用域
"""
i = 0
for i in range(5):
    print(i)

print(i)
