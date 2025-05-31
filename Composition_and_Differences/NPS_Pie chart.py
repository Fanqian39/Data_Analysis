from pyecharts.charts import Pie
from pyecharts import options as opts

user_data = [("批评者", 879), ("被动者", 440), ("推荐者", 1248)]

total_samples = sum([count for _, count in user_data])
detractors_count = next(count for label, count in user_data if label == "批评者")
promoters_count = next(count for label, count in user_data if label == "推荐者")
nps = ((promoters_count / total_samples) * 100) - ((detractors_count / total_samples) * 100)

pie = Pie()
pie.add(
    series_name="",
    data_pair=user_data,
    label_opts=opts.LabelOpts(formatter="{d}%", position="inside"),
    radius="40%"
)

pie.set_global_opts(
    title_opts=opts.TitleOpts(title="购买核桃用户NPS占比", subtitle=f"NPS: {nps:.2f}%", pos_left="center"),
    toolbox_opts=opts.ToolboxOpts(is_show=True),
    legend_opts=opts.LegendOpts(pos_left="70%", pos_top="middle", orient="vertical")
)

pie.render("./NPS_pie.html")