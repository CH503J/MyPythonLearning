"""
综合案例-发工资
"""
import random

money = 10000

for i in range(1, 21):
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}绩效分{score},低于5，跳过发工资")
        continue
    else:
        print(f"员工{i}领取了工资1000元")
        money -= 1000
        if money <= 0:
            break
print("工资发完了，下月再来哦")
