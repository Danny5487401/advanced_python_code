from unittest import mock
import unittest
from chapter25_unitest import pay


class TestPayStatues(unittest.TestCase):
    """单元测试用例"""

    @mock.patch("chapter25_unitest.pay.pay")
    def test_01(self, mock_pay):
        """测试支付成功场景"""
        # 方法一：mock一个支付成功的数据
        # temple.zhifu = mock.Mock(return_value={"result": "success", "reason":"null"})

        # 方法二：mock.path装饰器模拟返回结果
        mock_pay.return_value = {"result": "success", "reason": "null"}
        # 根据支付结果测试页面跳转
        statues = pay.pay_statues()
        self.assertEqual(statues, "支付成功")

    @mock.patch("chapter25_unitest.pay.pay")
    def test_02(self, mock_pay):
        """测试支付失败场景"""
        # mock一个支付成功的数据

        mock_pay.return_value = {"result": "fail", "reason": "余额不足"}
        # 根据支付结果测试页面跳转
        statues = pay.pay_statues()
        self.assertEqual(statues, "支付失败")


class TestUnipayClass(unittest.TestCase):
    """单元测试用例"""

    @mock.patch("chapter25_unitest.pay.Unipay")
    def test_01(self, mock_unipay):
        """测试支付成功场景"""
        a = mock_unipay.return_value  # 先返回实例，对类名称替换
        # 通过实例调用方法，再对方法的返回值替换
        a.pay_by_aliyun.return_value = {"result": "success", "reason": "null"}
        # 根据支付结果测试页面跳转
        statues = pay.UnipayStatues().pay_by_aliyun_status()
        self.assertEqual(statues, "支付成功")

    @mock.patch("chapter25_unitest.pay.Unipay")
    def test_02(self, mock_unipay):
        """测试支付失败场景"""
        b = mock_unipay.return_value  # 先返回实例，对类名称替换
        # 通过实例调用方法，再对方法的返回值替换
        b.pay_by_aliyun.return_value = {"result": "fail", "reason": "余额不足"}
        # 根据支付结果测试页面跳转
        statues = pay.UnipayStatues().pay_by_aliyun_status()
        self.assertEqual(statues, "支付失败")


if __name__ == "__main__":
    unittest.main()
