"""
演示字符串的三种定义方式
- 单引号定义
- 双引号定义
- 三引号定义
"""

# 单引号定义
name = '张三'
print(type(name))

# 双引号定义
name = "张三"
print(type(name))

# 三引号定义
name = """
zhangsan
lisi
wangwu
"""
print(type(name))

"""
字符串的拼接
"""
# 字符串字面量之间拼接
print("盟友知识产权" + "滁州来安县")

# 字符串变量的拼接
name = '张三'
add = '新安镇'
tel = '123'

print(name + add + tel)

"""
字符串格式化
"""
name = '张三'
age = 15
classNum = 2
print("姓名：%s；年龄：%s； 班级：%s" % (name, age, classNum))

"""
字符串格式化精度控制
"""
num1 = 11
num2 = 114.514
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是 ：%1d" % num1)
print("数字114.514宽度限制8，小数精度2，结果是 ：%8.2f" % num2)
print("数字114.514宽度不限制，小数精度2，结果是 ：%.2f" % num2)

"""
使用f"{变量}"的方式格式化字符串
"""

name = '张三'
age = 16
num = 114.514
print(f"姓名：{name}, 年龄：{age}, 恶臭代码：{num}")

"""
对表达式的格式化
"""
print('1 * 1的结果是： %d' % (1 * 1))
print(f'1 * 1的结果是{1 * 1}')
