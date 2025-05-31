import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 将全局字体大小设置为原来的两倍
original_font_size = plt.rcParams['font.size']
plt.rcParams['font.size'] = original_font_size * 2

# 读取数据
df = pd.read_excel("./data.xlsx")
df["LastPurchaseDate"] = pd.to_datetime(df["LastPurchaseDate"])

# 计算R值（最近消费间隔天数）
end_time = datetime(2026, 12, 31)
df["time_gap"] = (end_time - df["LastPurchaseDate"]).dt.days
R = df["time_gap"]

# 提取F值（消费频率）和M值（消费金额）
F = df["order_count"]
M = df["total_amount"]

# 定义描述性分析函数
def describe_rfm(data_series, metric_name):
    desc = data_series.describe()
    print(f"\n{metric_name} 描述性统计结果：")
    print(f"最小值: {desc['min']:.2f}")
    print(f"最大值: {desc['max']:.2f}")
    print(f"平均值: {desc['mean']:.2f}")
    print(f"中位数: {desc['50%']:.2f}")
    print(f"标准差: {desc['std']:.2f}")
    return data_series

# 执行描述性分析
R_series = describe_rfm(R, "最近消费间隔（R）")
F_series = describe_rfm(F, "消费频率（F）")
M_series = describe_rfm(M, "消费金额（M）")

# 绘制直方图（三张图在同一画布）
plt.figure(figsize=(18, 6))  # 设置画布大小

# 绘制R值直方图
plt.subplot(1, 3, 1)
plt.hist(R_series, bins=20, color='skyblue', edgecolor='black')
plt.title("最近消费间隔（R）分布")
plt.xlabel("间隔天数")
plt.ylabel("用户数量")

# 绘制F值直方图
plt.subplot(1, 3, 2)
plt.hist(F_series, bins=10, color='lightgreen', edgecolor='black')
plt.title("消费频率（F）分布")
plt.xlabel("订单次数")
plt.ylabel("用户数量")

# 绘制M值直方图
plt.subplot(1, 3, 3)
plt.hist(M_series, bins=20, color='lightcoral', edgecolor='black')
plt.title("消费金额（M）分布")
plt.xlabel("消费金额（元）")
plt.ylabel("用户数量")

# 调整子图间距
plt.tight_layout()
plt.show()