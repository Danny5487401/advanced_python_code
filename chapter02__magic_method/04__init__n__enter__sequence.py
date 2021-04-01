#先__init__ 再__enter__

class C:
    def __init__(self):
        print("init")

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def __del__(self):
        print("del")



# if __name__ == '__main__':
#     a = C() #init
#     print("st")
#     with a:
#         print("hi")
#     with a:
#         print("hi")
#     print("ed")

if __name__ == '__main__':
    print("st")
    with C():
        print("hi")
    with C():
        print("hi")
    print("ed")