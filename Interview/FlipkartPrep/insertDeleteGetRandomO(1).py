import random
class RandomizedSet(object):

    def __init__(self):
        self.l = []
        self.d = {}

    def insert(self, val):
        if val in self.l:
            return False
        self.d[val]=len(self.l)
        self.l.append(val)
        print(self.l, self.d)
        return True
    def remove(self, val):
        if val not in self.l:
            return False
        index=self.d[val]
        self.l[index]=self.l[-1]
        self.d[self.l[-1]]=index
        self.l.pop()
        del self.d[val]
        print(self.l,self.d)
        return True


    def getRandom(self):
        return random.choice(self.l)

#Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(4)
print(param_1)
param_2 = obj.insert(3)
print(param_2)
param_3 = obj.insert(6)
print(param_3)
param_4 = obj.remove(3)
print(param_4)
print(obj.getRandom())