
#define a note class 
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 
    
""" In a binary search tree, all nodes on the left branch of a node are less than the node value. All values on the right branch are greater than the node value. """
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break 
       
def height(root):
    addLeft = 0
    addRight = 0
    if root.right:
        addRight = 1 + height(root.right) # count of right nodes
    if root.left:
        addLeft = 1 + height(root.left) # count of left nodes
    
    return addLeft if (addLeft > addRight) else addRight



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
