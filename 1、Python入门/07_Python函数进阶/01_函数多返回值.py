"""
函数多返回值
"""


# 1.return多个返回值
def test():
    return 1, "2", {3}


x, y, z = test()
print(f'test函数的返回值中x={x}；y={y}；z={z}')
