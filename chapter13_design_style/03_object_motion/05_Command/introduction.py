"""命令模式【Command】
意图：

将一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化；对请求排队或记录请求日志，以及支持可撤消的操作。

抽象出待执行的动作以参数化某对象，你可用过程语言中的回调（callback）函数表达这种参数化机制。所谓回调函数是指函数先在某处注册，而它将在稍后某个需要的时候被调用。Command 模式是回调机制的一个面向对象的替代品。

适用性：

在不同的时刻指定、排列和执行请求。一个Command对象可以有一个与初始请求无关的生存期。如果一个请求的接收者可用一种与地址空间无关的方式表达，那么就可将负责该请求的命令对象传送给另一个不同的进程并在那儿实现该请求。

支持取消操作。Command的Excute 操作可在实施操作前将状态存储起来，在取消操作时这个状态用来消除该操作的影响。Command 接口必须添加一个Unexecute操作，该操作取消上一次Execute调用的效果。执行的命令被存储在一个历史列表中。可通过向后和向前遍历这一列表并分别调用Unexecute和Execute来实现重数不限的“取消”和“重做”。

支持修改日志，这样当系统崩溃时，这些修改可以被重做一遍。在Command接口中添加装载操作和存储操作，可以用来保持变动的一个一致的修改日志。从崩溃中恢复的过程包括从磁盘中重新读入记录下来的命令并用Execute操作重新执行它们。

用构建在原语操作上的高层操作构造一个系统。这样一种结构在支持事务( transaction)的信息系统中很常见。一个事务封装了对数据的一组变动。Command模式提供了对事务进行建模的方法。Command有一个公共的接口，使得你可以用同一种方式调用所有的事务。同时使用该模式也易于添加新事务以扩展系统。

比如：

1、命令设计模式帮助我们将一个操作（撤销、重做、复制、粘贴等）封装成一个对象。简而言之，这意味着创建一个类，包含实现该操作所需要的所有逻辑和方法。这样做的优势如下所述。

2、我们并不需要直接执行一个命令。命令可以按照希望执行。
调用命令的对象与指导如何执行命令的对象解耦。调用者无需知道命令的任何实现细节。
如果有意义，可以把多个命令组织起来，这样调用者能够按顺序执行它们。例如，在实现一个多层撤销命令时，这是很有用的。

3、事务型行为和日志记录：事务型行为和日志记录对于为变更记录一份持久化日志是很重要的。操作系统用它来从系统崩溃中恢复，关系型数据库用它来实现事务，文件系统用它来实现快照，而安装程序（向导程序）用它来恢复取消的安装。

4、宏：在这里，宏是指一个动作序列，可在任意时间点按要求进行录制和执行。流行的编辑器（比如，Emacs和Vim）都支持宏。

"""