######################### example_inspect.py ##########################
def module_level_function(arg1, arg2, *args, **kwargs):
    """This function is declare in the module"""
    local_variable = arg1 * 2
    return local_variable


class A(object):
    """The A class"""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Return the name of instance"""
        return self.name

    @classmethod
    def test(cls):
        pass

    @staticmethod
    def do_nothing():
        pass


instance_of_a = A("simple_instance")


class B(A):
    """This is B class
    it is Derived from A"""

    # This method is not part of A
    def do_something(self):
        """Does some works"""

    def get_name(self):
        """Overrides version from A"""
        return "B(" + self.name + ")"
