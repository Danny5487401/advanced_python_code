# __getattr__,__getattribute__这是完整写法

# __getattr__ 在查找不到属性的时候调用

from datetime import date,datetime
class User:
    def __init__(self,name,birthday,info):
        self.name = name
        self.birthday = birthday
        self.info = info

    # 查找不到时调用
    def __getattr__(self, item):
        # return "not find attr"
        # 添加逻辑
        return self.info[item]

    # 更高级，首先调用这函数，不管任何条件，把握所有属性的入口
    # def __getattribute__(self, item):
    #     return "danny1"



if __name__ == "__main__":
    user = User("danny", date(year=2000, month=1, day=11),info = {"company": "xiada"} )
    # 没写 __getattr__
    # user.age # AttributeError: 'User' object has no attribute 'age'
    # 写了 __getattr__
    # print(user.age)  #not find attr
    print(user.company)
