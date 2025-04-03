"""
折线图开发
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, InitOpts, LabelOpts

in_file_path = r'C:\Develop\PythonProjects\MyPythonLearning\1、Python入门\10_基础综合案例-折线图可视化\数据准备\印度.txt'
jp_file_path = r'C:\Develop\PythonProjects\MyPythonLearning\1、Python入门\10_基础综合案例-折线图可视化\数据准备\日本.txt'
us_file_path = r'C:\Develop\PythonProjects\MyPythonLearning\1、Python入门\10_基础综合案例-折线图可视化\数据准备\美国.txt'
# 处理数据
file_in = open(in_file_path, 'r', encoding='utf-8')
in_data = file_in.read()

file_jp = open(jp_file_path, 'r', encoding='utf-8')
jp_data = file_jp.read()

file_us = open(us_file_path, 'r', encoding='utf-8')
us_data = file_us.read()

# 去掉不合Json规范的开头
in_data = in_data.replace('jsonp_1629350745930_63180(', '')
jp_data = jp_data.replace('jsonp_1629350871167_29498(', '')
us_data = us_data.replace('jsonp_1629344292311_69436(', '')

# 去掉不合Json规范的结尾
in_data = in_data[:-2]
jp_data = jp_data[:-2]
us_data = us_data[:-2]

# Json转Python字典
in_dict = json.loads(in_data)
jp_dict = json.loads(jp_data)
us_dict = json.loads(us_data)

# 获取trend key
in_dict = in_dict['data'][0]['trend']
jp_dict = jp_dict['data'][0]['trend']
us_dict = us_dict['data'][0]['trend']
# print(in_dict)

# 获取日期数据，用于x轴，取2020年到315下标结束
us_x_date = us_dict['updateDate'][:315]
print(us_x_date)

# 获取确诊数据，用于y轴，取2020年到315下标结束
in_y_data = in_dict['list'][0]['data'][:314]
jp_y_data = jp_dict['list'][0]['data'][:314]
us_y_data = us_dict['list'][0]['data'][:314]
print(us_y_data)

# 生成折线图
us_file_path = r'C:\Develop\PythonProjects\MyPythonLearning\1、Python入门\10_基础综合案例-折线图可视化\数据准备\美日印2020年确诊人数折线图.html'
line = Line(
    init_opts=InitOpts(width="1000px", height="600px")
)
line.add_xaxis(us_x_date)
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.set_global_opts(
    title_opts=TitleOpts(title="印度、美国、日本2020年确诊人数折线图", pos_left="center", pos_bottom="1%"),
)
line.render(us_file_path)

file_in.close()
file_jp.close()
file_us.close()