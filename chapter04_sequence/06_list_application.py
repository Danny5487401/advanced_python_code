# array , deque,
# 数组
# a = list   #直接点是pycharm生成接口
import array

my_array = array.array("i")  #看官网看类型
# 布隆过滤器(Bloom Filter)详解就用到array
my_array.append(1)
my_array.append(10)
print(my_array)