# 5大类
ParameterKind = [
    {"POSITIONAL_OR_KEYWORD": "可以通过定位参数和关键字参数传入的形参, python函数的参数多数属于此类"},  # 普通参数
    {"VAR_POSITIONAL": "定位参数元组"},  # *args
    {"VAR_KEYWORD": "关键字参数字典"},  # **kwargs
    {"KEYWORD_ONLY": "仅限关键字参数"},  # 类似于 下边d=100 的这种
    {"POSITIONAL_ONLY": "仅限定位参数, python声名的函数不支持, 但是有些c语言实现且不接受关键字参数的函数, 例如: divmod 支持"},
]

# 前四类
from inspect import signature


def func(a, b, c=10, *args, d=100, **kwargs):
    print(a, b, c, args, d, kwargs)


sig_func = signature(func)

for _, para_ in sig_func.parameters.items():
    print(para_.name, para_.kind, para_.default)

"""
   参数        参数类型                   参数默认值
    a       POSITIONAL_OR_KEYWORD     <class 'inspect._empty'>
    b       POSITIONAL_OR_KEYWORD     <class 'inspect._empty'>
    c       POSITIONAL_OR_KEYWORD     10
    args    VAR_POSITIONAL            <class 'inspect._empty'>
    d       KEYWORD_ONLY              100
    kwargs  VAR_KEYWORD               <class 'inspect._empty'>
"""

# 特殊的POSITIONAL_ONLY

sig_divmod = signature(divmod)

for _, _para in sig_divmod.parameters.items():  #
    print(_para.name, _para.kind, _para.default)
"""
    x     POSITIONAL_ONLY     <class 'inspect._empty'>
    y     POSITIONAL_ONLY     <class 'inspect._empty'>
"""
