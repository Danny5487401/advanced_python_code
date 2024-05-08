from unittest.mock import Mock
import unittest


class TestMock(unittest.TestCase):
    def test_magic_mock(self):
        mock = Mock()
        # 当 return_value 和 side_effect 同时设置时，会返回side_effect的结果。
        # 1 side_effect 是一个异常:
        # mock.side_effect = ValueError("hello")

        # 2 side_effect 是一个可迭代对象：
        # mock.side_effect = [1, 2, 3]

        # 3 side_effect 为一个函数
        mock.side_effect = side_func
        print(f"-----{mock()}-------")

    def test_first_last_name(self):
        formatted_name = get_formatted_name("kobe", "bryant")
        self.assertEqual(formatted_name, "Kobe Bryant")


def side_func(value: int = 1):
    return value * 2


def get_formatted_name(first, last):
    full_name = first + " " + last
    return full_name.title()


if __name__ == "__main__":
    # 创建测试套件
    suite = unittest.TestSuite()
    suite.addTest(TestMock("test_magic_mock"))
    suite.addTest(TestMock("test_first_last_name"))

    # 创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suite)
