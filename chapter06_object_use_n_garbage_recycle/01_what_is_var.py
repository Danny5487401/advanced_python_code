# python 和java 变量本质不一样，java和go 一样需要指明变量类型，Python变量实际是一个指针，大小固定
# a = "abc"
# 1.过程先生成对象，然后再指向对象
a = [1,2,3]
b = a
b.append(4)
print(a)
