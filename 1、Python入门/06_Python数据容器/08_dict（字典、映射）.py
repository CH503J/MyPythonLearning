"""
字典
1.什么是字典
2.字典的常用操作
3.字典的特点
    - 可以容纳多个容器
    - 可以容纳不同类型的数据
    - 每一份数据都是一个键值对
    - 可以通过key获取value，key不可重复
    - 不支持下标索引
    - 可修改
    - 支持for循环
"""

# 1.字典的定义
# 字典同样使用大括号{}，不过字典的元素是一个一个键值对
# 字面量：{key:value, key:value, key:value, key:value}
# 变量：dict = {key:value, key:value, key:value, key:value}
# 空字典：dict()、{}


# 定义重复key的字典，字典与集合一样，字典的key是唯一的，但value可以重复
# 当字典中有重复的key时，在输出时，会覆盖之前的key对应的value
dict1 = {"张三": 18, "李四": 20, "王五": 22, "张三": 19}
print(f"字典dict1的值是：{dict1}")

# 从key获取value
dict1 = {"张三": 18, "李四": 20, "王五": 22, "赵六": 19}
print(f"字典dict1中张三对应的value是：{dict1['张三']}")

# 嵌套字典，字典的key和value可以是任意类型，但key不可以为字典
dict2 = {
    "张三": {
        "age": 18,
        "sex": "男"
    },
    "李四": {
        "age": 20,
        "sex": "女"
    },
    "王五": {
        "age": 22,
        "sex": "男"
    }
}

# 从嵌套字典中获取数据
print(f"字典dict2中张三的年龄是：{dict2['张三']['age']}")

# 2.字典的常用操作
# 2.1 新增和修改
dict3 = {"张三": 18, "李四": 20, "王五": 22, "赵六": 19}
dict3["张三"] = 19
print(f"字典dict3中张三长了一岁：{dict3}")

dict3["赵七"] = 20
print(f"赵七加入了字典dict3：{dict3}")

# 2.2 删除
dict4 = {"张三": 18, "李四": 20, "王五": 22, "赵六": 19}
dict4.pop("赵六")
print(f"字典dict4中赵六被删除了：{dict4}")

# 2.3 清空字典
dict4.clear()
print(f"字典dict4被清空了：{dict4}")

# 2.4 获取字典中所有的key
dict5 = {"张三": 18, "李四": 20, "王五": 22, "赵六": 19}
dict5_keys = dict5.keys()
print(f"字典dict5中所有的key是：{dict5_keys}，类型是：{type(dict5_keys)}")

# 2.5 遍历字典
dict6 = {"张三": 18, "李四": 20, "王五": 22, "赵六": 19}
dict6_keys = dict6.keys()
# 方法一：通过获取全部的key来遍历
for key in dict6_keys:
    print(f"字典dict6中key是：{key}，value是：{dict6[key]}")

# 方法二：直接对字典进行for循环
for key in dict6:
    print(f"字典dict6中key是：{key}，value是：{dict6[key]}")

# 2.6 统计字典的元素数量
dict7 = {"张三": 18, "李四": 20, "王五": 22, "赵六": 19}
dict7_len = len(dict7)
print(f"字典dict7的元素数量是：{dict7_len}")

# 4.小练习
worker = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

print(f"全体员工当前信息如下：{worker}")
for name in worker:
    if worker[name]["级别"] == 1:
        worker[name]["级别"] = 2
        worker[name]["工资"] += 1000

print(f"全体员工级别为1的员工完成升职加薪操作，操作后：{worker}")
