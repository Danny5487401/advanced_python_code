<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [抽象类概念](#%E6%8A%BD%E8%B1%A1%E7%B1%BB%E6%A6%82%E5%BF%B5)
  - [为什么要有抽象类](#%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E6%9C%89%E6%8A%BD%E8%B1%A1%E7%B1%BB)
  - [作用](#%E4%BD%9C%E7%94%A8)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 抽象类概念

抽象类是一个特殊的类，只能被继承，不能实例化

## 为什么要有抽象类
其实在未接触抽象类概念时，我们可以构造香蕉、苹果、梨之类的类，然后让它们继承水果这个基类，水果的基类包含一个eat函数。

　　但是你有没有想过，我们可以将香蕉、苹果、梨实例化，去吃香蕉、苹果、梨。但是我们却不能将水果实例化，因为我们无法吃到叫水果的这个东西。

　　所以抽象类中只能有抽象方法（没有实现功能），该类不能被实例化，只能被继承，且子类必须实现抽象方法。

## 作用
在不同的模块中通过抽象基类来调用，可以用最精简的方式展示出代码之间的逻辑关系，让模块之间的依赖清晰简单。

抽象类的编程，让每个人可以关注当前抽象类的方法和描述，而不需要考虑过多的实现细节，这对协同开发有很大意义，也让代码可读性更高
