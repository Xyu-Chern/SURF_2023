

import matplotlib.pyplot as plt

# 数据点的x坐标（轮次）
x = ['Baseline', 'Auto-D', ' Gold-D', 'Auto-D\n + COT', 'Gold-D\n + COT']

# 第1个数据集的y坐标和上下误差范围
y1 = [0.2658, 0.3142, 0.3285, 0.3192, 0.3382]
y1_err = [0.0087, 0.0094, 0.0047, 0.0240, 0.0049]

# 第2个数据集的y坐标和上下误差范围
y2 = [0.2111, 0.1056, 0.3167, 0.1056, 0.2111]
y2_err = [0.0111, 0.0056, 0.0166, 0.0056, 0.0111]

# 绘制误差线图表
plt.errorbar(x, y1, yerr=y1_err, fmt='o', capsize=5, label='Compressible')
plt.errorbar(x, y2, yerr=y2_err, fmt='o', capsize=5, label='Incompressible')

# 设置图例、标题和坐标轴标签
plt.legend()
plt.title('Errorbar Plot')
plt.xlabel('Methods')
plt.ylabel('Passing rate')

# 调整图表布局，将下方空白区域调大
plt.subplots_adjust(bottom=0.2)

# 显示图表并保存为图片
plt.savefig('errorbar_plot.png')
plt.show()

