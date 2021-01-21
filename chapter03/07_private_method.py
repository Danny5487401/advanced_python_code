# 数据封装和私有属性


class User:
    def __init__(self,birthday):
        # self.birthday = birthday
        # 双下划线  子类和外部获取不到
        self.__birthday = birthday


    def get_age(self):
        return 2021-self.__birthday.year
class Student:
    def __init__(self,birthday):
        self.__birthday = birthday

class Date:
    # 构造函数
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{year}/{month}/{day}" .format(year= self.year, month = self.month, day = self.day)

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        # Date是硬编码，建议使用类方法
        return Date(int(year),int(month),int(day))

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        # 不是硬编码
        return cls(int(year),int(month),int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0 and (int(month)>0 and int(month)<=12) and int(day)>0:
            return True
        else:
            return False


if __name__ == "__main__":
    user = User(Date(1996,1,2))
    print(user.get_age())
    # 外部引用看得到
    # print(user.birthday)
    # 变形 obj._classname__attr
    print(user._User__birthday)
