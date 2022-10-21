# 函数注释中要同时包含类型和帮助字符串，可以使用具有两个 key（例如：type 和 help）的 dict
def div(
    a: dict(type=float, help="the dividend"),
    b: dict(type=float, help="the divisor (must be different than 0)"),
) -> dict(type=float, help="the result of dividing a by b"):
    """Divide a by b"""
    return a / b


if __name__ == "__main__":
    print(div.__annotations__)
    print(div(5, 2))
