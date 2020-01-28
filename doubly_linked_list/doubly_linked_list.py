"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #instantiate a Node that takes value as its argument and assign it to a new variable new_node
        new_node = ListNode(value, None, None)

        #increment the size of the list
        self.length += 1

        #if the list is empty
        #set new_node as both the head and the tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        #if the list is not empty
        else:
            #set the new node's next pointer to self.head (points to existing head)        
            new_node.next = self.head

            #set the existing head's prev pointer to the new_node
            self.head.prev = new_node

            #set the new_node as the new head
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #assign self.head.value to value so it can be returned when the method ends
        value = self.head.value

        #use's the DoublyLinkedList's delete method
        self.delete(self.head)

        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        #instantiate a Node that takes value as its argument and assign it to a new variable new_node
        new_node = ListNode(value, None, None)

        #increment the size of the list
        self.length += 1

        #if the list is empty
        #make the new_node the head and the tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        #if the list is not empty   
        else:
            #we are putting the new node prev's pointer to self.tail (the existing tail)     
            new_node.prev = self.tail

            #put the existing tail's next pointer to the new_node
            self.tail.next = new_node

            #assign the new_node as the new tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #assign self.head.value to value so it can be returned when the method ends
        value = node.value

        #use's the DoublyLinkedList's delete method
        self.delete(node)

        #add it as the head node uing DoublyLinkedList's add_to_head method
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        #store the value of the node to be moved
        value = node.value

        #use's the DoublyLinkedList's delete method
        self.delete(node)

        #add it as the tail node using DoublyLinkedList's add_to_tail method
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):

        #decrement the size of the list
        self.length -= 1

        #if the list is empty, do nothing
        if not self.head and not self.tail:
            # TODO: Error handling
            return

        #if there is only one item in the list
        #set the pointes to null and garbage collection will handle the rest for us    
        # If head and tail
        if self.head == self.tail:
            self.head = None
            self.tail = None

        #if there is a head and head is the node to be deleted
        elif self.head == node:

            #this removes the head's next pointer before the head is deleted (assigns it to itself)
            self.head = self.head.next

            #delete the node using the delete mentod in the ListNode class
            node.delete()

        #if there is a tail and the tail is the node to be deleted
        elif self.tail == node:

            #this removes the tail's prev's pointer before the tail is deleted (assigns it to itself)
            self.tail = self.tail.prev
            node.delete()

        #if none of the other cases match, delete the node
        else:
            node.delete()
            
    """Returns the highest value currently in the list"""
    def get_max(self):

        #if there is no head or if the list is empty, return None
        if self.head is None:
            return None

        #else set the head as the initial max value
        max_value = self.head.value

        #assign the head to current
        current = self.head

        #iterate through the list to find the max_value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next #move on to the next item
        return max_value