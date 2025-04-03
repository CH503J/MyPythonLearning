# s：接收传入字符串，将字符串反转后返回
# x:下标
# y:下标

# 接收传入字符串，将字符串反转后返回
def str_reverse(s):
    re_s = s[::-1]
    return re_s


# 按照下标x和y对字符串进行切片
def substr(s, x, y):
    sub_str = s[x:y]
    return sub_str


if __name__ == '__main__':
    str1 = "abcdefg"
    print(f"原始字符串{str1}")
    new_str1 = str_reverse(str1)
    print(f'反转后的字符串为：{new_str1}')

if __name__ == '__main__':
    str2 = "abcdefg"
    print(f"原始字符串{str2}")
    new_str2 = substr(str2, 1, 4)
    print(f'切片后的字符串为：{new_str2}')