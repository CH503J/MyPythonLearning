"""
函数的体验及开发和应用
"""
str1 = "zhangsan"
str2 = "lisi"
str3 = "wangwu"

# 不使用len()函数统计字符串的长度
count = 0
for i in str1:
    count += 1
print(count)

count = 0
for i in str2:
    count += 1
print(count)

count = 0
for i in str3:
    count += 1
print(count)


# 自定义函数统计字符串长度
def length(data):
    count = 0
    for _ in data:
        count += 1
    print(count)


length(str1)
length(str2)
length(str3)
