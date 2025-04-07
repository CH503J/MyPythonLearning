"""
演示面向对象的类、对象、成员变量、成员方法之间的关系
"""


# 设计一个闹钟类
class AlarmClock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)  # 声音频率不是响起频率， 持续时间


# 构建两个闹钟对象并使其工作
if __name__ == '__main__':
    clock1 = AlarmClock()
    clock1.id = 1
    clock1.price = 100
    print(f'闹钟{clock1.id}的价格是{clock1.price}，正在响')
    clock1.ring()
    clock2 = AlarmClock()
    clock2.id = 2
    clock2.price = 200
    print(f'闹钟{clock2.id}的价格是{clock2.price}，正在响')
    clock2.ring()