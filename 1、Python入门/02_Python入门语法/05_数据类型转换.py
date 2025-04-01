# 将数字类型转换为字符串
num_str = str(11)
print(num_str, type(num_str))

float_str = str(11.11)
print(float_str, type(float_str))

# 将字符串转换为数字
num = int("11")
print(num, type(num))

num2 = float("11.11")
print(num2, type(num2))

# 任何数据都可以转换为字符串，但并不是所有字符串都可以转换为整数
num3 = int("黑马程序员")
print(num3, type(num3))

# 整数转浮点数(float类型默认带小数的，所以输出结果为11.0)
float_num = float(11)
print(float_num, type(float_num))

# 浮点数转整数(会直接取浮点数的整数部分，会丢失精度)
int_num = int(11.11)
print(int_num, type(int_num))
