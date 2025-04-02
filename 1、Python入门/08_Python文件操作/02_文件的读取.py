"""
文件的读取
1. 打开/创建文件
2. 读取
3. 关闭
"""
import time

file_path = "C:/Develop/PythonProjects/MyPythonLearning/1、Python入门/08_Python文件操作/test/读取.txt"
# 打开文件
file = open(file_path, 'r', encoding='utf-8')
print(type(file))

# 读取文件 .read()
print(f"从python_file.txt中读取10个字节的结果：{file.read(10)}")

print("=============================================================================")

# 读取文件 .readline()
lines = file.readlines()
print(f"readlines的类型是：{type(file.readlines())}")
print(f"从python_file.txt中读取一行的结果：{lines}")

# 读取文件 .readline()
line = file.readline()
print(f"readline的类型是：{type(file.readline())}")
print(f"从python_file.txt中读取一行的结果：{line}")

# for 循环遍历文件
for line in open(file_path, 'r', encoding='utf-8'):
    print(line)

# 文件关闭
file.close()

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        print(line)

list1 = file.read()
count = list1.count('itheima')
print(f'itheima出现的次数是：{count}')

count = 0
for line in file:
    line.strip()
    words = line.split()
    for word in words:
        if word == 'itheima':
            count += 1


print(f'itheima出现的次数是：{count}')

file.close()