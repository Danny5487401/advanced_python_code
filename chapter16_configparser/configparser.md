# configparser

configparser解析的配置文件的格式为ini的配置文件格式 （xxx.ini），就是文件中由多个section构成，每个section下又有多个配置项
```ini
;配置文件
#  定义section0
[section0]
 
key0 = value0
key1 = value1
 
[section1]
 
key2 = value2
key3 = value3
```

## 常见函数

- sections() 得到所有的section，并以列表的形式返回
- options(section) 得到该section的所有option (key值)
- items(section) 得到该section的所有键值对，返回结果是列表中包含的元祖
- get(section, option) 得到section中option的值，返回为string类型，指定标签下面的key对应的value值
- getint(section, option) 得到section中的option值，返回为int类型
- has_section(section) 判断指定的option是否存在
- has_option(section,option)判断指定option中的option是否存在
- add_section(str) 往配置文件中添加section
- set(section, name, value) 在section下设置name=value
- remove_option(section,option)删除指定节点section中的option
- remove_section(section)删除指定的section
- read(filename) 读取配置文件， read(’./config.ini’)
- write(obj_file) 写入配置文件 ，write(open(“config.ini”, “w”))
