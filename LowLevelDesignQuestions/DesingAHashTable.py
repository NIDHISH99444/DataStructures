class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
                if item.key == key:
                    return item.value
        # try:
        #     raise KeyError('Asked value not in hash map ')
        # except Exception as e:
        #     print("Asked value not in hash map ")

    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        #raise KeyError('Key not found')

h=HashTable(5)
h.set(0,1)
h.set(5,2)
h.set(2,3)
h.set(2,4)
print(h.get(2))
h.set(7,5)

print(h.get(3))
print(h.remove(7))
print(h.get(7))