a = list()
# + 只能相同类型
c = a + [3, 4]
c.append(5)
print(c)
# += 符号  实际是 __iadd__,实际调用extend,extend又是append

a += [5, 6]
a += (7, 8)
a.extend(range(3))


print(a)
