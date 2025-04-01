"""
元组tuple
1. 元组的定义格式
2. 元组的特点
    2.1 元组一旦定义完成，就不可被修改，所以当需要在程序内封装数据又不希望封装的数据被修改就可以使用元组封装
3. 元组的常见操作
"""

"""
1. 定义元组
    1.1 元组字面量
    (元素, 元素, 元素, .....,元组)
    1.2 元组变量
    变量名 = (元素, 元素, 元素, .....,元组)
    1.3 空元组
    方式一： 变量名 = ()
    方式二： 变量名 = tuple()
"""

# 定义元组
t1 = (1, "你好", True, [1, 2, 3])
t2 = ()
t3 = tuple()

print(f"t1的类型是{type(t1)}, 内容是{t1}")
print(f"t2的类型是{type(t2)}, 内容是{t2}")
print(f"t3的类型是{type(t3)}, 内容是{t3}")

# 定义单个元素的元组
t4 = (1,)
# 要注意的是，如果元组中的元素只有一个时，需要在元素后面加上逗号，否则就是这个元素的类型
print(f"t4的类型是{type(t4)}, 内容是{t4}")

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是{type(t5)}, 内容是{t5}")
print(f"t5中最后一个元素的类型是{type(t5[1][2])}, 内容是{t5[1][2]}")

# 根据下标索引取出元组中的元素
t6 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"元组t6中的第4个元素是{t6[3]}")

# 元组的常用操作
# 1.index查找方法
t7 = ('zhangsan', 'lisi', 'wangwu', 'zhaoiu')
index = t7.index('wangwu')
print(f"在元组t7中wangwu的下标是{index}")

# 2.count统计方法
t8 = ('zhangsan', 'lisi', 'wangwu', 'zhaoiu', 'wangwu', 'zhaoiu', 'wangwu')
count = t8.count('wangwu')
print(f"在元组t8中wangwu出现的次数是{count}")

# 3.len函数统计元素长度
t9 = ('zhangsan', 'lisi', 'wangwu', 'zhaoiu', 'wangwu', 'zhaoiu', 'wangwu')
num = len(t9)
print(f"元组t9中元素个数是{num}")

# 4.while循环遍历
t10 = ('zhangsan', 'lisi', 'wangwu', 'zhaoiu', 'wangwu', 'zhaoiu', 'wangwu')
index = 0
while index < len(t10):
    print(f"元组t10中的第{index + 1}个元素是：{t10[index]}")
    index += 1

# 5.for循环遍历
t11 = ('zhangsan', 'lisi', 'wangwu', 'zhaoiu', 'wangwu', 'zhaoiu', 'wangwu')
for index in t11:
    print(f"元组t11中的元素有：{index}")

# 修改元组内容
t12 = ('zhangsan', 'lisi', 'wangwu', ['zhaoiu', 'wangwu', 'zhaoiu', 'wangwu'])
# t12[0] = '123'
print(f"元组t12中的元素有{t12}")
t12[3][0] = '123'
print(f"元组t12中的元素有{t12}")

stu = ('周杰伦', 11, ['football', 'music'])
age = stu.index(11)
print(f'年龄所在下标位置为:{age}')
name = stu[0]
print(f'姓名为:{name}')
stu[2][1] = 'coding'
print(f'爱好是:{stu[2]}')
