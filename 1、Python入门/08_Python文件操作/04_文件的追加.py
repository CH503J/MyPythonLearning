"""
文件追加（继续在文件原始内容后续写）
注意：
    1. 追加模式中，目标文件必须已存在，写入内容会在目标文件的最后继续写入
"""

file_path = "C:/Develop/PythonProjects/MyPythonLearning/1、Python入门/08_Python文件操作/test/追加.txt"
# 读取文件
file = open(file_path, 'a', encoding='utf-8')

# 写入内容
file.write("你好Python，再见Python")

# 刷新内容
file.flush()

# 关闭文件
file.close()
