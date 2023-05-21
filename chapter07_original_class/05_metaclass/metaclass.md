# 元类

元类就是创建类的类，当通过type.__new__(cls, classname, bases, attrs)创建类时，cls就是该类的元类

## 作用
> Python大师Tim Peters说过：元类主要的使用场景是创建API，一个典型的例子是Django ORM。
 

元类可以做到：

- 拦截类的生成
- 修改类
- 返回修改后的类


## __metaclass__ 属性


1、在类中查找__metaclass__属性，如果找到就用，如果没有，进入2

2、在继承树中查找__metaclass__属性，如果还是没有，进入3

3、使用type类


## 参考资料

1 [元类](https://www.cnblogs.com/ajianbeyourself/p/4052084.html)

