import importlib


def dynamic_import(module):
    return importlib.import_module(module)


if __name__ == "__main__":
    # 确保该代码在刚才创建的两个文件foo.py, bar.py 在相同目录下
    module = dynamic_import("foo")
    module.main()

    module2 = dynamic_import("bar")
    module2.main()
