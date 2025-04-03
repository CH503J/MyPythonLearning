"""
1. pyEcharts简介
    - Echarts是个由百度开源的数据可视化，凭借着良好的交互性，精巧的图表设计，得到了众多开发者的认可. 而Python是门富有表达力的语言，很适合用于数据处理. 当数据分析遇上数据可视化时pyecharts 诞生了。
2. pyEcharts快速入门
"""
# 导包，导入line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts

# 得到折线图对象
line = Line()

# 添加x轴数据
line.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])

# 添加y轴数据
line.add_yaxis("基础折线图", [5, 20, 36, 10, 75, 90])

# 全局配置项
# 更多全局配置项可在官网查询  https://pyecharts.org/#/zh-cn/global_options
line.set_global_opts(
    title_opts=TitleOpts(title="基础折线图", pos_left="1%", pos_bottom="95%"),
    legend_opts=LegendOpts(is_show=False),
    toolbox_opts=ToolboxOpts(is_show=True, pos_left="1%", pos_bottom="5%"),
)

# 生成图标文件
line.render(r"C:\Develop\PythonProjects\MyPythonLearning\1、Python入门\10_基础综合案例-折线图可视化\pyEcharts快速入门\基础折线图实例.html")
