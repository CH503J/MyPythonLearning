"""
if_elif_else 组合使用语法
"""

"""
height = int(input("请输入你的身高："))
vip = int(input("请输入你的VIP等级："))

he = 120
v = 3
if height < he:
    print("身高小于120，可以免费游玩")
elif vip > v:
    print(f"VIP等级为：{vip}，可以免费游玩")
else:
    print("条件不满足，需要买票")
"""

num = 10
if int(input("请输入猜想的数字：")) == num:
    print("恭喜！第一次就猜对了")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你猜对了")
elif int(input("还是不对，再猜一次：")) == num:
    print("恭喜你猜对了")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你猜对了")
else:
    print(f"全都猜错了，我想的是{num}")
