import json

with open("dataset_Qzc.json", "r") as f:
    data=json.load(f)
# print(data["id2"])



# """Enter a string containing only three Floating-point arithmetic numbers, namely three sides of a triangle, to determine whether a triangle can be formed."""'
# “”“输入一个仅包含三个浮点算术数字的字符串，即三角形的三条边，以确定是否可以形成三角形。”“”


def is_triangle(sides):
    side_lengths = sides.split()  # 将输入字符串分割成一个列表
    if len(side_lengths) != 3:  # 确保列表中有且仅有三个元素
        return False
    
    try:
        a, b, c = map(float, side_lengths)  # 将字符串转换为浮点数
        if a <= 0 or b <= 0 or c <= 0:  # 确保边长均大于零
            return False
        if a + b > c and a + c > b and b + c > a:  # 根据三角形的边长关系判断是否可以形成三角形
            return True
    except ValueError:
        pass
    
    return False


def check(candidate):
    assert candidate("123") == False
    assert candidate("223") == True
    # assert candidate("345") == True
    # assert candidate("111") == True
    # assert candidate("011") == False

try:
    check(is_triangle)
    print("hhhh")
except:
    print("md")

print(is_triangle("2.1 2.2 3.2"))