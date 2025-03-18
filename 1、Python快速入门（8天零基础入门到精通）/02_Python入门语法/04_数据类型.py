# # Python中不用定义变量的数据类型（变量无类型而数据有类型）（与Java不同，Java需要在新建变量对象时指定数据类型），那么怎么验证数据的类型呢
# 666
# 13.14
# "黑马程序员"
#
# print(type(666))
# print(type(13.14))
# print(type("黑马程序员"))

string_type = type("黑马程序员")
int_type = type(666)
float_type = type(13.14)

print(string_type)
print(int_type)
print(float_type)
