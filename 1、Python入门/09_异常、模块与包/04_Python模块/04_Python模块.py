"""
Python模块
1. 模块的导入
    1.1 什么是Python模块
        - 模块就是一个Python文件，以.py结尾，模块能定义函数、类和变量，也包含可执行的代码；模块的作用就是实现一些功能，然后导入该模块直接使用它
    1.2 导入Python内置的模块
        - 模块在使用前需要先导入才能使用
            [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [ as 别名]
            - 模块导入中，[]包裹的部分都可以不写，但是import必须要写，这是导入模块的关键字
        - 常见的组合有
            - import 模块名
            - from 模块名 import 类、变量、方法等
            - from 模块名 import *
            - import 模块名 as 别名
            - from 模块名 import 功能名 as 别名
        - 模块导入中，[]包裹的部分都可以不写，但是import必须要写，这是导入模块的关键字
2. 自定义模块
"""
# 1.1 Python模块
# 1.2 导入Python内置的模块
# 使用import导入item模块使用sleep功能（函数）
# import time
#
# time.sleep(2)
#
# # 使用from导入item的sleep功能（函数）
# from time import sleep
#
# sleep(2)
#
# # 使用*导入item模块的全部功能
# # 与上面import time不同的是：上面import time在使用模块中的功能时需要用[模块名.功能名]，而from time import *在使用模块中的功能时只需要[功能名]
# from time import *
#
# sleep(5)
#
# # 使用as 给特定功能加上别名
# import time as tt
#
# tt.sleep(3)
#
# from time import sleep as ts
#
# ts(4)

# 2.自定义模块
# 2.1 导入自定义模块
# import my_module1
# from my_module1 import test

# num = test(1, 2)
# print(num)

# 2.2 导入不同模块的同功能
# from my_module1 import test as t1
# from my_module2 import test as t2

# num = t1(1, 2)

# 2.3 __main__变量
# import my_module1

# 2.4 __all__变量
# from my_module1 import *
from my_module1 import test
test(1,2)