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
        self.top_item = None
        # Why is our DLL a good choice to store our elements?
        self.storage = 1000 #this is the limit

    def push(self, value):

        #if there is still space on the stack
        if self.len() < 1000:

            #instantiate a node with value as an argument and assign it to the variable item
            #because this item is a node, we have easy access to ListNode’s class methods
            new_item = ListNode(value)

            self.size += 1

            #if the stack is empty
            if not self.top_item:

                #set the new node as the top item
                self.top_item = new_item

            #if the stack is not empty
            else:
                #set the existing top item's prev pointer to new_item
                self.top_item.prev = new_item 

                #set the new_item's next pointer to the current top item
                new_item.next = self.top_item

                #set the new_item as the top item
                self.top_item = new_item 

        #if there is no space left on the stack
        else:
            print("All out of space!")
        
    def pop(self):

        #if the stack is not empty
        if self.size > 0:

            #always remove the first item from a stack first
            item_to_remove = self.top_item

            #this removes the self.top_item's next pointer (assigns it back to itself)
            self.top_item = item_to_remove.next

            #decrement the stack size
            self.size -= 1

            #return's the value of item_to_remove after the item is popped or removed
            return item_to_remove.value
        
        #if the stack is not empty
        else:
            print("The stack is totally empty.")


    def len(self):

        #returns the size of the stack
        return self.size
