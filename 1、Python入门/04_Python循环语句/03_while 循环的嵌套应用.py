"""
while 循环的嵌套应用
"""

i = 1
while i <= 100:
    print(f"今天是第{i}天，准备讲价")
    j = 1
    while j <= 10:
        print(f"送出第{j}朵玫瑰花")
        j += 1

    print("小妹，便宜点")
    i += 1

print(f"坚持到第{i-1}天，小妹给打了对折")
