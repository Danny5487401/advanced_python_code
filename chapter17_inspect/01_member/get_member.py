######################### do_inspect.py ##########################
import inspect
import example_inspect

for name, data in inspect.getmembers(example_inspect):
    if name.startswith("__"):
        # 因为模块有一些私有属性作为导入实现的一部分，还会包含一组__builtins__。这两个东西的列表非常长
        continue
    print("{} : {!r}".format(name, data))

print("-------")
for name, data in inspect.getmembers(example_inspect, inspect.isclass):  # 修改了这里
    if name.startswith("__"):
        continue
    print("{} : {!r}".format(name, data))
