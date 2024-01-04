<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [mixins](#mixins)
  - [mixins 模式特点： 理解成接口， GenericViewSet真正的方法](#mixins-%E6%A8%A1%E5%BC%8F%E7%89%B9%E7%82%B9-%E7%90%86%E8%A7%A3%E6%88%90%E6%8E%A5%E5%8F%A3-genericviewset%E7%9C%9F%E6%AD%A3%E7%9A%84%E6%96%B9%E6%B3%95)
  - [看DRF](#%E7%9C%8Bdrf)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# mixins
编码不推荐mro多继承，一般就继承一个类，推荐mixin模式


## mixins 模式特点： 理解成接口， GenericViewSet真正的方法
1.功能单一
2.不和基类关联，可以和任意基类组合，基类可以不和mixin关联就能初始化成功
3.在mixin中不要super这种方法

## 看DRF
```python
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
```