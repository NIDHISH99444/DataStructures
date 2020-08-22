# Python program to find largest
# BST in a Binary Tree.

INT_MIN = -2147483648
INT_MAX = 2147483647



class newNode:


    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def largestBSTBT(root):

    if (root == None):
        return True,1,INT_MIN,INT_MAX
    if (root.left == None and root.right == None):
        return True,1, root.data, root.data

    l = largestBSTBT(root.left)
    r = largestBSTBT(root.right)


    ret = [False, 0, 0, 0]


    if (l[0] and r[0] and l[3] <
            root.data and r[2] > root.data):
        ret[2] = min(l[2], root.data)
        ret[3] = max(r[3],root.data)


        ret[1] = 1+l[1]+r[1]
        ret[0] = True

        return ret



    ret[1] = max(l[1], r[1])
    ret[0] = False

    return ret


if __name__ == '__main__':

    root = newNode(50)
    root.left = newNode(30)
    root.right = newNode(60)
    root.left.left = newNode(5)
    root.left.right = newNode(20)
    root.right.left = newNode(45)
    root.right.right= newNode(70)
    root.right.right.left=newNode(65)
    root.right.right.right=newNode(80)
    print("Size of the largest BST is",
          largestBSTBT(root)[1])

    root = newNode(60)
    root.left = newNode(65)
    root.right = newNode(70)
    root.left.left = newNode(50)
    print("Size of the largest BST is",
          largestBSTBT(root)[1])

# This code is contributed
