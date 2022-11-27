# PEP380

# RESULT = yield from EXPR
# 可以简化成如下
"""
说明：
_i: 子生成器，同是也是一个迭代器
_y: 子生成器生产的值
_r: yield from 表达式最终的值
_s: 调用方通过send()发送的值
_e: 异常对象
"""

"""
_i = iter(EXPR) # EXPR是一个可迭代的对象，_i其实是子生成器
try:
    _y = next(_i) # 预激子生成器，把产生出来的第一个值放在_y中

except StopIteration as _e: # 调用ctrl+c
    _r = _e.value   # 如果抛出了StopIteration异常，那么就将异常对象的value传给_r
else:
    while 1:  # 尝试执行这个循环，委托生成器会阻塞：
        try:
            _s = yield _y  # 生产子生成器的值，等待调用方"send()值“,发送过来的值将保存到_s中
        except GeneratorExit as _e:
            try:
                _m = _i.close
            except AttributeError: # 可能没有这属性
                pass
            else:
                _m()
            raise _e
        except BaseException as _e:
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError: # 可能没有这属性
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s) # 转发_S，并且尝试以下操作
            except StopIteration as _e: # 如果子生成器抛出异常，那么将获取异常对象的值给_r
                _r = _e.value
                break
RESULT = _r #_r 是整个yield from 表达式的值
"""

"""
# 需要处理的问题
1.子生成器可能只是一个迭代器，并不是一个作为协程的生成器，所以他不支持.throw和.close方法
2. 如果子生成器支持.throw和.close方法,但是在子生成器的内部，这两个方法都会抛出异常
3. 调用方让子生成器自己抛出异常
4. 当调用方使用next()和.send(None)时，都要在子生成器上调用next()函数。当调用方发送非None值，才调用子生成器的.send方法

"""

"""
结论：
1.子生成器生产的值，都是直接传给调用方的，调用方通过.send()发送的值都是直接传递给子生成器的；如果发送的是None,会调用子生成器的__next__()
方法，如果不是None,会调用子生成器的.send()方法
2.子生成器退出的时候，最后的return EXPR ，会触发一个StopIteration(EXPR)异常
3.yield from 表达式的值，是子生成器终止时，传递给StopIteration异常的第一个参数。
4.如果调用的时候出现StopIteration异常，委托生成器会恢复运行，同时其他的异常会向上“冒泡"
5.传入委托生成器的异常里，除了GeneratorExit之外，其他的所有异常全部传递给子生成器.throw()方法。如果调用.throw()的时候出现了StopIteration异常，
那么就会恢复委托生成器的运行，其他的异常全部都会向上“冒泡”
6.如果在委托生成器上调用.close()，或者传入GeneratorExit异常，会调用子生成器.close方法，如果没有的话就不调用、如果在调用.close()的时候，
出现了异常，那么会向上“冒泡”，否则的话委托生成器抛出GeneratorExit异常。
"""
