import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt

df = pd.read_excel("./data.xlsx")

products = []
for i in df['商品类型']:
    product = i.split(',')
    products.append(product)

rules = apriori(products, min_support=0.1, min_confidence=0.6)

extract_result = []
for rule in rules:
    support = round(rule.support, 3)
    for i in rule.ordered_statistics:
        head_set = list(i.items_base)
        tail_set = list(i.items_add)
        if not head_set:
            continue
        related_category = f"[{','.join(head_set)}]→[{','.join(tail_set)}]"
        confidence = round(i.confidence, 3)
        lift = round(i.lift, 3)
        extract_result.append([related_category, support, confidence, lift])

rule_data = pd.DataFrame(extract_result, columns=['关联规则', '支持度', '置信度', '提升度'])
promoted_rules = rule_data[rule_data['提升度'] > 1]
restricted_rules = rule_data[rule_data['提升度'] < 1]

plt.rcParams.update({'font.size': 20})
plt.rcParams["font.sans-serif"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False
fig, axes = plt.subplots(1, 2, figsize=(18, 8))
plt.subplots_adjust(wspace=0.4)

def add_labels(ax):
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(
            f'{height:.3f}',
            xy=(p.get_x() + p.get_width()/2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center',
            va='bottom'
        )

if not promoted_rules.empty:
    ax1 = promoted_rules.plot.bar(
        x='关联规则',
        y=['支持度', '置信度'],
        ax=axes[0],
        rot=0,
        title="促进关系的强关联规则",
        color=['#5DA5DA', '#FAA43A'],
        width=0.4
    )
    # 将图例位置设置为右上角
    ax1.legend(loc='upper right')
    add_labels(ax1)
    plt.setp(ax1.get_xticklabels(), rotation=0, ha='center', rotation_mode='anchor')
else:
    axes[0].text(0.5, 0.5, '没有促进关系的规则', ha='center', va='center')
    axes[0].set_title("促进关系的强关联规则")

if not restricted_rules.empty:
    ax2 = restricted_rules.plot.bar(
        x='关联规则',
        y=['支持度', '置信度'],
        ax=axes[1],
        rot=0,
        title="抑制关系的强关联规则",
        color=['#60BD68', '#B2912F'],
        width=0.4
    )
    # 将图例位置设置为右上角
    ax2.legend(loc='upper right')
    add_labels(ax2)
    plt.setp(ax2.get_xticklabels(), rotation=0, ha='center', rotation_mode='anchor')
else:
    axes[1].text(0.5, 0.5, '没有抑制关系的规则', ha='center', va='center')
    axes[1].set_title("抑制关系的强关联规则")

plt.tight_layout()
plt.show()

print(rule_data)