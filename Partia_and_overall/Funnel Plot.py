import openpyxl
from pyecharts.charts import Timeline, Funnel
from pyecharts import options as opts

path = "./Position pass.xlsx"
wb = openpyxl.load_workbook(path)
positionSheet = wb["岗位序列"]

def read_excel(row):
    label = positionSheet[1]
    num = positionSheet[row]
    total = []
    for i in range(1, 7):
        title = label[i].value
        number = num[i].value
        temp = []
        if i == 1:
            temp.append(title + "100%")
        else:
            pass_rate = (number / num[i - 1].value) * 100
            percent = round(pass_rate, 1)
            temp.append(title + f"{percent}%")
        temp.append(number)
        total.append(temp)

    return (num[0].value, total)

tl = Timeline()

for i in range(2, 8):
    data = read_excel(i)
    # 获取 HR 初筛时的人数作为最大值
    max_value = data[1][0][1]
    funnel = Funnel()
    funnel.add(
        series_name="",
        data_pair=data[1],
        gap=10,
        label_opts=opts.LabelOpts(position="inside"),
        # 修改 tooltip 的 formatter 配置
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}人"),
        itemstyle_opts=opts.ItemStyleOpts(),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
            ]
        ),
        max_=max_value
    )
    funnel.set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(title="各岗位招聘转化率")
    )
    tl.add(chart=funnel, time_point=f"{data[0]}岗位")

tl.render("./Funnel_position.html")