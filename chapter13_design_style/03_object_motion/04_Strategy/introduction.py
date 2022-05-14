"""
4、策略模式【Strategy】
意图：

定义一系列的算法,把它们一个个封装起来, 并且使它们可相互替换。

主要解决：在有多种算法相似的情况下，使用 if…else 所带来的复杂和难以维护的问题。
适用性：

许多相关的类仅仅是行为有异。

“策略”提供了一种用多个行为中的一个行为来配置一个类的方法。

需要使用一个算法的不同变体。例如，你可能会定义一些反映不同的空间/时间权衡的算法。当这些变体实现为一个算法的类层次时，可以使用策略模式。

算法使用客户不应该知道的数据。可使用策略模式以避免暴露复杂的、与算法相关的数据结构。

一个类定义了多种行为, 并且这些行为在这个类的操作中以多个条件语句的形式出现。将相关的条件分支移入它们各自的Strategy类中以代替这些条件语句

比如：

商场搞活动，可以按正常收费、打折收费、返利收费等支付方式，通过 一个具体的策略类来控制支付方式（也就是不同的算法）


"""