import openpyxl
from pyecharts.charts import Sankey
from pyecharts import options as opts
from pyecharts.charts import Page

wb = openpyxl.load_workbook("./sankey.xlsx")
sheet_A = wb["对照组"]
sheet_B = wb["实验组"]

def gen_nodesandlinks(sheet):
    list_labels = []
    links = []
    for row in sheet[2:24]:
        list_labels.append(row[0].value)
        list_labels.append(row[1].value)
        dic = {}
        dic["source"] = row[0].value
        dic["target"] = row[1].value
        dic["value"] = row[2].value
        links.append(dic)

    list_nodes = list(set(list_labels))
    nodes = []
    for i in list_nodes:
        dic = {}
        dic["name"] = i
        nodes.append(dic)

    return (nodes,links)

def plot_Sankey(sheet,title_name):
    sankey = Sankey(init_opts=opts.InitOpts(theme="dark",bg_color="#253441",width="1200px",height="600px"))
    nodes_links = gen_nodesandlinks(sheet)
    sankey.add("sankey",
            nodes=nodes_links[0],
            links=nodes_links[1],
            linestyle_opt=opts.LineStyleOpts(opacity=0.3, curve=0.5, color="source"),
            label_opts=opts.LabelOpts(position="right",color="#ffffff",font_size=10),
            node_gap=20
            )
    sankey.set_global_opts(title_opts=opts.TitleOpts(title=title_name),legend_opts=opts.LegendOpts(is_show=False))
    return sankey

page = Page()
page.add(plot_Sankey(sheet_A,"用户路径流转图对照组"),plot_Sankey(sheet_B,"用户路径流转图实验组"))
page.render("./sankey.html")