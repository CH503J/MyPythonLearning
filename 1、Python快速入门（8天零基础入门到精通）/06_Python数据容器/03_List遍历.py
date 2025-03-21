"""
list列表的遍历
"""


# 使用while循环遍历列表
def list_traversal_while(list_data):
    index = 0
    while index < len(list_data):
        print(f"while循环的遍历结果是：{list_data[index]}")
        index += 1


def list_traversal_for(list_data):
    for i in list_data:
        print(f'for循环的遍历结果是：{i}')


list_data = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']

list_traversal_for(list_data)
list_traversal_while(list_data)

# for循环
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

for i in old_list:
    if i % 2 == 0:
        new_list.append(i)

print(f"通过for循环，从列表{old_list}中取出偶数，组成新列表{new_list}")

# while循环
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
index = 0
while index < len(old_list):
    if old_list[index] % 2 == 0:
        new_list.append(old_list[index])
    index += 1


print(f"通过while循环，从列表{old_list}中取出偶数，组成新列表{new_list}")
