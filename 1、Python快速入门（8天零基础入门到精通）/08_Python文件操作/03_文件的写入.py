"""
文件的写入操作
注意：
    1. 直接调用write并不是将内容真正写入文件，而是将内容积攒在内存中，称之为缓冲区
    2. 当调用flush时，文件才会真正写入文件中
    3. 这是为了避免频繁操作硬盘，导致效率下降
"""

file_path = "C:/Develop/PythonProjects/MyPythonLearning/1、Python快速入门（8天零基础入门到精通）/08_Python文件操作/test/写入.txt"
# 打开文件
file = open(file_path, "w", encoding='utf-8')

# 文件写入
file.write("你好Python，再见Python")

# 内容刷新
file.flush()

# 关闭文件
file.close()

