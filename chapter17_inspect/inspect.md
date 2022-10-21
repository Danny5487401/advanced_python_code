# inspect 

获取函数签名对象。

函数签名包含了一个函数的信息，包括函数名、它的参数类型、它所在的类和名称空间及其他信息）。
## 作用 
1. 对是否是模块、框架、函数进行类型检查
2. 获取源码
3. 获取类或者函数的参数信息
4. 解析堆栈


## 使用

### 1. inspect.getmembers
```python
inspect.getmembers(object[, predicate])

```
返回值为object的所有成员，以（name,value）对组成的列表

第二个参数通常可以根据需要调用如下16个方法；

```python
inspect.ismodule(object)： 是否为模块
inspect.isclass(object)：是否为类
inspect.ismethod(object)：是否为方法（bound method written in python）
inspect.isfunction(object)：是否为函数(python function, including lambda expression)
inspect.isgeneratorfunction(object)：是否为python生成器函数
inspect.isgenerator(object):是否为生成器
inspect.istraceback(object)： 是否为traceback
inspect.isframe(object)：是否为frame
inspect.iscode(object)：是否为code
inspect.isbuiltin(object)：是否为built-in函数或built-in方法
inspect.isroutine(object)：是否为用户自定义或者built-in函数或方法
inspect.isabstract(object)：是否为抽象基类
inspect.ismethoddescriptor(object)：是否为方法标识符
inspect.isdatadescriptor(object)：是否为数字标识符，数字标识符有__get__ 和__set__属性； 通常也有__name__和__doc__属性
inspect.isgetsetdescriptor(object)：是否为getset descriptor
inspect.ismemberdescriptor(object)：是否为member descriptor

```