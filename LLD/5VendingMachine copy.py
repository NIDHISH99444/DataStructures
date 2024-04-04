class VendingMachine : 
    __instance=None

    def __new__(cls,*args):
        print(f"args : {args}")
        if cls.__instance is None:
             cls.__instance=super().__new__(cls)
        return cls.__instance 
    
    def __init__(self,logger):
        self.__logger=logger
    
    def printLogger(self):
        print("Name",self.__logger)


v1=VendingMachine("nidhish")
v1.printLogger()

v2=VendingMachine("nidhish1")
v2.printLogger()


