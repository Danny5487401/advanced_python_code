######################### do_inspect.py ##########################
import inspect
import example_inspect

if __name__ == "__main__":

    for name, data in inspect.getmembers(example_inspect):
        if name.startswith("__"):
            # 因为模块有一些私有属性作为导入实现的一部分，还会包含一组__builtins__。这两个东西的列表非常长
            continue
        print("{} : {!r}".format(name, data))

    print("---获取该模块的所有类----")
    for name, data in inspect.getmembers(
        example_inspect, inspect.isclass
    ):  # 第二个参数判断是否为类
        if name.startswith("__"):
            continue
        print("{} : {!r}".format(name, data))
