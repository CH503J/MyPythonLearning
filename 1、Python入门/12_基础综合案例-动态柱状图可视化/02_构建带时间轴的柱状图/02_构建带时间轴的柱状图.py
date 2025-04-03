import random

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150)
], label_opts=LabelOpts(position="right"))
bar.reversal_axis()

bar1 = Bar()
bar1.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar1.add_yaxis("商家A", [
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150)
], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar2.add_yaxis("商家A", [
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150)
], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar3.add_yaxis("商家A", [
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150)
], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

bar4 = Bar()
bar4.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar4.add_yaxis("商家A", [
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150)
], label_opts=LabelOpts(position="right"))
bar4.reversal_axis()

bar5 = Bar()
bar5.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar5.add_yaxis("商家A", [
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150)
], label_opts=LabelOpts(position="right"))
bar5.reversal_axis()

bar6 = Bar()
bar6.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar6.add_yaxis("商家A", [
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150)
], label_opts=LabelOpts(position="right"))
bar6.reversal_axis()

bar7 = Bar()
bar7.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar7.add_yaxis("商家A", [
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150)
], label_opts=LabelOpts(position="right"))
bar7.reversal_axis()

bar8 = Bar()
bar8.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar8.add_yaxis("商家A", [
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150)
], label_opts=LabelOpts(position="right"))
bar8.reversal_axis()

bar9 = Bar()
bar9.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar9.add_yaxis("商家A", [
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150),
    random.randint(50, 150)
], label_opts=LabelOpts(position="right"))
bar9.reversal_axis()



time_line = Timeline(
    {"theme": ThemeType.ROMANTIC}
)
time_line.add(bar, "2020-01-01")
time_line.add(bar1, "2020-01-02")
time_line.add(bar2, "2020-01-03")
time_line.add(bar3, "2020-01-04")
time_line.add(bar4, "2020-01-05")
time_line.add(bar5, "2020-01-06")
time_line.add(bar6, "2020-01-07")
time_line.add(bar7, "2020-01-08")
time_line.add(bar8, "2020-01-09")
time_line.add(bar9, "2020-01-10")

time_line.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

time_line.render("02_构建带时间轴的柱状图.html")
