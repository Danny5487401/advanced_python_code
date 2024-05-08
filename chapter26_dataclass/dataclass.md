<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [dataclass](#dataclass)
  - [基本使用](#%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8)
  - [参考](#%E5%8F%82%E8%80%83)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# dataclass 

数据类是Python3.7 开始引入的一个新功能, 数据类提供了开箱即用的方法来创建自定义数据, 可以直接实例化、打印和比较数据类实例.

## 基本使用

```python
def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
              unsafe_hash=False, frozen=False):
```

- Frozen 实例是在初始化对象后无法修改其属性的对象
- init：默认将生成__init__方法；
- repr：默认将生成__repr__方法；repr字符串包含类名、每个字段名称和其repr（按其类中定义顺序）；
- frozen：若为true，实例初始化后属性将无法修改；
- order：默认不生成__gt__、__ge__、__lt__、__le__方法；

```python
def field(*, default=MISSING, default_factory=MISSING, init=True, repr=True,
          hash=None, compare=True, metadata=None):
```
- default：如果提供，这将是该字段的默认值。
- default_factory：用于指定具有可变默认值的字段，必须是一个无参可调用对象；与default互斥（不可同时指定）


## 参考

- 官方文档 https://docs.python.org/zh-cn/3.7/library/dataclasses.html

