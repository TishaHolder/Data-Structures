import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode, DoublyLinkedList

"""
We can add items to the tail of our queue using the enqueue method, 
but we remove them from the head using a method known as dequeue(),
"""

class Queue:
    def __init__(self):
        self.size = 0
        
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    #add items to the tail
    def enqueue(self, value):       

        self.storage.add_to_tail(value)

        #increment the size of the stack
        self.size += 1  
       

    #remove items from the head
    def dequeue(self):
        
        #if the queue is not empty
        if self.len() > 0:

            value = self.storage.remove_from_head()

            #decrement the size of the stack
            self.size -= 1

            #return's the value of item_to_remove after the item is removed
            return value


        #if the queure is empty
        else:
            print("The queue is totally empty.")

    def len(self):
        #returns the size of the queue
        return self.size
