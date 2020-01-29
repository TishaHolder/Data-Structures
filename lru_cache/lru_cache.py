"""LRU Caches discard the least recently used item in the cache when it is full"""
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    """when we have a cache we want to be able to look something up by a certain key. we can use a key 
       to look in the cache and see if the data corresponding to that key is in there"""

    """when adding items to the cache/dictionary by key we also have to add it to the linked list at the head
       to indicate it is the most recently used (MRU) item"""

    """to get items from the cache we look up in the dictionary by key to see if the item is there.
       if it is there we need to mark the item as most recently used (MRU) by moving it to the 
       head of the list"""

    """if the cache is over full or at max capacity, look at the least recently used (LRU) item 
       at the end of the list (tail) and delete it from both the list and the dictionary"""

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0

        #used to store or order the data in memory and organize the data in a 
        # most recently used/least recently used way
        self.list = DoublyLinkedList()

        #dictionary used as cache to store key value pairs and point to every element in the DoublyLinkedList
        #if we want a pointer to Node C, use dictionary to look up by the key of C and it will return 
        #a pointer to C
        self.storage = dict()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
                
            if key in self.storage:

                #Retrieves the value/node associated with the given key.                
                node = self.storage[key]

                #Also needs to move the key-value pair to the end/front of the order such that the pair is 
                # considered most-recently used.
                self.list.move_to_front(node)                

                #Returns the value associated with the key
                #nodes are stored as a tuple with a key, value pair
                #to access value use [1]
                return node.value[1]
            else:
                #returns none if the key/value pair doesn't exist
                return None



    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):    
        
        #check if key already exists in the dictioary
        # if it does, overwrite the old value (node) associated with the key with the new value
        if key in self.storage:

            #get the value associated with the existing key
            old_node = self.storage[key]         
        
            #then assign the new key/value pair as a tuple to to the old node's value
            #nodes are stored as a tuple with a key, value pair
            old_node.value = (key, value)

            #and add it to the doubly linked list as the first item (MRU)
            self.list.move_to_front(old_node)  
                     

        #if the cache is at max capacity, delete the oldest entry in the cache to make room        
        elif self.size == self.limit:      

            #remove it from the cache or dictionary
            #this syntax [self.list.tail.value[0]] accesses the key from the key/value pair tuple
            del self.storage[self.list.tail.value[0]]

            #remove it from the doubly linked list
            self.list.remove_from_tail()

            self.size -= 1

            #add the key/value pair as a tuple to the node's value             
            self.list.add_to_head((key, value))

            #update the the dictionary with the new node (key,value tuple becomes the node)
            self.storage[key] = self.list.head

        else:
            #add the key/value pair as a tuple to the node's value  
            self.list.add_to_head((key, value))

            #update the the dictionary with the new node (key,value tuple becomes the node)
            self.storage[key] = self.list.head

            self.size += 1




            


