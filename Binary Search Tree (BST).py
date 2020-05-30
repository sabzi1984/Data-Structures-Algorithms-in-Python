class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        i=self.root
        self.insert_bst(i,new_val)

    def search(self, find_val):
        i=self.root
        return self.search_bst(i,find_val)
    def insert_bst(self,start,new_val):
        if new_val<start:
            if start.left:
                self.insert_bst(start.left,new_val)
            else:
                start.left=Node(new_val)
        if new_val>start:
            if start.right:
                self.insert_bst(start.right,new_val)
            else:
                start.right=Node(new_val)
        
    def search_bst(self, start, find_val):
        if start:
            if find_val==start.value:
                return True
            elif find_val<start:
                return self.search_bst(start.left,find_val)
            else:
                return self.search_bst(start.right,find_val)
        return False    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
