# 类型注解

在 Python 3.5 中，Python PEP 484 引入了类型注解（type hints），在 Python 3.6 中，PEP 526 又进一步引入了变量注解（Variable Annotations），

## 函数注释语法

函数注释作用是提高代码可读性，暗示传入参数及返回数据的类型。

函数注释两个部分：
- 参数注释：以冒号（:）标记，建议传入的参数类型
- 返回值注释：以 ->标记，建议函数返回的类型
```python
def funname(para1: expression, para2: expression = 5) -> expression:
    ...

```
expression 为函数注释。函数注释可以包含类型、帮助字符串，以及其他更多信息。一般为字符串表示注释，或变量类型名。


### "弱"声明
```python
names: list = ['Germey', 'Guido']
version: tuple = (3, 7, 4)
operations: dict = {'show': False, 'sort': True}
```

### “强 “的类型
```python
from typing import List, Tuple, Dict

names: List[str] = ['Germey', 'Guido']
version: Tuple[int, int, int] = (3, 7, 4)
operations: Dict[str, bool] = {'show': False, 'sort': True}
```


## 类型
- List
- Tuple、NamedTuple
- Dict、Mapping、MutableMapping
- NoReturn
- Sequence
- Any,Set、AbstractSet
- Callable
- Generator
- 等
下面特殊
### TypeVar

TypeVar，我们可以借助它来自定义兼容特定类型的变量，比如有的变量声明为 int、float、None 都是符合要求的，实际就是代表任意的数字或者空内容都可以，
其他的类型则不可以，比如列表 list、字典 dict 等等，像这样的情况，我们可以使用 TypeVar 来表示。 例如一个人的身高，便可以使用 int 或 float 或 None 来表示，但不能用 dict 来表示，所以可以这么声明：

```python
height = 1.75
Height = TypeVar('Height', int, float, None)
def get_height() -> Height:
    return height
```

### Union

联合类型，Union[X, Y] 代表要么是 X 类型，要么是 Y 类型。 联合类型的联合类型等价于展平后的类型：

### NewType

NewType，我们可以借助于它来声明一些具有特殊含义的类型，
```python
Person = NewType('Person', Tuple[str, int, float])
person = Person(('Mike', 22, 1.75))
```
这里实际上 person 就是一个 tuple 类型，我们可以对其像 tuple 一样正常操作。

```python
Union[Union[int, str], float] == Union[int, str, float]
```

### Optional

Optional，意思是说这个参数可以为空或已经声明的类型，即 Optional[X] 等价于 Union[X, None]。
但值得注意的是，这个并不等价于可选参数，当它作为参数类型注解的时候，不代表这个参数可以不传递了，而是说这个参数可以传为 None。

如当一个方法执行结果，如果执行完毕就不返回错误信息， 如果发生问题就返回错误信息，则可以这么声明
```python
def judge(result: bool) -> Optional[str]:
    if result: return 'Error Occurred'
```
