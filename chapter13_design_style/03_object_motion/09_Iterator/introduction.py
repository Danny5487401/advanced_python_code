"""迭代器模式【Iterator】
意图：

提供一种方法顺序访问一个集合对象中各个元素, 而又不需暴露该对象的内部表示。

主要解决： 不同的方式来遍历整个集合对象。

适用性：

访问一个聚合对象的内容而无需暴露它的内部表示。

支持对聚合对象的多种遍历。

为遍历不同的聚合结构提供一个统一的接口(即, 支持多态迭代)。

比如：

遍历一个集合。
"""