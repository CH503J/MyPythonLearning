"""
while循环的基础语法
"""
i = 0
while i < 100:
    print(f'PythonNB{i + 1}')
    i += 1

# 从1-100累加的和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1

print(f"和为：{sum}")