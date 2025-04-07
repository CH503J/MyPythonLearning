"""
常用魔术方法
__str__()   字符串方法
__lt__()    小于大于比较方法
__le__()    小于等于、大于等于比较方法
__eq__()    ==比较方法
"""
from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__()
    def __str__(self):
        return f'学生姓名：{self.name}，年龄：{self.age}'

    # __lt__()
    def __lt__(self, other):
        return self.age < other.age

    # __le__()
    def __le__(self, other):
        return self.age <= other.age


# __str__()
stu = Student('张三', 18)
print(stu)
print(str(stu))
print(stu.__str__())

# __lt__()
stu1 = Student('张三', 22)
stu2 = Student('李四', 20)
print(stu1 < stu2)
print(stu1.__lt__(stu2))

# __le__()
stu1 = Student('张三', 20)
stu2 = Student('李四', 20)
print(stu1 >= stu2)
