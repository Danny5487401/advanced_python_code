import math
import argparse  # 1、导入argpase包


def parse_args():
    parse = argparse.ArgumentParser(description="Calculate cylinder volume")  # 2、创建参数对象
    parse.add_argument("--radius", default=2, type=int, help="Radius of Cylinder")
    # 3、往参数对象添加参数
    parse.add_argument("--height", default=4, type=int, help="height of Cylinder")
    args = parse.parse_args()  # 4、解析参数对象获得解析对象
    return args


def cal_vol(radius, height):
    vol = math.pi * pow(radius, 2) * height
    return vol


if __name__ == "__main__":
    args = parse_args()
    print(cal_vol(args.radius, args.height))  # 5、使用解析对象.参数获取使用命令行参数
