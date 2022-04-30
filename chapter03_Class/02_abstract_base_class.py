# abc 对应java的接口interface，go的interface

# 抽象基类不能实例化
# 抽象基类用于判断类型和实现接口（建议用mixin）


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        # item是索引  变成可迭代对象
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["danny", "tom", "joy"])

# 1. 检查某个类是否有某种方法
print(hasattr(company, "__len__"))
# 判断类型
from collections.abc import Sized

print(isinstance(company, Sized))
print(len(company))


# 2. 需要强制子类必须实现某些方法， 实现一个web框架，集成cache(redis,cache,memcache)
# 需要设计一个抽象基类，指定子类必须实现某些方法

## 方式一
# 模拟一个抽象基类
class CacheBase:
    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


# 必须实现方法
class RedisCache(CacheBase):
    def set(self, key, value):
        pass


redis_cache = RedisCache()
# 方法一：调用时候出现异常
redis_cache.set("key", "value")

# 全局的abc
import abc


## 方式二：使用abc
class CacheBase1(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache1(CacheBase1):
    def set(self, key, value):
        pass

    def get(self, key):
        pass


# 方法二：初始化就会报异常
redis_cache = RedisCache1()
