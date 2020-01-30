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
        
        #if there is no root node
        if self.value is None:
            #assign the value to the root node
            self.value = value
        else:
            #if the root is greater than the value passed in
            if self.value > value:
                #the left subtree contains the values that are less than the node
                #if there is no left subtree
                if self.left is None:
                    #create a new left subtree and initialize it with value
                    self.left = BinarySearchTree(value)
                else:
                    #if there is a left subtree insert the value in the left subtree
                    self.left.insert(value)
            else:
                #if the root is less than the value passed in
                #the right subtree contains the values that are greater than the node
                #if there is no right subtree
                if self.right is None:
                    #create a new right subtree and initialize it with value
                    self.right = BinarySearchTree(value)
                else:
                    #if there is a right subtree insert the value in the right subtree
                    self.right.insert(value)
       

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        #if there is no root, then there is no tree, return false
        if self.value is None:
            return False

        #if the target is equal to the root, the value was found   
        if self.value == target:
            return True

        #if the target is greater than the root then it is in the right subtree(s)
        if target > self.value:
            #if there are no right subtrees, then the value is not in the tree
            if self.right is None:
                return False
            else:
                #if there is a right subtree, call contains on the right subtree(s)
                return self.right.contains(target)
        else:
            #if the target is less than the root then it is in the left subtree(s)
            #if there are no left subtrees, then the value is not in the tree
            if self.left is None:
                return False
            else:
                #if there is a left subtree, call contains on the left subtree(s)
                return self.left.contains(target)    
         

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


