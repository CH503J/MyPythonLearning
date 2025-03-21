"""
数据容器-list列表
"""
"""
# 列表字面量
# ['zhansgan', 'lisi', 'wangwu']

# 定义变量
list1 = ['zhansgan', 'lisi', 'wangwu']

# 定义空列表
list2 = []
list()

# 定义一个列表并打印和查看类型
name_list = ['zhansgan', 'lisi', 'wangwu']
print(name_list)
print(type(name_list))

# 不同元素类型
my_list = ['zhansgan', 1, True]
print(my_list)
print(type(my_list))

# 定义一个嵌套列表
name_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(name_list)
print(type(name_list))

# 取出指定索引位的数据
print(name_list[1])
name = name_list[0]

print(name)

print(name_list[-1])

# name_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(name_list[3][-1])
"""

"""
list列表的常用操作
"""
"""
# 知道元素值，查找元素的下标索引
name_list = ['zhansgan', 'lisi', 'wangwu']
index = name_list.index('lisi')
print(index)

# 如果查找的元素不存在，程序会报错
name_list = ['zhansgan', 'lisi', 'wangwu']
index = name_list.index('hi')
print(index)

# 修改特定下标索引的值
name_list = ['zhansgan', 'lisi', 'wangwu']
name_list[0] = 'zhaoliu'
print(name_list)

# 插入元素
name_list = ['zhansgan', 'lisi', 'wangwu']
name_list.insert(1, 'zhaoliu')
print(name_list)

# 列表末尾追加元素
name_list = ['zhansgan', 'lisi', 'wangwu']
name_list.append('zhaoliu')
print(name_list)
# 将其他容器的数据全部追加到当前列表的末尾
name_list2 = [1, 2, 3]
name_list.extend(name_list2)
print(name_list)

name_list.append(name_list2)
print(name_list)


# 删除元素
# del 列表[下标]
name_list = ['zhansgan', 'lisi', 'wangwu']
del name_list[0]
print(name_list)
name = name_list.pop(1)
print(name, name_list)

# 删除某个列表中第一个匹配项
name_list = ['zhansgan', 'lisi', 'wangwu', 'lisi']
name_list.remove('lisi')
print(name_list)

# 清空列表
name_list = ['zhansgan', 'lisi', 'wangwu', 'lisi']
name_list.clear()
print(f'name_list列表清空后的值为：{name_list}')

# 统计列表中的元素个数
name_list = ['zhansgan', 'lisi', 'wangwu', 'lisi']
print(f"name_list列表中lisi的个数为：{name_list.count('lisi')}")

# 统计列表中所有的元素个数
name_list = ['zhansgan', 'lisi', 'wangwu', 'lisi']
count = len(name_list)
print(f"name_list列表中元素的个数为：{count}")
"""

# 小练习
"""
有一个列表[21, 25, 21, 23, 22, 20]，记录的是一批学生的年龄
通过列表的方法，对其进行
1、定义这个列表，并用变量接收它
2、追加一个数字31，到列表尾部
3、追加一个新列表[29， 33， 30]，到列表尾部
4、取出第一个元素
5、取出最后一个元素
6、查找元素31，在列表中的下标位置
"""
age_list = [21, 25, 21, 23, 22, 20]
print(f"定义的列表为：{age_list}")
age_list.append(31)
print(f"追加31到列表尾部，列表为：{age_list}")
age_list2 = [29, 33, 30]
age_list.extend(age_list2)
print(f"新列表追加后，列表为：{age_list}")
print(f"取出第一个元素{age_list[0]}后，列表为：{age_list}")
print(f"取出最后一个元素{age_list[-1]}后，列表为：{age_list}")
print(f"元素31在列表中的下标位置为：{age_list.index(31)}")