a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # 重新生成对象
# 调用 __eq__函数
print(a == b)

# 强调: intern机制，小整数，小字符串是一样的
c = 1
d = 1
e = "ab"
f = "ab"
print(c is d)
print(e is f)


class People:
    pass


person = People()
if type(person) is People:
    print(True)
