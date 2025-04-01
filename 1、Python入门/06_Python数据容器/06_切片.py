"""
数据容器（序列）
序列是指内容连续、有序、可使用下标索引的一类数据容器；列表、元组、字符串都可以视为序列
"""
# 什么是序列
# 序列[起始下标:结束下标:步长]


# 序列的切片
# 对list切片,从1开始到5结束，步长为1
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list1 = list1[1:5]
print(f"新list1的值是：{new_list1}")

# 对tuple切片，从头开始到末尾结束，步长为1
tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
new_tuple1 = tuple1[:]
print(f"新tuple1的值是：{new_tuple1}")

# 对str切片，从头开始到尾结束，步长为2
str1 = "0123456789"
new_str1 = str1[::2]
print(f"新str1的值是：{new_str1}")

# 对str切片，从头开始到尾结束，步长为-1
str2 = "0123456789"
new_str2 = str2[::-1]
print(f"新str2的值是：{new_str2}")

# 对list切片，从3开始到1结束，步长-1
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list2 = list2[3:1:-1]
print(f"新list2的值是：{new_list2}")

# 对tuple切片，从头开始到尾结束，步长-2
tuple2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
new_tuple2 = tuple2[::-2]
print(f"新tuple2的值是：{new_tuple2}")
