class Singelton:
    _instance =None
    def __new__(cls):
        if cls._instance is None:
            print("onetime")
            cls._instance =super().__new__(cls)
        return cls._instance
    

s=Singelton()
s1=Singelton()
