
"""
原型模式
用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
当我们想复制一个复杂对象时，使用原型模式会很方便。
对于复制复杂对象，我们可以将对象当作是从数据库中获取的，
并引用其他一些也是从数据库中获取的对象。
若通过多次重复查询数据来创建一个对象，则要做很多工作。
在这种场景下使用原型模式要方便得多。
"""
import copy
from collections import OrderedDict


class Book(object):
    # 创建一个书籍对象
    def __init__(self, name, authors, price, **rest):
        '''rest的例子有：出版商、长度、标签、出版日期'''
        self.name = name
        self.authors = authors
        self.price = price  # 单位为美元
        self.__dict__.update(rest)  # self.__dict__是包含name,authors,price,**rest的元素的字典

    def __str__(self):
        mylist = []
        # 对对象中的内置字典进行升序排序，然后再固定字典元素位置
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


class ProtoType(object):
    # 创建一个原型
    def __init__(self):
        self._object = {}

    def register_object(self, name, obj):
        """注册一个对象"""
        self._object[name] = obj

    def unregister_object(self, name, obj):
        """删除一个对象"""
        del self._object[name]

    def clone(self, identifier, **attr):
        """根据 identifier 在原型列表中查找原型对象并克隆"""
        obj = copy.deepcopy(self._object.get(identifier))
        if not obj:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj.__dict__.update(attr)  # 用新的属性值替换原型对象中的对应属性
        return obj


def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'),
              price=118, publisher='Prentice Hall', length=228, publication_date='1978-02-22',
              tags=('C', 'programming', 'algorithms', 'data structures'))
    prototype = ProtoType()  # 实例化原型
    cid = 'k&r-first'
    prototype.register_object(cid, b1)  # 注册一个书籍原型
    # 对书籍原型进行克隆
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99,
                         length=274, publication_date='1988-04-01', edition=2)
    for i in (b1, b2):
        print(i)
    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))


if __name__ == '__main__':
    main()

"""
总结：
用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
原型模式本质就是克隆对象，
所以在对象初始化操作比较复杂的情况下，很实用，能大大降低耗时，提高性能，
因为“不用重新初始化对象，而是动态地获得对象运行时的状态”。

浅拷贝（Shallow Copy）:指对象的字段被拷贝，而字段引用的对象不会被拷贝，
拷贝的对象和源对象只是名称相同，但是他们共用一个实体。
深拷贝（deep copy）:对对象实例中字段引用的对象也进行拷贝。

比如：当我们出版了一本书《Python 设计模式 1.0版》，若10 年后我们觉得这本书跟不上时代了，
这时候需要去重写一本《Python 设计模式 2.0版》，
那么我们是完全重写一本书呢？还是在原有《Python 设计模式 1.0版》的基础上进行修改呢？
当然是后者，这样会省去很多排版、添加原有知识等已经做过的工作。
"""

