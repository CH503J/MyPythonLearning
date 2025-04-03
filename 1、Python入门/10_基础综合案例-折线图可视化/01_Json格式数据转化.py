"""
1. 什么是Json
    - Json是一种轻量级的数据交互格式。可以按照Json指定的格式组织和封装数据
    - 本质上Json是一个带有特定格式的字符串
    - 主要功能就是在在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互
2. 掌握对Json的数据转换
"""
import json

# 2. 掌握对Json的数据转换
# 准备列表，列表内每一个元素都是字典，将其转换为Json
data1 = [{"name": "张三", "age": 18, "gender": "男"}, {"name": "李四", "age": 20, "gender": "女"}]
data1 = json.dumps(data1, ensure_ascii=False)
print(f'将列表转换为Json：{data1}')

# 准备字典，将字典转换为Json
data2 = {"name": "李四", "age": 20, "gender": "女"}
data2 = json.dumps(data2, ensure_ascii=False)
print(f'将字典转换为Json：{data2}')

# 将Json字符串转换为Python中的列表
data3 = json.loads(data1)
print(f'将转换为Json的列表再转换回来：{data3}')

# 将Json字符串转换为Python中的字典
data4 = json.loads(data2)
print(f'将转换为Json的字典再转换回来：{data4}')