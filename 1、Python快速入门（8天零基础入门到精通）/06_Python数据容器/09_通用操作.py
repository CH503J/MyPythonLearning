"""
通用操作
"""
# len()函数
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
str1 = "abcdefg"
set1 = {1, 2, 3, 4, 5}
dict1 = {"name": "张三", "age": 18, "gender": "男"}

# len()元素个数
print(f"list1的长度是：{len(list1)}")
print(f"tuple1的长度是：{len(tuple1)}")
print(f"str1的长度是：{len(str1)}")
print(f"set1的长度是：{len(set1)}")
print(f"dict1的长度是：{len(dict1)}")
print("================================================")

# max()最大元素
print(f"list1的最大元素是：{max(list1)}")
print(f"tuple1的最大元素是：{max(tuple1)}")
print(f"str1的最大元素是：{max(str1)}")
print(f"set1的最大元素是：{max(set1)}")
print(f"dict1的最大元素是：{max(dict1)}")
print("================================================")

# min()最小元素
print(f"list1的最小元素是：{min(list1)}")
print(f"tuple1的最小元素是：{min(tuple1)}")
print(f"str1的最小元素是：{min(str1)}")
print(f"set1的最小元素是：{min(set1)}")
print(f"dict1的最小元素是：{min(dict1)}")
print("================================================")

# 类型转换：容器转列表
print(f"list1的类型转换：{list(list1)}")
print(f"tuple1的类型转换：{list(tuple1)}")
print(f"str1的类型转换：{list(str1)}")
print(f"set1的类型转换：{list(set1)}")
print(f"dict1的类型转换：{list(dict1)}")
print("================================================")

# 类型转换：容器转元组
print(f"list1的类型转换：{tuple(list1)}")
print(f"tuple1的类型转换：{tuple(tuple1)}")
print(f"str1的类型转换：{tuple(str1)}")
print(f"set1的类型转换：{tuple(set1)}")
print(f"dict1的类型转换：{tuple(dict1)}")
print("================================================")

# 类型转换：容器转字符串
print(f"list1的类型转换：{str(list1)}")
print(f"tuple1的类型转换：{str(tuple1)}")
print(f"str1的类型转换：{str(str1)}")
print(f"set1的类型转换：{str(set1)}")
print(f"dict1的类型转换：{str(dict1)}")
print("================================================")

# 类型转换：容器转集合
print(f"list1的类型转换：{set(list1)}")
print(f"tuple1的类型转换：{set(tuple1)}")
print(f"str1的类型转换：{set(str1)}")
print(f"set1的类型转换：{set(set1)}")
print(f"dict1的类型转换：{set(dict1)}")
print("================================================")

# 容器排序 sorted(容器)
list2 = [1, 3, 2, 5, 4]
tuple2 = (1, 5, 2, 4, 3)
str2 = "acfedbhg"
set2 = {5, 1, 4, 2, 3}
dict2 = {"name": "张三", "age": 18, "gender": "男"}
print(f"list2的排序：{sorted(list2)}")
print(f"tuple2的排序：{sorted(tuple2)}")
print(f"str2的排序：{sorted(str2)}")
print(f"set2的排序：{sorted(set2)}")
print(f"dict2的排序：{sorted(dict2)}")

print("================================================")
# 容器排序 sorted(容器,[reverse = True])
print(f"list2的排序：{sorted(list2, reverse=True)}")
print(f"tuple2的排序：{sorted(tuple2, reverse=True)}")
print(f"str2的排序：{sorted(str2, reverse=True)}")
print(f"set2的排序：{sorted(set2, reverse=True)}")
print(f"dict2的排序：{sorted(dict2, reverse=True)}")
