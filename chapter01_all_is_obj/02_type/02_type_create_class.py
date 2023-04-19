def echo_bar(self):
    print(self.bar)


class Foo(object):
    bar = True


FooChild = type("FooChild", (Foo,), {"echo_bar": echo_bar})


if __name__ == "__main__":
    print(hasattr(Foo, "echo_bar"))
    print(hasattr(FooChild, "echo_bar"))
