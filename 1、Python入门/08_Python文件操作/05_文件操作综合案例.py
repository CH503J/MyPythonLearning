"""
有一份账单文件bill.txt,记录了消费收入的具体记录
需求：
    1. 将文件写出到bill.txt.bak进行备份
    2. 备份时将标记为测试的数据丢弃

在这个需求中，虽然两个for循环的处理结果一样，但是细节问题同样需要考虑
    1.写法一最大的优点是直接实现了效果，不在乎一些细节问题，因为最终需求就是将带有测试的数据不进行备份，
      但同时带有很多不确定性，比如行中测试不在预期位置时，写法一就会将这一条数据进行误删
    2.写法二的优点就是考虑全面，首位空格、统一换行符、指定字段进行过滤，写法二避免了写法一的各种问题
    很多情况下推荐写法二，写法一只适合用来写一些demo、测试一类的代码，项目中不适用
"""

file_path = "C:/Develop/PythonProjects/MyPythonLearning/1、Python入门/08_Python文件操作/test/bill.txt"
new_file_path = "C:/Develop/PythonProjects/MyPythonLearning/1、Python入门/08_Python文件操作/test/bill.txt.bak"

file = open(file_path, 'r', encoding='utf-8')
new_file = open(new_file_path, 'w', encoding='utf-8')

# 写法一
for line in file:
    if "测试" not in line:
        new_file.write(line)

file.close()
new_file.close()

# 写法二：推荐写法
for line in file:
    line = line.strip()
    if line.split(",")[4] == "测试":
        continue
    new_file.write(line)
    new_file.write("\n")

file.close()
new_file.close()
