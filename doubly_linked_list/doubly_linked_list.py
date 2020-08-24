"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode
    inserts it as the NEW HEAD of the list
    Don't forget to handle the old head node's previous pointer accordingly

    >> Replaces the head of the list with a new value that is passed in.
    """
    def add_to_head(self, value):
        newNode = ListNode(value)
        # none
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return value
        # one
        else:
            oldHead = self.head
            oldHead.prev = newNode
            self.head = newNode
            newNode.next = oldHead
            self.length += 1
            return value 
        # if a bunch
        # if a fuck ton
        pass
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.

    >> removes the head node and returns the value stored in it
    """
    def remove_from_head(self):
        removed_head = self.head
        if self.length == 0:
            return None
        
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_head.value
        
        else:
            current_head = self.head
            current_head.head = None
            current_head.tail = None
            self.length -= 1
            return removed_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.

    >> replaces the tail of the list with a new value that is passed in.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return value

        else: 
            old_tail = self.tail
            old_tail.next = new_node
            self.tail = new_node
            self.length += 1
            return value

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.

    >> removes the tail node and returns the value stored in it.
    """
    def remove_from_tail(self):
        removedTail = self.tail

        if self.length == 0:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return removedTail.value

        else:
            new_tail = removedTail.prev
            new_tail.next = None
            removedTail.prev = None
            self.tail = new_tail
            self.length =- 1
            return new_tail.value


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.

    >> takes a reference to a node in the list and removes it from the list. 
    >> The deleted node's previous and next pointers should point to each afterwards
    """
    def delete(self, node):
        if self.length == None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return node.value

        elif node.next == None: # is this the TAIL?
            # Assign variable to new TAIL
            newtail = self.tail.prev
            # Assign new TAIL
            self.tail = newtail
            # Removes only pointer from the old TAIL
            node.prev = None
            # decrease length
            self.length -= 1
            return node.value

        elif node.prev == None: # is this the HEAD?
            # Assign variables to the NEW HEAD
            newHead = self.head.next
            # Assign NEW HEAD value
            self.head = newHead
            # Remove OLD HEADs points = gets removed
            node.next = None
            # Decrease length
            self.length -= 1
            return node.value

        else:
            # Assign variables to Next and Prev
            nextInList = node.next # = 6
            prevInList = node.prev # = 4
            # Assign them to each other
            nextInList.prev = prevInList
            prevInList.next = nextInList
            # Remove node
            node.next = None
            node.prev = None
            # Decrease length
            self.length -= 1

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.

    >> takes a reference to a node in the list and 
    >> moves it to the front of the list, shifting all other list nodes down

    """
    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.

    >> takes a reference to a node in the list and 
    >> moves it to the end of the list, shifting all other list nodes up
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Finds and returns the maximum value of all the nodes 
    in the List.

    > > returns the maximum value in the list
    """
    def get_max(self):
        currentNode = self.head # will hold the looping node
        maxValue = 0
        inc = 0

        if self.length == 0:
            return None
        elif self.tail == self.head:
            return self.head.value
        else:
            while inc is not self.length:
                if currentNode.value > maxValue:
                    maxValue = currentNode.value
                    currentNode = currentNode.next
                    inc += 1
                else: 
                    currentNode = currentNode.next
                    inc += 1

        return maxValue