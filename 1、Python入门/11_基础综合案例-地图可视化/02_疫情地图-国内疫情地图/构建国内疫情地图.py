# 导包
import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

name_map = {
    "北京市": "北京",
    "天津市": "天津",
    "河北省": "河北",
    "山西省": "山西",
    "内蒙古自治区": "内蒙古",
    "辽宁省": "辽宁",
    "吉林省": "吉林",
    "黑龙江省": "黑龙江",
    "上海市": "上海",
    "江苏省": "江苏",
    "浙江省": "浙江",
    "安徽省": "安徽",
    "福建省": "福建",
    "江西省": "江西",
    "山东省": "山东",
    "河南省": "河南",
    "湖北省": "湖北",
    "湖南省": "湖南",
    "广东省": "广东",
    "广西壮族自治区": "广西",
    "海南省": "海南",
    "重庆市": "重庆",
    "四川省": "四川",
    "贵州省": "贵州",
    "云南省": "云南",
    "西藏自治区": "西藏",
    "陕西省": "陕西",
    "甘肃省": "甘肃",
    "青海省": "青海",
    "宁夏回族自治区": "宁夏",
    "新疆维吾尔自治区": "新疆",
    "香港特别行政区": "香港",
    "澳门特别行政区": "澳门",
    "台湾省": "台湾",
    "内蒙古": "内蒙古",
}

# 读取数据文件
file_path = r"C:\Develop\PythonProjects\MyPythonLearning\1、Python入门\11_基础综合案例-地图可视化\02_疫情地图-国内疫情地图\疫情.txt"
file = open(file_path, 'r', encoding='utf-8')
data = file.read()

# 关闭文件
file.close()

# 取到各省数据
# 将Json转换为Python字典
data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
# print(province_data_list)

# 组装各个省份和确诊人数为元组，并将省份数据封装到列表
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    confirm = province_data["total"]["confirm"]
    data_list.append((province_name, confirm))

print(data_list)
# 创建地图对象
map = Map()

# 添加数据
map.add("国内疫情地图", data_list, "china", name_map=name_map)

# 设置全局配置，定制分段视觉映射
map.set_global_opts(
    title_opts={"title": "全国地图"},
    visualmap_opts=VisualMapOpts(
        is_show=True,
        max_=1500,
        min_=0,
        is_piecewise=False,
        range_color=["#FFB0B0FF", "#FF8686FF", "#FF4545FF", "#FD1C1CFF", "#910303FF", "#530000FF"]
    )
)

# 绘图
map.render("全国疫情确诊人数图.html")


