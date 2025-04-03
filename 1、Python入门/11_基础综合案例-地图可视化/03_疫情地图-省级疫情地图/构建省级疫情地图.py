# 导包
import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

# 读取数据文件
file_path = r"C:\Develop\PythonProjects\MyPythonLearning\1、Python入门\11_基础综合案例-地图可视化\02_疫情地图-国内疫情地图\疫情.txt"
file = open(file_path, 'r', encoding='utf-8')
data = file.read()

# 关闭文件
file.close()

# 取到各省数据
# 将Json转换为Python字典
data_dict = json.loads(data)
city_data_list = data_dict["areaTree"][0]["children"][3]["children"]
print(city_data_list)

# 组装各个省份和确诊人数为元组，并将省份数据封装到列表
data_list = []
for city_data in city_data_list:
    city_name = city_data["name"] + "市"
    confirm = city_data["total"]["confirm"]
    data_list.append((city_name, confirm))

print(data_list)
# 创建地图对象
map = Map()

# 添加数据
map.add("国内疫情地图", data_list, "河南")

# 设置全局配置，定制分段视觉映射
map.set_global_opts(
    title_opts={"title": "河南省"},
    visualmap_opts=VisualMapOpts(
        is_show=True,
        max_=500,
        min_=0,
        is_piecewise=False,
        range_color=["#FFB0B0FF", "#FF8686FF", "#FF4545FF", "#FD1C1CFF", "#910303FF", "#530000FF"]
    )
)

# 绘图
map.render("河南省疫情确诊人数图.html")


