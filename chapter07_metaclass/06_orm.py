# 需求 orm：类映射数据库中的一张表
import numbers


class Field:
    pass


class IntField(Field):
    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("int value need")
            elif min_value < 0:
                raise ValueError("positive value needed")

        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError("int value need")
            elif max_value < 0:
                raise ValueError("positive value needed")

        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value must be smaller than max_value")

    # 数据描述符
    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        # 保存值
        if value < 0:
            raise ValueError("POSITIVE value needed")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must be between min_value and max_value")
        # 如果instance.age 会死循环
        self._value = value

    def __delete__(self, instance):
        pass


class CharField(Field):
    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_column = db_column
        self.max_length = max_length
        if max_length is None:
            raise ValueError("max_length needs to be specified")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value needed")
        if len(value) > self.max_length:
            raise ValueError("len of value excesses len of max_length")
        self._value = value


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, *args, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, *args, **kwargs)
        fields = {}
        for key, value in attrs.items():
            # 判断是不是表中的列
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
        if db_table is not None:
            db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, *args, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))

        # sql = 'insert user(name,age) value("danny",30)'
        # .join 要同种类型
        sql = 'insert {db_table}({fields}) values({values})'.format(db_table=self._meta["db_table"],
                                                                    fields=",".join(fields), values=",".join(values))
        pass


# class User(metaclass=ModelMetaClass):
class User(BaseModel):
    # # 初始化让基类完成
    # def __init__(self,name, age):
    #     pass
    name = CharField(db_column="name", max_length=10)
    age = IntField(db_column="age", min_value=1, max_value=100)

    class Meta:
        db_table = "user"


if __name__ == "__main__":
    # 方法一
    # user = User()
    # user.name ="danny"
    # user.age =26
    # 方法二
    user = User(name="danny2", age=11)
    user.save()
