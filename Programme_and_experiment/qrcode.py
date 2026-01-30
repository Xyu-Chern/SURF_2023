

# # 生成github code
# import pyqrcode

# # 定义要生成二维码的网页链接
# url = "https://github.com/nakupenda-c/Auto-Prompt-Decomposition-with-Chain-of-Thought-in-Large-Language-Models-for-Program-Synthesis"

# # 生成二维码对象
# qr_code = pyqrcode.create(url)

# # 保存二维码图片
# qr_code.png("qrcode.png", scale=8)



# 生成github code
import pyqrcode

# 定义要生成二维码的网页链接
url = "https://drive.google.com/file/d/1Xfx46xbFcn70kTChgyXKSFExR_DdENi8/view?usp=sharing"

# 生成二维码对象
qr_code = pyqrcode.create(url)

# 保存二维码图片
qr_code.png("report.png", scale=8)