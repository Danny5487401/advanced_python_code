# 1. 打印int和str的基类
# 结论 type=>int =>1
a = 1
b = "abc"
print(type(1))  # <class 'int'>
print(type(int))  # <class 'type'>
print(type(b))  # <class 'str'>
print(type(str))  # <class 'type'>
print(int.__bases__)  # (<class 'object'>,)
print(str.__bases__)  # (<class 'object'>,)



# 2. 打印clase的基类
# 结论 type=>class 类对象 =>obj  实例
class Student:
    pass


class Mystudent(Student):
    pass


stu = Student()
print(type(stu))  # <class '__main__.Student'>
print(type(Student))  # <class 'type'>
print(Student.__bases__)  # (<class 'object'>,)
print(Mystudent.__bases__)  # (<class '__main__.Student'>,)
print(type.__bases__)  # (<class 'object'>,)
print(object.__bases__)  # ()
print(type(object))  # <class 'type'>

#  结论  object 是所有类的基类
# type是一个类，同时type也是一个基类
