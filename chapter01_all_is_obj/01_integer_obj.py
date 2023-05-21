if __name__ == "__main__":
    # 1 查看integer对象
    two = 2
    print(type(two))
    print(type(type(two)))
    print(type(two).__bases__)
    print(dir(two))


"""
>>> two = 2   1
>>> type(two)
<type 'int'> 2
>>> type(type(two))
<type 'type'> 3
>>> type(two).__bases__
(<type 'object'>,) 4
>>> dir(two) 5
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', 
 '__delattr__', '__div__', '__divmod__', '__doc__', '__float__',
 '__floordiv__', '__format__', '__getattribute__', '__getnewargs__',
 '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__',
 '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__',
 '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__',
 '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__',
 '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__',
 '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
 '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
 '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
 'conjugate', 'denominator', 'imag', 'numerator', 'real']
 
 
 

"""
