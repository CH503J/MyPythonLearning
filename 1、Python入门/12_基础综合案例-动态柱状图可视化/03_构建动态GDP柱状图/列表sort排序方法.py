"""
扩展列表常用方法sort()
"""

my_list = [['zhangsan', 22], ['lisi', 33], ['wangwu', 44], ['zhaoliu', 55]]

# lambda匿名函数表达式
my_list.sort(key=lambda element: element[1], reverse=True)


def choose_sort_key(element):
    return element[1]


# 函数式
my_list = my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)
