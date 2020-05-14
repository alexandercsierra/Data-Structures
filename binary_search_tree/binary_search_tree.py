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

from bq import Queue

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = BinarySearchTree(value)
        if self.value == None:
            self.value = value
        elif self.value > value:
            if self.left == None:
                self.left = node
            else:
                self.left.insert(value)
        elif self.value < value or self.value == value:
            if self.right == None:
                self.right = node
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.left != None:
            if self.value > target:
                if self.left == target:
                    return True
                else:
                    return self.left.contains(target)
        if self.right != None:
            if self.value < target:
                if self.right == target:
                    return True
                else:
                    return self.right.contains(target)
        else:
            return False
            

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value != None:
            max = self.value
            if self.right != None:
                max = self.right.value
                return self.right.get_max()
            return max
        else: 
            return None

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
            if self.left != None:
                self.left.for_each(fn)
            fn(self.value)
            if self.right != None:
                self.right.for_each(fn)
            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node.for_each(print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while len(q) > 0:
            curr = q.dequeue()
            if curr.right != None:
                q.enqueue(curr.right)
            if curr.left != None: 
                q.enqueue(curr.left)
            print(curr.value)
            
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)
        while len(stack) > 0:
            curr = stack.pop()
            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)
            print(curr.value)

        #start with root node, add to stack
        #does it have a left node? add to stack
            #repeat until no more left nodes
            #no more left nodes? check right 
                #if right, add to stack


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            node.left.pre_order_dft(node.left)
        if node.right is not None:
            node.right.pre_order_dft(node.right)
            

                


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left is not None:
            node.left.post_order_dft(node.left)
        if node.right is not None:
            node.right.post_order_dft(node.right)
        print(node.value)

