"""
经典的《设计模式》一书归纳出23种设计模式。

这23种模式又可归为，创建型、结构型和行为型3大类。
a. 创建型:提供实例化的方法，为适合的状况提供相应的对象创建方法。
    背景： 社会化的分工越来越细，自然在软件设计方面也是如此，因此对象的创建和对象的使用分开也就成为了必然趋势。
        因为对象的创建会消耗掉系统的很多资源，所以单独对对象的创建进行研究，从而能够高效地创建对象就是创建型模式要探讨的问题。
    具体：1、工厂方法模式【Factory Method】
        2、抽象工厂模式【Abstract Factory】
        3、创建者模式【Builder】
        4、原型模式【Prototype】
        5、单例模式【Singleton】


b.结构型：通常用来处理实体之间的关系，使得这些实体能够更好地协同工作。
    背景：在解决了对象的创建问题之后，对象的组成以及对象之间的依赖关系就成了开发人员关注的焦点，
        因为如何设计对象的结构、继承和依赖关系会影响到后续程序的维护性、代码的健壮性、耦合性等。
    具体：1、外观模式【Facade】
        2、适配器模式【Adapter】
        3、代理模式【Proxy】
        4、装饰模式【Decorator】
        5、桥接模式【Bridge】
        6、组合模式【Composite】
        7、享元模式【Flyweight】

c.行为型:用于在不同的实体间进行通信，为实体之间的通信提供更容易，更灵活的通信方法。
    背景：在对象的创建和对象的结构问题都解决了之后，就剩下对象的行为问题了。
        如果对象的行为设计的好，那么对象的行为就会更清晰，
        它们之间的协作效率就会提高。
    具体：1、模板方法模式【Template Method】
        2、观察者模式【Observer】
        3、状态模式【State】
        4、策略模式【Strategy】
        5、职责链模式【Chain of Responsibility】
        6、命令模式【Command】
        7、访问者模式【Visitor】
        8、调停者模式【Mediator】
        9、备忘录模式【Memento】
        10、迭代器模式【Iterator】
        11、解释器模式【Interpreter】


"""