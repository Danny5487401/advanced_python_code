# set 集合 frozenser不可变集合,无序不重复  性能高，用哈希
# 方法一
s = set("aberr")
# print(type(s))
# 方法二
s1 = {"r","g"}
# 添加数据一
s1.add("k")
# 添加数据二
anothser_et = set("opq")
s1.update(anothser_et)
# print(type(s1)) #<class 'set'>
print(s1)
# 不可以添加值，可以作为dict的key  强调：重点
s2 = frozenset("iouere")

# print(type(s2))
# difference 去掉重复的q
diff_set = set("q")
re_set = s1.difference(diff_set)
# 相当于
re_set2 = s1 - diff_set
print(re_set2)

# | & - 集合运算  魔法函数

# __contains__魔法函数
if "q" in diff_set:
    print(True)
# isubset 是不是另外一个集合的一部分
# print(diff_set.issubset(s1))