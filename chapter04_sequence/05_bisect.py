import bisect

# 处理已排序的序列，升序
# bisect 二分查找

inte_list = []
bisect.insort(inte_list,3)
bisect.insort(inte_list,2)
bisect.insort(inte_list,1)
bisect.insort(inte_list,5)
bisect.insort(inte_list,6)
bisect.insort(inte_list,7)
bisect.insort(inte_list,0)

# 插入的位置
print(bisect.bisect(inte_list,3))

print(inte_list)
