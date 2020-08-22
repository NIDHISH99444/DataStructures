from collections import defaultdict
class newNode:


    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def distanceK( root, target, K):
    adj, res, visited = defaultdict(list), [], set()

    def dfs(node):
        if node.left:
            adj[node.data].append(node.left.data)
            adj[node.left.data].append(node.data)
            dfs(node.left)
        if node.right:
            adj[node.data].append(node.right.data)
            adj[node.right.data].append(node.data)
            dfs(node.right)

    dfs(root)

    def dfs2(node, d):
        if d < K:
            visited.add(node)
            for v in adj[node]:
                if v not in visited:
                    dfs2(v, d + 1)
        else:
            res.append(node)

    dfs2(target, 0)
    return res

if __name__ == '__main__':
    root = newNode(50)
    root.left = newNode(30)
    root.right = newNode(60)
    root.left.left = newNode(5)
    root.left.right = newNode(20)
    # root.right.left = newNode(45)
    # root.right.right= newNode(70)
    # root.right.right.left=newNode(65)
    # root.right.right.right=newNode(80)
    print(distanceK(root,30,2))