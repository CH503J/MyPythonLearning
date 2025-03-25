"""
字符串常用操作
"""

# 1.通过索引取值
my_str = "hello world and bye world"
val1 = my_str[2]
val2 = my_str[-3]
print(f'val1:{val1}')
print(f'val2:{val2}')

# 2.index方法
index = my_str.index("and")
print(f'字符串my_str中and的起始下标是:{index}')

# 3.replace方法
new_str = my_str.replace("world", "python")
print(f'替换后的字符串是:{new_str}')

# 4.split方法
str1 = "hello world and bye world"
print(f'str1切分的结果是:{str1.split()}')
print(str1)

# 5.strip方法
str2 = "    12hello world and bye world21    "
# 不传参数，默认去除空格
new_str2 = str2.strip()
print(f'new_str2的规整操作后是:{new_str2}')
# 传入参数，去除指定的字符
new_str3 = str2.strip(" 12hello")
print(f'new_str3的规整操作后是:{new_str3}')

# 6.统计字符串中某一个字符的次数
str4 = "hello world and bye world"
count = str4.count('o')
print(f'字符串str4中o的个数是:{count}')

# 7.字符串长度
str5 = "hello world and bye world"
length = len(str5)
print(f'字符串str5的长度是:{length}')

# 8.遍历打印字符串
str6 = "hello world and bye world"
index = 0
while index < len(str6):
    print(f'while循环str6中第{index + 1}个字符是:{str6[index]}')
    index += 1

for i in str6:
    print(f'for循环str6中的字符有:{i}')

"""
- 给定一个字符串”itheima itcast boxuegu”
    - 统计字符串中有多少个”it”字符
    - 将字符串中的空格全部替换为字符”|”
    - 并按照字符”|”进行分隔，得到列表
"""
test_str = "itheima itcast boxuegu"
print(f'test_str中it的个数是:{test_str.count("it")}')
new_test_str = test_str.replace(" ", "|")
print(f'test_str中的空格替换为|后的结果为：{new_test_str}')
print(f'test_str按照|分割后的结果为：{new_test_str.split("|")}')
