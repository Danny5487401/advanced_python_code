import inspect
import pprint


def show_stack():
    for level in inspect.stack():
        print(
            "{}[{}]\n -> {}".format(
                level.frame.f_code.co_filename,
                level.lineno,
                level.code_context[level.index].strip(),
            )
        )
        pprint.pprint(level.frame.f_locals)
        print("\n")


def recurse(limit):
    local_variable = "." * limit
    if limit <= 0:
        show_stack()
        return
    recurse(limit - 1)
    return local_variable


if __name__ == "__main__":
    recurse(2)

# 输出
"""
/Users/python/Downloads/advanced_python_code/venv/bin/python /Users/python/Downloads/advanced_python_code/chapter17_inspect/03_stack/stack.py 
/Users/python/Downloads/advanced_python_code/chapter17_inspect/03_stack/stack.py[6]
 -> for level in inspect.stack():
{'level': FrameInfo(frame=<frame at 0x7fc4000d9780, file '/Users/python/Downloads/advanced_python_code/chapter17_inspect/03_stack/stack.py', line 14, code show_stack>, filename='/Users/python/Downloads/advanced_python_code/chapter17_inspect/03_stack/stack.py', lineno=6, function='show_stack', code_context=['    for level in inspect.stack():\n'], index=0)}


/Users/python/Downloads/advanced_python_code/chapter17_inspect/03_stack/stack.py[21]
 -> show_stack()
{'limit': 0, 'local_variable': ''}


/Users/python/Downloads/advanced_python_code/chapter17_inspect/03_stack/stack.py[23]
 -> recurse(limit - 1)
{'limit': 1, 'local_variable': '.'}


/Users/python/Downloads/advanced_python_code/chapter17_inspect/03_stack/stack.py[23]
 -> recurse(limit - 1)
{'limit': 2, 'local_variable': '..'}


/Users/python/Downloads/advanced_python_code/chapter17_inspect/03_stack/stack.py[28]
 -> recurse(2)
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': '/Users/python/Downloads/advanced_python_code/chapter17_inspect/03_stack/stack.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fc4200e80a0>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'inspect': <module 'inspect' from '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/inspect.py'>,
 'pprint': <module 'pprint' from '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/pprint.py'>,
 'recurse': <function recurse at 0x7fc40017a4c0>,
 'show_stack': <function show_stack at 0x7fc4000c21f0>}
"""
