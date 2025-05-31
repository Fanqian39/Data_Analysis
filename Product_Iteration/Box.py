import openpyxl
from pyecharts.charts import Boxplot
from pyecharts import options as opts

path = "./Box_test_data.xlsx"
wb = openpyxl.load_workbook(path)
user_time = wb["使用时长"]

def read_time(row):
    rowData = user_time[row]
    timeList = []
    for cell in rowData[1:]:
        time = cell.value
        if time == None:
            continue
        timeList.append(time)
    return timeList

control_gp = []
exp_gp = []
for row in range(2,9):
    result = read_time(row)
    control_gp.append(result)

    exp_result = read_time(row+10)
    exp_gp.append(exp_result)

boxplot = Boxplot()
boxplot.add_xaxis(xaxis_data=["第一天", "第二天", "第三天", "第四天", "第五天", "第六天", "第七天"])
boxplot.add_yaxis(series_name="对照组", y_axis=boxplot.prepare_data(control_gp))
boxplot.add_yaxis(series_name="实验组", y_axis=boxplot.prepare_data(exp_gp))
boxplot.set_global_opts(title_opts=opts.TitleOpts(title='用户使用时长对比'))
boxplot.render("./box_test.html")