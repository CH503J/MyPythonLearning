"""
for 循环的嵌套应用
"""

# 手冲100天，每天冲10次
i = 0
for i in range(1, 101):
    print(f"今天是手冲第{i}天！")
    for j in range(1, 11):
        print(f"今天手冲的第{j}次")
    print("啊！！！！！！！！！！！")

print(f"第{i}天，终于是冲死了")

"""
用for循环打印输出九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j} \t", end='')
    print()
