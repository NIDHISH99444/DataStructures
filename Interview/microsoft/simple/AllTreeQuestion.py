class Tree:

    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def inorder(root,k):
    stack=[]
    while stack or root:
        if root:
            stack.append(root)
            root=root.right
        else:
            root=stack.pop()
            k-=1
            if k==0:
                return root.val
            root=root.left
def leftBoundary(root):
    if not root:
        return
    if root:
        if root.left:
            print(root.val,end=" ")
            leftBoundary(root.left)
        elif root.right:
            print(root.val,end=" ")
            leftBoundary(root.right)
def rightBoundary(root):
    if not root:
        return
    if root:
        if root.right:
            rightBoundary(root.right)
            print(root.val,end=" ")

        elif root.left:
            rightBoundary(root.left)
            print(root.val,end=" ")

def leaf(root):
    if not root:
        return
    if not root.left and not root.right:
        print(root.val,end=" ")
    leaf(root.left)
    leaf(root.right)
def boundary(root):
    if not root :
        return
    leftBoundary(root)
    leaf(root)
    rightBoundary(root.right)

def postOrderIterative(root):
    traversal,stack=[],[(root,False)]
    while stack:
        node,visited=stack.pop()
        if node:
            if visited:
                traversal.append(node.val)
            else:
                stack.append((node,True))
                stack.append((node.right,False))
                stack.append((node.left, False))

    return traversal
#for checking code for BSt
root=Tree(10)
root.left=Tree(5)
root.right=Tree(20)
root.right.right=Tree(30)
# checking codes for Binary Tree
root1=Tree(8)
root1.left=Tree(3)
root1.right=Tree(10)
root1.left.left=Tree(1)
root1.left.right=Tree(6)
root1.right.left=Tree(7)
root1.right.right=Tree(9)

k=2
print("Kth largest Element in BST")
print(inorder(root,k))
print("Boudary Traversal of Tree")
boundary(root1)
print()
print("Post order iterative solution")
print(postOrderIterative(root1))