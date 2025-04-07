"""
使用构造方法给成员变量赋值
"""


class Student:
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print('Student类创建了一个类对象')


stu1 = Student('张三', 18, '123456789')

print(f'{stu1.name}的年龄是{stu1.age}，手机号是{stu1.tel}')
