"""
布尔类型的定义和比较运算符

== 判断内容是否相等
!= 判断内容是否不相等
> 判断左侧内容是否大于右侧内容
< 判断左侧内容是否小于右侧内容
>= 判断左侧内容是否大于或等于右侧内容
<= 判断左侧内容是否小于或等于右侧内容
"""

# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False

print(f"bool_1变量的内容是：{bool_1}, 类型是：{type(bool_1)}")
print(f"bool_1变量的内容是：{bool_2}, 类型是：{type(bool_2)}")

# 比较运算符的使用
# 内容相等比较
num_1 = 10
num_2 = 10
print(f'10 == 10的结果是：{num_1 == num_2}')

num_1 = 10
num_2 = 15
print(f'10 != 15的结果是：{num_1 != num_2}')

name_1 = 'zhangsan'
name_2 = 'lisi'
print(f'name_1 == name_2的结果是：{name_1 == name_2}')

# 大于小于，大于等于小于等于的比较运算
num_1 = 10
num_2 = 5
print(f'10 > 5的结果是：{num_1 > num_2}')
print(f'10 < 5的结果是：{num_1 < num_2}')

num_1 = 10
num_2 = 10
print(f'10 <= 10的结果是：{num_1 <= num_2}')
print(f'10 >= 10的结果是：{num_1 >= num_2}')

num_1 = 10
num_2 = 11
print(f'10 <= 11的结果是：{num_1 <= num_2}')
print(f'10 >= 11的结果是：{num_1 >= num_2}')