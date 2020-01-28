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
    def __init__(self, limit=10):
        self.limit = limit
        self.size = None
        self.list = DoublyLinkedList()
        self.storage = {}


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        for i in self.storage:
            if key in key.storage:

                #if the key is found store the associated value in the value variable                
                value = self.storage[key]

                #this removes the key/value pair specified by the key from the dict. it returns the removed value
                self.storage.pop(key)

                #use the set method below to move the pair to the end of the order so it's MRU
                self.set(key, value)

                #rerturns the value associated with the given key
                return self.storage[key]
            else:
                #returns none of the key/value pair doesn't exist
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
        pass
