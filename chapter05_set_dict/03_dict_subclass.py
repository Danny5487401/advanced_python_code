# 不建议继承c语言的list和dict

class Mydict(dict):
    def __setitem__(self, key, value):
        # C语言可能没有调用父类的方法
        super().__setitem__(key,value*2)

# 这样写没有调用
my_dict = Mydict(one=1)
print(my_dict)
# 纠正写法
my_dict["one"] = 1
print(my_dict)

# 方法二
from collections import UserDict
class Mydict2(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key,value*2)


my_dict2 = Mydict2(one=1)
print(my_dict2)
# 纠正写法
my_dict2["two"] = 1
print(my_dict2)

from collections import defaultdict
my_dict3 = defaultdict(dict)
# 调用__missing__方法
my_value = my_dict3["danny5"]
print(my_value)

# 顺序orderdict
from collections import OrderedDict
order_dict = OrderedDict()
order_dict["a"] = "haha"
order_dict["b"] = 2
order_dict["c"] = 3


for k,v in order_dict.items():
    print(k,v)
