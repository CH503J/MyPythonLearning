money = 5000000
name = None

name = input("请输入您的姓名：\n")


# 查询函数
def search():
    print("======余额查询======")
    print(f"{name}您好，您的余额剩余{money}元")


def add(num):
    global money
    money += num
    print("========存款========")
    print(f"{name}，您好，您存款{num}元成功！您现在的余额为：{money}")


def get(num):
    global money
    money -= num
    print("========取款========")
    print(f"{name},您好，您成功取款{num}元！您现在的余额为：{money}")


def menu():
    while True:
        print(f"{name}，您好，欢迎使用ATM，请选择业务：\n查询余额\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]")
        choice = int(input("请输入您的选择："))
        if choice == 1:
            search()
        elif choice == 2:
            print("请输入您像存款的钱数")
            add(int(input()))
        elif choice == 3:
            print("请输入您像存款的钱数")
            get(int(input()))
        elif choice == 4:
            print("已退出ATM系统")
            break
        else:
            print("输入业务指令不正确，已退出ATM系统")
            break


menu()
