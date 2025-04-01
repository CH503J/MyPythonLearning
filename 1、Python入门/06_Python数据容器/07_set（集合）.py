"""
集合
1.集合的基本定义
2.集合的特点：元素不可重复
3.集合的常见操作
"""
# 1.集合的基本定义
# 集合字面量：{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 集合变量：set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 空集合：set2 = ()

# 2.集合的特点：元素不可重复
set1 = {"hello", 'hi', 'hi', "hello", '你好', "python", "python", '你好', "hello", 'hi', "hello"}
print(f'set1集合的元素是：{set1}，类型是{type(set1)}')

# 3.集合的常见操作
# 3.1 添加元素
set2 = {"hello", 'hi', 'hi', "hello", '你好', "python", "python", '你好', "hello", 'hi', "hello"}
set2.add(11)
print(f'添加元素11后的集合是：{set2}')

# 3.2 删除元素
set2.remove(11)
print(f'删除元素11后的集合是：{set2}')

# 3.3 随机取出一个元素
print(f'随机取出一个元素是：{set2.pop()}，取出后的集合为：{set2}')
print(f'随机取出一个元素是：{set2.pop()}，取出后的集合为：{set2}')

# 3.4 清空集合
set2.clear()
print(f'清空集合后的集合为：{set2}')

# 3.5 取两个集合的差集，集合的差集是集合A中存在，集合B中不存在的元素
# 集合的差集操作的是集合A，集合B只是用来进行对比
set3 = {1, 3, 5, 7, 9}
set4 = {1, 2, 4, 6, 8, 10}
set5 = set3.difference(set4)
print(f'set3和set4的差集是：{set5}')

# 3.6 消除两个集合的差集，消除差集是消除集合A中存在，集合B中不存在的元素，而集合B不变
set6 = set3.difference_update(set4)
print(f'消除set3和set4的差集后的集合是：{set3}')
print(f'消除set3和set4的差集后的集合是：{set4}')

# 3.7 集合合并，合并时先创建一个新集合，然后将两个集合中的元素依次取出，插入新集合时计算哈希值，如果哈希值相同，则不插入新集合
set7 = {1, 2, 3, 4, 5, 6, 7}
set8 = {3, 4, 5, 6, 7, 8, 9}
set9 = set7.union(set8)
print(f'集合合并后的集合是：{set9}')
print(set7)
print(set8)

# 3.8 集合的长度
set10 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f'集合的长度是：{len(set10)}')

# 3.9 集合的遍历
for i in set10:
    print(i)

# 这里不使用下标是因为集合是无序的，而且.pop方法是随机取出一个元素，使用.pop遍历是随机取出元素而不是读取元素
while set10:
    print(set10.pop())