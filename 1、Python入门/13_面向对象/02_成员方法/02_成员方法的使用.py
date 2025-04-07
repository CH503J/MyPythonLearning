"""
成员方法的定义和使用
"""


# 成员方法的定义和使用
class Student:
    name = None

    def say_hi(self):
        print(f'hi大家好，我是{self.name}')

    def say_hi2(self, msg):
        print(f'hi，大家好，我是{self.name}，{msg}')


stu1 = Student()
stu1.name = '张三'
stu1.say_hi()
stu1.say_hi2('很高兴认识大家')
