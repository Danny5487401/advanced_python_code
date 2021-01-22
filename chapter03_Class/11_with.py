def exec_with():
    try:
        print("A")
        raise KeyError
        return 1
    except KeyError as e:
        print("keyerror")
        return  2
    else:
        print("ok")
        return 3
    finally:
        print("finally")
        # return 4

# with 简化try finally
# 简化生成类，用contextlib，但必须是生成器
class Sample():
    # 上下文管理器协议
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print("do")


if __name__ == "__main__":
    result = exec_with()
    # 有finally 返回4， 无finally return 返回2
    print(result)

    with Sample() as sample:
        sample.do_something()
