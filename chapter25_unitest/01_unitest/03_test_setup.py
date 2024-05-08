def setup_module():
    print("\n 这是setup_module方法，只执行一次，当有多个测试类的时候使用")


def teardown_module():
    print("这是 teardown_module方法，只执行一次，当有多个测试类的时候使用")


def setup_function():
    print("这是 setup_function方法，只执行一次，当有多个测试类的时候使用")


def teardown_function():
    print("这是 teardown_function方法，只执行一次，当有多个测试类的时候使用")


def test_five():
    print("this is test_five method")


def test_six():
    print("this is test_six method")


class TestPytest01:
    def setup_class(self):
        print("调用了setup_class1方法")

    def teardown_class(self):
        print("调用了teardown_class1方法")

    def setup_method(self):
        print("执行测试方法前的setup1操作")

    def teardown_method(self):
        print("执行测试方法后的teardown1操作")

    def test_one(self):
        print("this is test_one method")

    def test_two(self):
        print("this is test_two method")

    def setup(self):
        print("this is setup 方法")

    def teardown(self):
        print("this is teardown 方法")


class TestPytest02:
    def setup_class(self):
        print("调用了setup_class2方法")

    def teardown_class(self):
        print("调用了teardown_class2方法")

    def setup_method(self):
        print("执行测试方法前的setup2操作")

    def teardown_method(self):
        print("执行测试方法后的teardown2操作")

    def test_three(self):
        print("this is test_three method")

    def test_four(self):
        print("this is test_four method")
