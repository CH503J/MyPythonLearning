"""
循环中断：continue 和 break
"""
for i in range(1, 6):
    print("语句1")
    for j in range(6, 10):
        print("语句2")
        continue
        print("语句3")

    print("语句4")
