import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None       

    # Insert the given value into the tree
    def insert(self, value):        

        root = BinarySearchTree(value)

        if self.value is None:
            root = value
        else:
            if value > root.value:
                if root.right is None:
                    root.right = value
                else:
                    insert(root.right.value)
            else:
                if root.left is None:
                    root.left = value
                else:
                    insert(root.left.value)
       

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if self.value is None:
            return False
        if self.value == target:
            return True
        if target > self.value:
                if self.right is None:
                    return False
                else:
                    contains(self.right.value)
        else:
            if self.left is None:
                return False
            else:
                contains(self.left.value)   
    
        
       

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


