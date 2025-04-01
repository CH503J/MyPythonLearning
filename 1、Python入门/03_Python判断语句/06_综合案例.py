import random

num = random.randint(1, 10)

gue_num = int(input("请输入猜测的数字"))

if gue_num == num:
    print(f"猜对啦,随机数字是：{num}")
else:
    print("猜错啦")
    if gue_num > num:
        print("猜测数字比随机数字大")
    else:
        print("猜测数字比随机数字小")

    gue_num = int(input("请再猜一次"))
    if gue_num == num:
        print(f"猜对了,随机数字是：{num}")
    else:
        print("又猜错了")
        if gue_num > num:
            print("猜测的数字还是比随机数大")
        else:
            print("猜测数字比随机数小哦")
        gue_num = int(input("第三次猜测"))
        if gue_num == num:
            print(f"第三次猜对了，随机数是：{num}")
        else:
            print(f"还是错了，机会用完了，随机数是：{num}")