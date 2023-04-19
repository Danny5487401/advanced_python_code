class Student:
    pass


class My_student(Student):
    pass


def foo():
    pass


if __name__ == "__main__":
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
    print(
        "使用__class__查看int元类，__class__返回的是一个类对象，再一次__class__返回创建类对象的类：", int.__class__
    )  # <class 'type'>

    # 2. 打印class的基类
    # 结论 type=>class 类对象 =>obj  实例
    stu = Student()
    print(type(stu))  # <class '__main__.Student'>
    print(type(Student))  # <class 'type'>
    print(Student.__bases__)  # (<class 'object'>,)
    print(My_student.__bases__)  # (<class '__main__.Student'>,)
    print(type.__bases__)  # (<class 'object'>,)
    print(object.__bases__)  # ()
    print(type(object))  # <class 'type'>

    # 3 打印函数foo的基类
    print(type(foo))  # <class 'function'>

# 结论  object 是所有类的基类
# type是一个类，同时type也是一个基类
