import configparser


class Operation(object):

    def __init__(self, cf):
        self.cf = cf

    def get_sections(self):
        print('------------------------ ----- ---------------------------')
        # 得到所有的section，并以列表的形式返回
        print('Current function is get_sections, the answer is:', self.cf.sections())
        return

    def get_options(self, option_name):
        print('------------------------ ----- ---------------------------')
        # 得到该section的所有option (key值)
        print('Current function is get_options, the answer is:', self.cf.options(option_name))
        return

    def get_items(self, option_name):
        print('------------------------ ----- ---------------------------')
        # 得到该section的所有键值对
        print('Current function is get_items, the answer is:', self.cf.items(option_name))
        return

    def get_editor_value(self, option_name, key_name):
        print('------------------------ ----- ---------------------------')
        # 得到section中option的值，返回为string类型，指定标签下面的key对应的value值
        print("Current function[get] is get_editor_value, the answer from {}'s {} is: {}".format(option_name, key_name,
                                                                                                 self.cf.get(option_name,
                                                                                                             key_name)))
        return

    def get_editor_int_value(self, option_name, key_name):
        print('------------------------ ----- ---------------------------')
        # 得到section中的option值，返回为int类型
        print("Current function[get] is get_editor_value, the answer from {}'s {} is: {}".format(option_name, key_name,
                                                                                                 self.cf.get(option_name,
                                                                                                             key_name)))

        return

    def has_section(self, section_name):
        # 判定是否存在某section
        print('------------------------ ----- ---------------------------')
        print('has {} sections:{}'.format(section_name, self.cf.has_section(section_name)))

    def has_option(self, section_name, option_name):
        # 判定是否存在某section
        print('------------------------ ----- ---------------------------')
        print("has {}'s {} value:{}".format(section_name, option_name, self.cf.has_option(section_name, option_name)))

    def set_add_function(self, section_name):
        # 添加一个节点section_name,但此时尚未写入文件
        print('------------------------ ----- ---------------------------')
        print('former sections:', self.cf.sections())
        self.cf.add_section(section_name)
        print('later sections:', self.cf.sections())
        return

    def set_section_value(self, section_name, option_name, key_name):
        print('------------------------ ----- ---------------------------')
        # 在已存在的节点中添加一个键值对k1 = v1 ,如果该节点不存在则报错,如果key已经存在，则修改value
        self.cf.set(section_name, option_name, key_name)
        self.cf.write(open("config.ini", "w"))             # 将添加的option写入配置文件
        return

    def remove_option(self, section_name, option_name):
        print('------------------------ ----- ---------------------------')
        # 删除section中的option值
        self.cf.remove_option(section_name, option_name)   # 删除section中的option值
        self.cf.write(open("config.ini", "w"))             # 将添加的option写入配置文件
        return

    def remove_section(self, section_name):
        print('------------------------ ----- ---------------------------')
        # 删除section
        self.cf.remove_section(section_name)               # 删除section
        self.cf.write(open("config.ini", "w"))             # 将添加的option写入配置文件
        return


if __name__ == '__main__':
    # 1. 创建ConfigParser对象。并调用read()函数打开配置文件，里面填的参数是地址
    cf = configparser.ConfigParser()
    cf.read('./config.ini')
    ops = Operation(cf)
    ops.get_sections()
    ops.get_options('editor')
    ops.get_items('editor')
    ops.get_editor_value('editor', 'job')
    ops.get_editor_int_value('editor', 'id')
    ops.has_section('editor')
    ops.has_option('editor', 'id')
    ops.set_add_function('new_section')
    ops.set_section_value('new_section', 'set', 'new_value')
    print("current new_section is :", ops.cf.items('new_section'))
    ops.remove_option('new_section', 'set')
    ops.remove_section('new_section')

