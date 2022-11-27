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