class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
    def AddNode(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = Node(val)

    def printNode(self):
        while self.head :
            print(self.head.val,end=" ")
            self.head=self.head.next

    def removeDuplicates(self):
        dummy=curr=Node(0)
        head1=self.head
        dummy.next=head1
        while self.head and self.head.next:
            if self.head and self.head.next.val:
                while self.head and self.head.next and self.head.val==self.head.next.val   :
                    self.head=self.head.next
                self.head = self.head.next
                curr.next=self.head
            else :
                curr = curr.next
                self.head=self.head.next
        return dummy.next

    def add(self,n1, n2, carry=0):
        if not n1 and not n2 and carry <= 0:
            return None
        total = 0
        if n1:
            total = n1.val
        total += carry
        if n2:
            total += n2.val
        n1_next = n1.next if n1 else None
        n2_next = n2.next if n2 else None
        carry = total // 10
        ret = LinkedList(total % 10)
        ret.next =self.add(n1_next, n2_next, carry)
        return ret

    def addTwoNumbers(self, l1, l2) :
        return self.add(l1, l2, 0)


myLL = LinkedList()
myLL.AddNode(7)
myLL.AddNode(5)
myLL.AddNode(9)
myLL.AddNode(4)
myLL.AddNode(6)
myLL.printNode()
print()
myLL1 = LinkedList()
myLL1.AddNode(8)
myLL1.AddNode(4)
myLL1.printNode()
res=LinkedList()
res.addTwoNumbers(myLL,myLL1)
res.printNode()



