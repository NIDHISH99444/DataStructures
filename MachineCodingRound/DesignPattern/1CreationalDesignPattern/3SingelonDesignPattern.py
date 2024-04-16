class Singelton:
    _instance=None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=super().__new__(cls, *args, **kwargs)
            print(f"instance created once -> {cls._instance}")
        return cls._instance

s=Singelton()
s=Singelton()