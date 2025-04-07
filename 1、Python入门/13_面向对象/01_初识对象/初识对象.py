# 设计一个类（设计一个登记表）
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None


# 创建一个对象（打印表格）
stu1 = Student()
stu2 = Student()

# 对象属性进行赋值
stu1.name = "张三"
stu1.gender = "男"

stu2.name = "李四"
stu2.gender = "女"

# 获取对象中记录的信息
print(stu1)
print(stu2)
print(stu1.name)
print(stu1.gender)
print(stu1.nationality)
print(stu2.name)
print(stu2.gender)
print(stu2.nationality)
