from typing import List
from dataclasses import dataclass
from dataclasses import field
import random


def get_random_marks():
    return [random.randint(1, 10) for _ in range(5)]


@dataclass(order=True)
class Student:
    age: int
    weight: float
    height: float
    name: str = field(
        compare=False
    )  # compare = False tells the dataclass to not use name for comparison methods
    marks: List[int] = field(
        default_factory=get_random_marks, compare=False
    )  # default_factory 不接受参数


class Number:
    def __init__(self, val):
        self.val = val


@dataclass
class Number2:
    # 初始化
    # 1 无需定义__init__，然后将值赋给self，dataclass负责处理它
    # 2 我们以更加易读的方式预先定义了成员属性，以及类型提示。我们现在立即能知道val是int类型
    val: int


if __name__ == "__main__":
    n1 = Number(1)
    print(n1.val)
    print(
        n1
    )  # <__main__.Number object at 0x100dc4be0>  无法知悉对象的作用，并且会导致糟糕的调试体验

    n2 = Number2(2)
    print(n2.val)
    print(n2)  # Number2(val=2) 会自动添加一个__repr__函数，这样我们就不必手动实现它了。

    user_1 = Student(name="John Doe", age=23, weight=70, height=1.70)
    user_2 = Student(name="Adam", age=24, weight=65, height=1.60)
    print(user_1 < user_2)
    print(user_1.marks)
