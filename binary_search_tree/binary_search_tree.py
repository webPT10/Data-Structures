"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given VALUE into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value) # recursion ???

        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value) # recursion ???

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: # compare Target Value to node.Value
            return True
        #   OR
        # if self.value == target:
        #     return True
        if target > self.value: # OR if self.value < target:
            if self.right is None: # OR self.right == None ?
                return False

        #     elif self.right.value == target:
        #         return True
        #     else:
        #         self.right.contains(target)

        # else:
        #     if self.left.value == None:
        #         return False
        #     elif self.left == target:
        #         return True
        #     else:
        #         self.left.contains(target)
            
    # Return the maximum value found in the tree
    # start at the ROOT
    # keep going RIGHT until you can't anymore >> RETURN that Value
    # 
    def get_max(self):
        bigger_node = self.right.right
        # keep moving right until right is none
        while bigger_node.right is not None:
            bigger_node = bigger_node.right
        return bigger_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a Recursive, Depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an Iterative Breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an Iterative Depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
