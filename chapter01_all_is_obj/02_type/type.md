# 通过type类创建类

当type()只有一个参数时，它的功能就是返回创建该参数的类；当多于一个参数时，type()才是type类的实例化，实例化得到 一个类并返回该类。


type创建类时，参数格式如下，classname是类名，字符串类型，parentclasses是类所有父类，元组类型，attrs是类的所有{属性:值}， 字典类型。
如果用户是用class关键字定义的类，那解释器会自动转为下面的格式执行。
```python
type(classname, parentclasses , attrs)
```

1. 案例一:定义一个类,没有属性
```python
class MyShinyClass(object):
    pass
```
当解释器执行时，会转为下面的语句，当然，你也可以直接这么写。
```python
MyShinyClass = type('MyShinyClass', (object,), {})
```

2. 案例二：定义一个类，并在类中定义属性
```python
class Foo(object):
    bar = True
```
被翻译成下面的形式
```python
Foo = type('Foo', (), {'bar':True})
```

3. 案例三：定义一个类，另一个类继承它
```python
class Foo(object):
    
class FooChild(Foo):
    pass
```
被翻译成下面的形式
```python
FooChild = type('FooChild', (Foo,), {})
```

4. 案例四：给你的类增加方法。定义一个函数，并将它分配给类的属性
```python
def echo_bar(self):
    print(self.bar)

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
```

