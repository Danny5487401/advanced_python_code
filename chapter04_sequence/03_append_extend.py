a = list()
# + 只能相同类型
c = a + [3,4]
# += 符号  实际是 __iadd__,实际调用extend,extend又是append
from collections import abc
a += [5,6]
a += (7,8)
a.extend(range(3))
print(c)
print(a)
