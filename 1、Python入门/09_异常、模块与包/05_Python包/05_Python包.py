"""
Python包
    1. 自定义包
        为什么需要Python包
            - Python中的模块非常丰富，如果任其发展会造成混乱的模块管理，Python包就是专门用来管理模块的
        1.1 什么是自定义Python包
            - Python包在现实意义上看就是一个文件夹，文件夹中管理着一个或多个Python模块
            - Python包中有一个__init__.py的文件，从逻辑上看，Python包的本质依然是一个模块
            - __init__: 如果一个Python包中没有__init__.py文件，那么这个Python包只是一个普通的文件夹，也就是说有__init__文件的才是Python包，没有的都是普通文件夹
        1.2 如何自定义包
    2. 安装第三方包
"""
# 导入包的几种方式
# from package.module import function
# import package.module
# from package import module

# 通过__all__变量来控制模块的导入
# from my_package import *

# my_module1.test()


# 2. 什么是第三方包
