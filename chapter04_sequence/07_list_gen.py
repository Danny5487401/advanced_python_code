# 列表生成式
# 提取1-20中的奇数
odd_list1 = []
for i in range(21):
    if i %2 ==1:
        odd_list1.append(i)


# 方法二
odd_list2 = [i for i in range(21) if i % 2 ==1]
# 逻辑复杂的情况,可以替代map,reduce
def handle_item(item):
    return item *item

# 列表生成式高于列表操作，强调可读性
odd_list3 = [handle_item(i) for i in range(21) if i % 2 ==1]

# print(odd_list3)

# 生成器表达式
odd_list_gen = (i for i in range(21) if i % 2 ==1)
# print(type(odd_list_gen))
# 生成器可以转换成list
odd_list_transter = list(odd_list_gen)
# print(odd_list_transter)

# 字典推导式
my_dict = {"name":"danny","company":"hover"}
# 调换key,value
reversed_dict = {value:key for key,value in my_dict.items()}
print(reversed_dict)

# 集合推导式
# 灵活性更高
my_set = {key for key,value in my_dict.items()}
print(type(my_set))
print(my_set)
my_set2 = set(my_dict.keys())
print(my_set2)
