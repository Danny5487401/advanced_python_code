# 主要通过eval(expression, globals=None, locals=None)
"""
expression：这个参数是一个字符串，python会使用globals字典和locals字典作为全局和局部的命名空间，将expression当做一个python表达式（从技术上讲，是一个条件列表）进行解析和计算。

globals:这个参数管控的是一个全局的命名空间，也就是我们在计算表达式的时候可以使用全局的命名空间中的函数，如果这个参数被提供了，并且没有提供自定义的__builtins__，那么会将当前环境中的__builtins__拷贝到自己提供的globals里，然后才会进行计算。关于__builtins__，它是python的内建模块，也就是python自带的模块，不需要我们import就可以使用的，例如我们平时使用的int、str、abs等都在这个模块中。关于它的说明可以参照这篇文章：点击打开链接。如果globals没有被提供，则使用python的全局命名空间。

locals：这个参数管控的是一个局部的命名空间，和globals类似，不过当它和globals中有重复的部分时，locals里的定义会覆盖掉globals中的，也就是当globals和locals中有冲突的部分时，locals说了算，它有决定权，以它的为准。如果locals没有被 提供的话，则默认为globals。

eval函数也可以被用来执行任意的代码对象（如那些由compile()创建的对象）。在这种情况下，expression参数是一个代码对象而不是一个字符串。如果代码对象已经被‘exec‘编译为模式参数，eavl（）的返回值是None

"""


# 动态调用函数
def function2(name, age):
    print("name: %s, age: %s" % (name, age))


# 动态调用方法
class Test(object):
    states = ["大于等于零", "大于等于二"]
    state2function = {"大于等于零": "check_gt0", "大于等于二": "check_gt2"}

    @staticmethod
    def check_gt0(x):
        return x >= 0

    @staticmethod
    def check_gt2(x):
        return x >= 2

    def predict(self, x):
        for state in Test.states:
            check_ans = eval("Test." + Test.state2function[state])(x)  # 调用Test类中的方法
            print(state, Test.state2function[state], x, check_ans)


if __name__ == '__main__':
    # 动态调用函数
    # 方式一
    eval("function2")("Alice", 11)

    # 或者：
    args = ["Alice", 11]
    kwargs = {}
    eval("function2")(*args, **kwargs)

    test = Test()
    test.predict(x=-1)
    test.predict(x=1)
    test.predict(x=2)
