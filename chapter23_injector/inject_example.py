from injector import Module, provider, Injector, inject, singleton, threadlocal
import sqlite3


class IModelView(object):
    view = "test"

    def __init__(self):
        pass


class IRequestHandler(object):
    pass


class Configuration(object):
    def __init__(self, connection_string):
        self.connection_string = connection_string


class RequestHandler(IRequestHandler):
    @inject
    def __init__(
        self, db: sqlite3.Connection, configuration: Configuration, my: "MyClass"
    ):
        self._db = db
        self._configuration = configuration
        self.my = my

    def get(self):
        cursor = self._db.cursor()
        cursor.execute("SELECT key, value FROM data ORDER by key")
        return cursor.fetchall()


class MyClass:
    def __init__(self, value: int) -> None:
        self.value = value


def factory():
    print("providing")
    return MyClass(42)


def create_my_class(binder):
    configuration = Configuration(":memory:")
    binder.bind(Configuration, to=configuration, scope=threadlocal)
    binder.bind(MyClass, to=factory, scope=singleton)


class DatabaseModule(Module):
    @singleton
    @provider
    def provide_sqlite_connection(
        self, configuration: Configuration
    ) -> sqlite3.Connection:
        conn = sqlite3.connect(configuration.connection_string)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS data (key PRIMARY KEY, value)")
        cursor.execute('INSERT OR REPLACE INTO data VALUES ("hello", "world")')
        return conn


class ModelView(IModelView):
    view = "test1"

    @inject
    def __init__(self, req: IRequestHandler, my: MyClass):
        self.req = req
        self.my = my


if __name__ == "__main__":
    injector = Injector([create_my_class, DatabaseModule()], auto_bind=False)

    handler = injector.create_object(RequestHandler)
    injector.binder.bind(IRequestHandler, handler)

    model_view = injector.create_object(ModelView)
    injector.binder.bind(IModelView, model_view)

    hd = injector.get(IRequestHandler)
    print(tuple(map(str, hd.get()[0])))
