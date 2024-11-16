class SingletonClass(object):
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super