"""
设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
- 无限次机会，猜中为止
- 每次猜不中提示大了或小了
- 猜完后，提示猜了几次
"""

import random

rand_num = random.randint(1, 100)
flag = True
count = 0

while flag:
    guess = int(input("\n请输入猜测的数字："))
    count += 1
    if guess == rand_num:
        print("猜对了")
        flag = False
    else:
        if guess > rand_num:
            print("猜测数字大于随机数")
        else:
            print("猜测的数字小于随机数")

print(f"你总共猜测了：{count}次")
