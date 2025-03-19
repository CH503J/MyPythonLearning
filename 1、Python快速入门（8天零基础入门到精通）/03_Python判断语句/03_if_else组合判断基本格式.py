"""
if_else组合判断基本句式
"""
age = int(input("请输入您的年龄："))
if age >= 18:
    print("您已成年，需要买票！")
else:
    print('您未成年，可以免费游玩！')
print("祝您玩的开心")


# 练习案例
height = 120
print("欢迎来到动物园。")
he = int(input("请输入您的身高："))
if he >= height:
    print(f"您的身高为：{he}，需要买票")
else:
    print(f"您的身高为：{he}，可以免费游玩")
