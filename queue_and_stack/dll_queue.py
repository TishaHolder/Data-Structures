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
        self.head = None
        self.tail = None
        # Why is our DLL a good choice to store our elements?
        self.storage = 1000 #max_size property that bounded queues can utilize to limit the total node count

    #add items to the tail
    def enqueue(self, value):

        #if there is still space in the queue
        if self.len() < self.storage:

            #instantiate a node with value as an argument and assign it to the variable new_item
            #because this item is a node, we have easy access to ListNode’s class methods
            new_item = ListNode(value)

            #increment the size of the stack
            self.size += 1

            #if the stack is empty
            #items are added to the tail of a queue            
            if not self.head and not self.tail:

                #set the new node as the head and tail
                self.head = new_item
                self.tail = new_item               

            #if the queue is not empty
            else:
                #set the existing tails next pointer to new_item
                self.head.next = new_item 

                #set the new_item's prev pointer to the current tail
                new_item.prev = self.tail

                #set the new_item as the tail
                self.tail = new_item 

        #if there is no space left on the queue
        else:
            print("All out of space!")

    #remove items from the head
    def dequeue(self):
        
        #if the queue is not empty
        if self.len() > 0:

            #remove items from the head
            item_to_remove = self.head            

            #remove the next pointer of the existing head by assigning it back to itself
            self.head = item_to_remove.next         
            

            #decrement the size of the stack
            self.size -= 1

            #return's the value of item_to_remove after the item is removed
            return item_to_remove.value


        #if the queure is empty
        else:
            print("The queue is totally empty.")

    def len(self):
        #returns the size of the queue
        return self.size
