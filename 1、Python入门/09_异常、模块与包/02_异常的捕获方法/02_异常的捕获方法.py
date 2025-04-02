"""
异常的捕获方法
    1. 为什么要捕获异常
     - 世界上没有完美的程序，任何程序在运行过程中都有可能出现异常，而程序员要做的就是尽可能的力所能及的将可能出现的bug进行提前准备、提前处理。这就是异常处理（捕获异常）
    2. 捕获异常的基本语法
    try:
        可能发生异常的代码：
    except:
        如果出现异常执行的代码
"""

# 基本捕获语法
try:
    f = open('test.txt', 'r')
except:
    print("文件不存在")

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print(f"变量未定义{e}")

# 捕获多个异常
try:
    print(name)
    1 / 0
    f = open('test.txt', 'r')
    print(f.read())
except NameError:
    print("变量未定义")
except ZeroDivisionError:
    print("分母不能为0")
except (FileNotFoundError, IOError):
    print(f"未知异常")

# 未正确设置捕获异常类型，将无法捕获异常
# try:
#     1 / 0
# except NameError:
#     print("变量未定义")

# 捕获所有异常
try:
    1 / 0
except Exception:
    print("未知异常")

try:
    name = 'zhangsan'
except NameError as e:
    print(f"变量未定义{e}")
else:
    print(name)

# finally关键字
try:
    f = open(r"/1、Python入门/09_异常、模块与包/test/123.txt", 'r', encoding='utf-8')
except Exception as e:
    print("文件不存在，使用写模式打开")
    f = open(r"/1、Python入门/09_异常、模块与包/test/123.txt", 'w', encoding='utf-8')
else:
    print("文件存在，使用读模式打开")
finally:
    print("文件操作完成，关闭文件")
    f.close()
