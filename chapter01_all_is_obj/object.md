# 一切都是对象
在Python中，一切都是对象，对象对用户来说只提供了变量，变量就是那些标识符，变量以引用的方式操作对象，变量相当于对象暴露给用户的接口。

## 对象三个特征: 身份，类型，值
1. 身份：ID地址

2. 类型：对应静态类型-->数值类型，迭代类型，序列类型，映射（dict)，集合，上下文管理器，None(全局只有一个）


- 数值：int,float,complex复数，bool
- 迭代类型: 迭代器，生成器
- 序列类型：list,bytes,bytearray,memoryview(二级制序列),range,tuple,str,array
- 映射：dict
- 集合：set, frozenset
- 上下文管理类型 with
- 其他，深入python源码： 模块类型，class和实例，函数类型，方法类型，代码类型，object对象，type类型，ellipsis类型，notimplemented类型

3. 值

## 元类

![](./type_class_obj.png)

通过type类创建对象是动态，其实我们平时使用class关键字定义类也是动态的，当Python解释器遇到class关键字的， 它就会执行，并创建类对象。

其实，类对象也是实例化的结果，即类对象是由另一个类实例化得到的，我们称创建类的类为元类，
反之也成立，如果类X实例化后得到是类对象，那X就是元类。在Python中，只有type类及其子类才可以当元类。

在Python中， 这个追溯终止在type类。元类是type类或其子类，而type类的元类就是它自己。

```python
# __class__返回的是一个类对象，再一次__class__返回创建类对象的类
```

### __metaclass__属性

__metaclass__属性，用它指定创建该类的元类。
__metaclass__只要是一个可调用对象就行，该可调用对象的参数格式为callable(classname, parentclasses , attrs)，与用type类创建类对象时，参数格式完全相同。






