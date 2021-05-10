"""享元模式【Flyweight】
意图：

运用共享技术有效地支持大量细粒度的对象。

享元旨在优化性能和内存使用。
内部状态：享元对象中不会随环境改变而改变的共享部分。比如围棋棋子的颜色。
外部状态：随环境改变而改变、不可以共享的状态就是外部状态。比如围棋棋子的位置。

适用性：

程序中使用了大量的对象，造成很大的存储开销。

如果删除对象的外部状态，可以用相对较少的共享对象取代很多组对象，就可以考虑使用享元模式。

比如：

假设我们正在设计一个性能关键的游戏，例如第一人称射击（First-Person Shooter，FPS）游戏。在FPS游戏中，玩家（士兵）共享一些状态，如外在表现和行为。
    例如，在《反恐精英》游戏中，同一团队（反恐精英或恐怖分子）的所有士兵看起来都是一样的（外在表现）。同一个游戏中，（两个团队的）所有士兵都有一些共同的动作，
    比如，跳起、低头等（行为）。这意味着我们可以创建一个享元来包含所有共同的数据。当然，士兵也有许多因人而异的可变数据，这些数据不是享元的一部分，
    比如，枪支、健康状况和地理位置等。

"""