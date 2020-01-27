import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode, DoublyLinkedList

"""
Stacks provide three methods for interaction:
•	Push - adds data to the “top” of the stack
•	Pop - returns and removes data from the “top” of the stack
•	Peek - returns data from the “top” of the stack without removing it

It is a First In, Last Out, or FILO structure
"""

class Stack:
    def __init__(self):
        self.size = 0
        
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):        

        self.storage.add_to_head(value)

        #increment the size of the stack
        self.size += 1   
        
        
    def pop(self):

        #if the stack is not empty
        if self.len() > 0:

            value = self.storage.remove_from_head()

            #decrement the stack size
            self.size -= 1

            #return's the value of item_to_remove after the item is popped or removed
            return value
        
        #if the stack is not empty
        else:
            print("The stack is totally empty.")

    def len(self):

        #returns the size of the stack
        return self.size
