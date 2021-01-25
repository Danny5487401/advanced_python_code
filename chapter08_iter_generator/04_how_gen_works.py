# 1.python中的函数工作原理
import inspect
frame = None
def foo():
    bar()


def bar():
    global frame
    frame = inspect.currentframe()

"""
python.exe会用一个叫做PyEval_EvalFramEx(C函数）去执行foo函数，
首先会创建一个栈帧（stack frame)，实际是个上下文
python中一切皆对象，栈帧对象，字节码对象
当foo调用子函数bar,又会创建一个栈帧，将函数控制权交给这个对象
所有的栈帧都是分配在堆内存上，堆不释放都一直存在内存当中，这就决定了栈帧可以独立于调用者存在
"""
import dis
"""
  4           0 LOAD_GLOBAL              0 (bar)
              2 CALL_FUNCTION            0
              4 POP_TOP
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE
None
"""
# print(dis.dis(foo))

foo()
print(frame.f_code.co_name) # bar
caller_frame = frame.f_back
print(caller_frame.f_code.co_name) # foo


def gen_func():
    # 可以返回return
    yield 1
    name = "danny"
    yield 2
    age = 20
    return "college"
# sehn'c'g'h
gen = gen_func()
# f_lasti 指数，f_locals变量
# 这两个变量控制暂停和继续
print(dis.dis(gen))
print(gen.gi_frame.f_lasti) # -1
print(gen.gi_frame.f_locals) # {}
next(gen)
print(gen.gi_frame.f_lasti) # 2
print(gen.gi_frame.f_locals) # {}
next(gen)
print(gen.gi_frame.f_lasti) # 12
print(gen.gi_frame.f_locals) # {'name': 'danny'}
"""
 38           0 LOAD_CONST               1 (1)
              2 YIELD_VALUE
              4 POP_TOP

 39           6 LOAD_CONST               2 ('danny')
              8 STORE_FAST               0 (name)

 40          10 LOAD_CONST               3 (2)
             12 YIELD_VALUE
             14 POP_TOP

 41          16 LOAD_CONST               4 (20)
             18 STORE_FAST               1 (age)

 42          20 LOAD_CONST               5 ('college')
             22 RETURN_VALUE
None
"""
from collections import UserList


pass
