
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None # poinst @ first node in list
        self.tail = None # points @ last node in list

    # append / add --> add_to_tail
    def add_to_tail(self, value):
        pass

    #remove
    def remove_head(self):
        pass

    def remove_tail(self):
        pass