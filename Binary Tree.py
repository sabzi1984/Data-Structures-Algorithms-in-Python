class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        i=self.root
        return self.preorder_search(i,find_val)
            
       
    def print_tree(self):
        i=self.root
        traversal=""
        return self.preorder_print(i, traversal)[:-1]
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        

    def preorder_search(self, start, find_val):
        if start:
            if start.value==find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        """Helper method - use this to create a 
        recursive search solution."""    
        return False
    def preorder_print(self, start, traversal):
        if start:
            traversal+=(str(start.value)+"-")
            traversal=self.preorder_print(start.left, traversal)
            traversal=self.preorder_print(start.right, traversal)
            
        """Helper method - use this to create a 
        recursive print solution."""
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print (tree.print_tree())
