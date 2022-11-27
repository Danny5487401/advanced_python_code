class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        # Date是硬编码，建议使用类方法 @classmethod
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        # 不是硬编码
        return cls(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0 and (0 < int(month) <= 12) and int(day) > 0:
            return True
        else:
            return False


if __name__ == "__main__":
    date = Date(2020, 11, 22)
    # 方法一：实际cpython解释器调用方式
    # Date.tomorrow(date)
    # 方法二 ： 简化写法
    date.tomorrow()
    print(date)

    # 2018-12-31 直接传入字符串，而不是2020,11,22
    # 方法一 ：外部处理
    # day_str = "2018-12-31"
    # year,month,day = tuple(day_str.split("-"))
    # new_day = Date(int(year),int(month),int(day))

    # 方法二：静态方法
    # new_day = Date.parse_from_string(day_str)
    # print(new_day)
    #
    # 方法三：使用类方法完成初始化
    # new_day = Date.from_string(day_str)
    # print(new_day)
    # 另外一种场景用于staticmethod：判断字符串是否正确，不需要返回类
    # print(Date.valid_str(day_str))
