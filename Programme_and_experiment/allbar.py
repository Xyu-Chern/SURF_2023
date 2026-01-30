import matplotlib.pyplot as plt
import numpy as np

# 数据集精度
dataset1_accuracy = [0.2658, 0.31505, 0.32855, 0.31915, 0.3382]
dataset2_accuracy = [0.2111, 0.10555, 0.31665, 0.10555, 0.2111]

# 柱状图参数设置
bar_width = 0.4
index = np.arange(5)  # 柱状图的索引位置

# 绘制柱状图
plt.bar(index, dataset1_accuracy, bar_width, label='Compressible')
plt.bar(index + bar_width, dataset2_accuracy, bar_width, label='Incompressible')

# 在每个柱子上标记具体的精度值
for i, v in enumerate(dataset1_accuracy):
    plt.text(i, v+0.02, "{:.2f}".format(v), ha='center', va='bottom')
for i, v in enumerate(dataset2_accuracy):
    plt.text(i + bar_width, v+0.02, "{:.2f}".format(v), ha='center', va='bottom')

# 第1个数据集的y坐标和上下误差范围
y1 = [0.2658, 0.3142, 0.3285, 0.3192, 0.3382]
y1_err = [0.0087, 0.0094, 0.0047, 0.0240, 0.0049]

# 第2个数据集的y坐标和上下误差范围
y2 = [0.2111, 0.1056, 0.3167, 0.1056, 0.2111]
y2_err = [0.0111, 0.0056, 0.0166, 0.0056, 0.0111]

# 绘制误差线图表，并指定颜色
plt.errorbar(index, y1, yerr=y1_err, fmt='o', capsize=5, color='b')
plt.errorbar(index + bar_width, y2, yerr=y2_err, fmt='o', capsize=5, color='r')

# 设置图表标题和标签
plt.title('Passing rate by Dataset and Method')
plt.xlabel('Method')
plt.ylabel('Passing rate')
plt.xticks(index + bar_width / 2, ['Baseline', 'Auto-D', 'Gold-D', 'Auto-D\n + CoT', 'Gold-D\n + CoT'])

# 调整图表布局，将下方空白区域调大
plt.subplots_adjust(bottom=0.2)

# 调整图例位置
plt.legend(loc='upper right')

# 设置y轴的取值范围
plt.ylim(0, 0.6)  # 设置y轴的最大值为0.5

# 保存图表为PNG格式
plt.savefig('bar_chart_err.png', dpi=300, bbox_inches='tight')

plt.show()
