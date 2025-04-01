"""
判断语句的嵌套
"""
# print("欢迎来到动物园")
# if int(input("请告诉我你的身高：")) > 120:
#     print("身高超出限制，不可免费")
#     if int(input("请告诉我你的vip等级：")) > 3:
#         print("vip级别达标，可以免费")
#     else:
#         print("条件不满足，需要买票")
# else:
#     print("欢迎免费游玩")


age = 20
year = 3
level = 1
if age >= 18:
    print("成年了！")
    if age < 30:
        print("年龄达标")
        if year > 2:
            print("年龄和入职时间都达标，可以领取礼物")
        elif level > 3:
            print("年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，年龄达标，但是级别和入职时间不达标")
    else:
        print("不好意思，年龄太大")
else:
    print("不好意思，你未成年")