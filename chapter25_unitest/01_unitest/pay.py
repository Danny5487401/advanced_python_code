# 场景一： pay 是函数
def pay():
    """假设这里是一个支付的功能,未开发完
    支付成功返回：{"result": "success", "reason":"null"}
    支付失败返回：{"result": "fail", "reason":"余额不足"}
    reason返回失败原因
    """
    pass
    return


# 场景二： pay 是类方法
class Unipay:
    def pay_by_aliyun(self):
        """假设这里是一个支付的功能,未开发完
        支付成功返回：{"result": "success", "reason":"null"}
        支付失败返回：{"result": "fail", "reason":"余额不足"}
        reason返回失败原因
        """
        pass
        return


def pay_statues():
    """根据支付的结果success or fail，判断跳转到对应页面"""
    result = pay()
    try:
        if result["result"] == "success":
            return "支付成功"
        elif result["result"] == "fail":
            print("失败原因：%s" % result["reason"])
            return "支付失败"
        else:
            return "未知错误异常"
    except:
        return "Error, 服务端返回异常!"


class UnipayStatues:
    def pay_by_aliyun_status(self):
        """根据支付的结果success or fail，判断跳转到对应页面"""
        result = Unipay().pay_by_aliyun()
        try:
            if result["result"] == "success":
                return "支付成功"
            elif result["result"] == "fail":
                print("失败原因：%s" % result["reason"])
                return "支付失败"
            else:
                return "未知错误异常"
        except:
            return "Error, 服务端返回异常!"
