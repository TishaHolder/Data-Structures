import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value #current node
        self.left = None #left subtree
        self.right = None #right subtree      
        self.stack = Stack()
        self.queue = Queue()

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
                    #each node is a new subtree
                    self.left = BinarySearchTree(value)
                else:
                    #if there is a left subtree insert the value in the left subtree (recurse)
                    self.left.insert(value)
            else:
                #if the root is less than the value passed in
                #the right subtree contains the values that are greater than the node
                #if there is no right subtree
                if self.right is None:
                    #create a new right subtree and initialize it with value
                    self.right = BinarySearchTree(value)
                else:
                    #if there is a right subtree insert the value in the right subtree (recurse)
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

        ###RECURSIVE SOLUTION###
        #if there is nothing to the right of this node then this node must be the max node
        """if not self.right:
            return self.value
        else
            return self.right.get_max()

        #using while loop
        max = self.value"""

        ###USING A WHILE LOOP###
        #set the root as the max value
        max = self.value

        #create a reference to the current node and update it as we traverse the tree
        current = self

        while current:
            if current.value > max:
                max = current.value
           
            current = current.right

        return max


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        #if no root
        if self.value is None:
            return

        #call cb on root
        cb(self.value)

        #if there is a right subtree
        if self.right:
            #call cb on each right subtree
            self.right.for_each(cb)

        #if there is a left subtree
        if self.left:
            #call cb on each left subtree
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):  
        if node is None:
            return    

        if node:
            print(node.value)  

        if node.left:
            return self.in_order_print(node.left)        

        if node.right:
            return self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        if node is None:
            return  
        else:
            self.stack.push(node.value)  

        if node.right is None:
            return
        else:
            self.stack.push(node.right.value)

        if node.left is None:
            return
        else:
            self.stack.push(node.left.value)

        
        for item in self.stack:
            print(item)




    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


