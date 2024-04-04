class Node :
    def __init__(self,key,value) -> None:
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.store={}
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head

    def _addNodeToFront(self,node):
        old=self.head.next
        node.prev=self.head
        node.next=old
        self.head.next=node
        old.prev=node

    def _deleteNode(self,node):
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p




    def get(self,key):
        if key not in self.store:
            return -1 
        else:
            node=self.store[key]
            self._deleteNode(node)
            self._addNodeToFront(node)
            return node.value
        
    def put(self,key,value):
        if key not in self.store:
            node=Node(key,value)
            self.store[key]=node
            self._addNodeToFront(node)
        elif key in self.store :
            node=self.store[key]
            self._deleteNode(node)
            self._addNodeToFront(node)
            node.value=value    #remember
        if len(self.store) > self.capacity:
            last_node=self.tail.prev
            self._deleteNode(last_node)
            del self.store[last_node.key]
            


capacity=2
obj = LRUCache(capacity)
obj.put(1,1)
obj.put(2,2)
param_1 = obj.get(1)
print("get1",param_1)
obj.put(3,3)
param_1 = obj.get(2)
print("get2",param_1)
obj.put(4,4)
param_1 = obj.get(1)
print(param_1)
param_1 = obj.get(3)
print(param_1)
param_1 = obj.get(4)
print(param_1)




[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]