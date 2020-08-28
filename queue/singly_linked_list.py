
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, length=0):
        self.head = None
        self.tail = None
        self.length = length

    def add_to_tail(self, value):
        # Create the node
        newNode = Node(value, None)
        self.length += 1
        # Check to see if there is a tail value
        if self.head is None:
            # If no tail: Set value as Tail (Assumed empty list)
            self.head = newNode
            self.tail = newNode

        else:
            # access current tail node value
            oldTail = self.tail
            # Update current tail node's "Next Value" to new tail
            oldTail.next = newNode
            # Set new node to tail
            self.tail = newNode

    def remove_head(self):
        if self.head is None:
            return None
        else:
            self.length -= 1
            # Check to see if there is a list of one
            if self.head == self.tail:
                # Set both head and tail to none
                oldHead = self.head
                self.head = None
                self.tail = None
                return oldHead.value

            else:
                currentHead = self.head
                self.head = currentHead.next
                return currentHead.value

    def remove_tail(self):
        if self.head == None:
            return None

        elif self.head == self.tail:
            self.length -= 1
            oldTail = self.tail
            self.head = None
            self.tail = None
            return oldTail.value
        else:
            self.length -= 1
            current = self.head
            # I need to ID the Tail to know when to stop
            oldTail = self.tail
            # "NewTail is equal to the node.next with the current tails value"
            while current.next is not self.tail:
                current = current.next

            removedValue = self.tail.value
            self.tail = None
            self.tail = current

            return removedValue