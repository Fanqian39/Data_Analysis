# 导入pandas模块
import pandas as pd
'''获取描绘R、F、M的数据'''
# 1. 读取并处理数据集
df = pd.read_excel("./data.xlsx")
df["LastPurchaseDate"] = pd.to_datetime(df["LastPurchaseDate"])

# 2. 获取描绘R的数据
from datetime import datetime
endTime = datetime(2026, 12, 31)
df["time_gap"] = endTime - df["LastPurchaseDate"]
df["time_gap"] = df["time_gap"].dt.days

'''依次划分R、F、M'''
# 1. 划分R
df["R"] = pd.qcut(df["time_gap"], q=5, labels=[5, 4, 3, 2, 1])
# 2. 划分F
df["F"] = pd.qcut(df["order_count"], q=5, labels=[1, 2, 3, 4, 5])
# 3. 划分M
df["M"] = pd.qcut(df["total_amount"], q=5, labels=[1, 2, 3, 4, 5])

'''对用户标记分层结果'''
# 1. 简化分值
def rfmTrans(x):
    if x > 3:
        return 1
    else:
        return 0

df["R"] = df["R"].apply(rfmTrans)
df["F"] = df["F"].apply(rfmTrans)
df["M"] = df["M"].apply(rfmTrans)

# 2. 获取数值标签
df["mark"] = df["R"].astype(str) + df["F"].astype(str) + df["M"].astype(str)

# 3. 标记用户层级
def rfmType(x):
    if x == "111":
        return "高价值用户"
    elif x == "101":
        return "重点发展用户"
    elif x == "011":
        return "重点唤回用户"
    elif x == "001":
        return "重点潜力用户"
    elif x == "110":
        return "一般潜力用户"
    elif x == "100":
        return "一般发展用户"
    elif x == "010":
        return "一般维系用户"
    else:
        return "低价值用户"

df["customer_type"] = df["mark"].apply(rfmType)

# 手动指定用户分层类别的顺序
customer_types_order = [
    "高价值用户", "重点发展用户", "重点唤回用户",
    "重点潜力用户", "一般潜力用户", "一般发展用户",
    "一般维系用户", "低价值用户"
]

# 按照指定顺序统计数量和占比
df_type = df["customer_type"].value_counts().reindex(customer_types_order)
df_perc = df["customer_type"].value_counts(normalize=True).reindex(customer_types_order)

# 4. 可视化结果
import matplotlib.pyplot as plt

# 调整画布大小（宽度增加到10英寸，高度保持6英寸）
plt.figure(figsize=(10, 6))

# 设置中文字体为黑体
plt.rcParams["font.sans-serif"] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False

# 绘制柱状图
ax1 = plt.subplot(111)  # 创建主坐标轴
bars = ax1.bar(df_type.index, df_type.values, color="skyblue", width=0.5)  # 调整柱状图宽度
ax1.set_xlabel("用户分层类别", fontsize=12)  # 设置x轴标签字体大小
ax1.set_ylabel("各层级用户总数", fontsize=12)

# 绘制折线图（次坐标轴）
ax2 = ax1.twinx()
ax2.plot(df_perc.index, df_perc.values, marker="o", color="lightcoral", linestyle="-")
ax2.set_ylabel("各层级用户总数占比", fontsize=12)  # 设置右侧y轴标签字体大小

# 调整x轴标签旋转角度（45度倾斜）
plt.xticks(rotation=45, ha="right", fontsize=10)  # 旋转并右对齐，缩小字体

# 调整子图边距（防止标签被截断）
plt.subplots_adjust(bottom=0.2, right=0.9)  # 增加底部和右侧边距

plt.show()