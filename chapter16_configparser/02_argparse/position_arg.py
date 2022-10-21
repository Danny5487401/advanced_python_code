import argparse

parser = argparse.ArgumentParser()

parser.add_argument("a")  # 获取的是字符串
parser.add_argument("b", type=int, help="display an integer")  # 获取的是数字

args = parser.parse_args("100 200".split())
print(args)
print(args.a)  # 可以进行变量的引用
print(args.b)
parser.print_usage()
parser.print_help()
