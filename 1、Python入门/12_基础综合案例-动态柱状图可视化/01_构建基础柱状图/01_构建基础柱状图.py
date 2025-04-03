from pyecharts.charts import Bar
from pyecharts.options import *

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90], label_opts=LabelOpts(position="right"))
bar.add_yaxis("商家B", [15, 25, 16, 55, 48, 8], label_opts=LabelOpts(position="right"))

bar.reversal_axis()
bar.set_global_opts(title_opts={"title": "基础柱状图"})
bar.render("01_构建基础柱状图.html")
