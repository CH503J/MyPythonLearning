import random

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, InitOpts

map = Map(
    init_opts=InitOpts(width="1200px", height="800px")
)

data = [
    ("安徽省", random.randint(0, 150)),
    ("湖南省", random.randint(0, 150)),
    ("江西省", random.randint(0, 150)),
    ("福建省", random.randint(0, 150)),
    ("山东省", random.randint(0, 150)),
    ("河南省", random.randint(0, 150)),
    ("湖北省", random.randint(0, 150)),
    ("广东省", random.randint(0, 150)),
    ("广西壮族自治区", random.randint(0, 150)),
    ("海南省", random.randint(0, 150)),
    ("四川省", random.randint(0, 150)),
    ("云南省", random.randint(0, 150)),
    ("重庆市", random.randint(0, 150)),
    ("贵州省", random.randint(0, 150)),
    ("陕西省", random.randint(0, 150)),
    ("青海省", random.randint(0, 150)),
    ("甘肃省", random.randint(0, 150)),
    ("宁夏回族自治区", random.randint(0, 150)),
    ("西藏自治区", random.randint(0, 150)),
    ("新疆维吾尔自治区", random.randint(0, 150)),
    ("内蒙古自治区", random.randint(0, 150)),
    ("河北省", random.randint(0, 150)),
    ("山西省", random.randint(0, 150)),
    ("辽宁省", random.randint(0, 150)),
    ("吉林省", random.randint(0, 150)),
    ("黑龙江省", random.randint(0, 150)),
    ("江苏省", random.randint(0, 150)),
    ("浙江省", random.randint(0, 150)),
    ("北京市", random.randint(0, 150)),
    ("天津市", random.randint(0, 150)),
    ("上海市", random.randint(0, 150)),
    ("台湾省", random.randint(0, 150)),
    ("香港特别行政区", random.randint(0, 150)),
    ("南海诸岛", random.randint(0, 150))
]
map.add("全国地图", data, "china")

map.set_global_opts(
    title_opts={"title": "全国地图"},
    visualmap_opts=VisualMapOpts(
        is_show=True,
        max_=100,
        min_=0,
        is_piecewise=False,
        pieces=[
            {"min": 101, "label": ">101", "color": "#FF0000FF"},
            {"min": 51, "max": 100, "label": "51-100", "color": "#FFAE00FF"},
            {"min": 0, "max": 50, "label": "0-50", "color": "#00CFFFFF"},
        ]
    )
)

map.render("01_构建基础全国可视化地图.html")