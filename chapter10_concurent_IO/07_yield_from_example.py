# 需求：返回字典中，将销量求和。
"""
    data_sets = {
        "danny牌面膜": [1000,2000,3000],
        "danny牌手机": [10,20,30],
        "danny牌电脑": [100,200,300]
    }
    变成
    final result: {
    'danny牌面膜': (6000, [1000, 2000, 3000]),
     'danny牌手机': (60, [10, 20, 30]),
     'danny牌电脑': (600, [100, 200, 300])
     }
# 重点概念：main 为调用方  middle为委托生成器  sales_num 为子生成器
# yield from 会在调用方main 与子生成器之间建立一个双向通道
"""

final_result = {}


# 子生成器
def sales_num(pro_name):
    total = 0
    nums = []
    while True:
        # 外部传进来值
        x = yield
        print(pro_name + "销量：", x)
        # 传进来如果是None
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


# 委托生成器
def middle(key):
    while True:
        # 接受生成器返回的值
        final_result[key] = yield from sales_num(key)
        print(key + "销售统计完成！！")


# 调用方
def main():
    data_sets = {
        "danny牌面膜": [1000, 2000, 3000],
        "danny牌手机": [10, 20, 30],
        "danny牌电脑": [100, 200, 300],
    }
    for key, data_set in data_sets.items():
        print("start key: ", key)
        m = middle(key)
        # 预先启动middle协程
        m.send(None)
        for value in data_set:
            # 给协程传递每一组的值
            m.send(value)
        # 结束生成器
        m.send(None)
    print("final result:", final_result)


if __name__ == "__main__":
    # 方法一：yield from 推荐
    # main()

    # 方法二：无yield from
    # 没有中间生成器需要处理异常，并且需要把e.value返回
    # 子生成器调用
    my_gen = sales_num("danny大衣")
    my_gen.send(None)
    my_gen.send(100)
    my_gen.send(1000)
    my_gen.send(10000)
    try:
        my_gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)
