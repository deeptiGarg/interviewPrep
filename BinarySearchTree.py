
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

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
    h = 0
    hLeft=0
    hRight=0
    if(root!= None):
        if(root.left!=None):
            hLeft = height(root.left) + 1
        if(root.right!=None):
            hRight = height(root.right) + 1
        if hLeft>=hRight:
            h = hLeft
        else:
            h = hRight
    return h


tree = BinarySearchTree()
arr = [3, 5, 2, 1, 4, 6, 7]

for i in range(len(arr)):
    tree.create(arr[i])

print(height(tree.root))