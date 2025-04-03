# file name：接收文件路径
# data：传入数据

# 接收传入文件路径，打印文件全部内容
# 如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
def print_file_info(file_name):
    file = None
    try:
        file = open(file_name, "r", encoding="utf-8")
        print(file.read())
    except FileNotFoundError:
        print(f'文件{file_name}不存在')
    finally:
        try:
            file.close()
        except Exception as e:
            print(f'文件关闭失败，原因：{e}')


# 接收文件路径以及传入数据，将数据追加写入到文件中
def append_to_file(file_name, data):
    file = open(file_name, "a", encoding="utf-8")
    file.write(data)
    print(f'{data}追加成功')
    return file.close()


if __name__ == '__main__':
    file_path = "C:/Develop/PythonProjects/MyPythonLearning/1、Python入门/08_Python文件操作/test/读.txt"
    print(print_file_info(file_path))

if __name__ == '__main__':
    file_path = "C:/Develop/PythonProjects/MyPythonLearning/1、Python入门/08_Python文件操作/test/追加.txt"
    append_to_file(file_path, "你好\n你好")
