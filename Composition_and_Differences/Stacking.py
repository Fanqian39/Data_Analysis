from pyecharts.charts import Bar
from pyecharts import options as opts

months = ["7月", "8月", "9月", "10月", "11月", "12月"]
choc_sales=[5340,6078,6460,6475,7431,8038]
gum_sales=[4340,4379,4460,5075,5431,6038]
walnut_sales=[6340,5579,4460,4075,3431,3038]

bar = Bar()

bar.add_xaxis(xaxis_data=months)
label_options=opts.LabelOpts(position='inside')

bar.add_yaxis(
    series_name="巧克力",
    y_axis=choc_sales,
    stack="sales",
    label_opts=label_options,
    color="red"
    )

bar.add_yaxis(
    series_name="口香糖",
    y_axis=gum_sales,
    stack="sales",
    label_opts=label_options
    )

bar.add_yaxis(
    series_name="核桃",
    y_axis=walnut_sales,
    stack="sales",
    label_opts=label_options
    )

bar.render("./bar_stack.html")