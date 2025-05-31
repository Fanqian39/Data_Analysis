from pyecharts.charts import Bar, Line, Pie, Map, Page
from pyecharts import options as opts

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sale = [220, 370, 800, 400, 220, 150, 130, 260, 130, 130, 110, 190]
stock_apple = [40, 30, 50, 70, 40, 50, 60, 70, 50, 40, 50, 40]
stock_banana = [60, 70, 90, 80, 60, 80, 100, 80, 90, 60, 50, 40]
stock_walnut = [50, 40, 60, 70, 60, 70, 80, 65, 70, 60, 80, 50]
data = [("苹果", 40), ("香蕉", 20), ("核桃", 40)]
saleData = [('安徽省', 521), ('北京市', 918), ('福建省', 345), ('甘肃省', 545), ('广东省', 766), ('广西壮族自治区', 257), ('贵州省', 185), ('海南省', 86), ('河北省', 327), ('河南省', 336), ('黑龙江省', 172), ('湖北省', 522), ('湖南省', 508), ('吉林省', 497), ('江苏省', 492), ('江西省', 374), ('辽宁省', 358), ('内蒙古自治区', 100), ('宁夏回族自治区', 84), ('青海省', 97), ('山东省', 508), ('山西省', 266), ('陕西省', 334), ('上海市', 324), ('四川省', 758), ('天津市', 263), ('西藏自治区', 62), ('新疆维吾尔自治区', 81), ('云南省', 551), ('浙江省', 500), ('重庆市', 262)]

bar = Bar(init_opts=opts.InitOpts(theme="dark", width="300px", height="300px"))
bar.add_xaxis(xaxis_data=month)
bar.add_yaxis(series_name="销售额", y_axis=sale)
bar.set_global_opts(datazoom_opts=opts.DataZoomOpts(is_show=True, type_="slider"))

line = Line(init_opts=opts.InitOpts(theme="dark", width="300px", height="300px"))
line.add_xaxis(xaxis_data=month)
line.add_yaxis(series_name="苹果", y_axis=stock_apple)
line.add_yaxis(series_name="香蕉", y_axis=stock_banana)
line.add_yaxis(series_name="核桃", y_axis=stock_walnut)
line.set_global_opts(datazoom_opts=opts.DataZoomOpts(is_show=True, type_="slider"))

pie = Pie(init_opts=opts.InitOpts(theme="dark", width="300px", height="300px"))
pie.add(
    series_name="",
    data_pair=data,
    radius=["40%", "50%"]
)

mapChart = Map(init_opts=opts.InitOpts(theme="dark", width="300px", height="300px"))
mapChart.add(
    series_name="",
    data_pair=saleData,
    maptype="china"
)

mapChart.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=1000))

page = Page(layout=Page.DraggablePageLayout)
page.add(pie, bar, line, mapChart)
page.render("./combined_show.html")