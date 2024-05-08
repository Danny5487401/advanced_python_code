class MyList(object):
    """自己实现一个list"""

    def __init__(self, values=None):
        # 初始化自定义list
        self.values = values or []
        self._index = 0

    def __setitem__(self, key, value):
        # 添加元素
        self.values[key] = value

    def __getitem__(self, key):
        # 获取元素
        return self.values[key]

    def __delitem__(self, key):
        # 删除元素
        del self.values[key]

    def __len__(self):
        # 自定义list的元素个数
        return len(self.values)

    def __iter__(self):
        # 可迭代
        return self

    def __next__(self):
        # 迭代的具体细节
        # 如果__iter__返回self 则必须实现此方法
        if self._index >= len(self.values):
            raise StopIteration()
        value = self.values[self._index]
        self._index += 1
        return value

    def __contains__(self, key):
        # 元素是否在自定义list中
        return key in self.values

    def __reversed__(self):
        # 反转
        return list(reversed(self.values))


if __name__ == "__main__":
    # 初始化自定义list
    my_list = MyList([1, 2, 3, 4, 5])

    print(my_list[0])  # __getitem__
    my_list[1] = 20  # __setitem__

    print(1 in my_list)  # __contains__
    print(len(my_list))  # __len__

    print([i for i in my_list])  # __iter__
    del my_list[0]  # __del__

    reversed_list = reversed(my_list)  # __reversed__
    print([i for i in reversed_list])  # __iter__
