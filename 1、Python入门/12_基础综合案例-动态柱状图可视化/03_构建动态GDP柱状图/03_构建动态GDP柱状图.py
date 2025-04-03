# 导包
import json
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
file_path = r"C:\Develop\PythonProjects\MyPythonLearning\1、Python入门\12_基础综合案例-动态柱状图可视化\03_构建动态GDP柱状图\1960-2019全球GDP数据.csv"
file = open(file_path, "r", encoding="GBK")
# print(file.read())
data_lines = file.readlines()

# 关闭文件
file.close()

# 删除第一条数据（表格标题）
data_lines.pop(0)

# 将数据转换为字典存储
# {年份:[[国家， gdp]， [国家， gdp]],年份:[[国家， gdp]， [国家， gdp]]}
data_dict = {}
for data_line in data_lines:
    year = int(data_line.split(",")[0])
    country = data_line.split(",")[1]
    gdp = float(data_line.split(",")[2])

    try:
        data_dict[year].append([country, gdp])
    except:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict)

# 创建时间线对象
timeline = Timeline(
    init_opts=InitOpts(
        width="1000px",
        height="600px",
        theme=ThemeType.LIGHT,
        page_title="GDP柱状图",
    )
)
# 按照年份排序
sorted_year = data_dict.keys()
# for循环每年数据，基于每年数据，创建每年的bar对象
for year in sorted_year:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出该年前8的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(
            title=f"{year}年全球GDP柱状图",
            pos_left="10%",
            title_textstyle_opts=TextStyleOpts(color="#000000FF"),
        ),
    )
    timeline.add(bar, str(year))

# 在for中将每年的bar对象添加到时间线中

# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

# 绘图
timeline.render("1960年-2019年GDP柱状图.html")