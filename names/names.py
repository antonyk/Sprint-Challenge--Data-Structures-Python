import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        else:
            if self.right:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def get(self, value):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn, method='order', left=True):
        # iterate over the elements of a sorted binary tree
        if method == 'order':
            if self.left:
                self.left.for_each(fn, method)
            fn(self.value)
            if self.right:
                self.right.for_each(fn, method)

        elif method == 'pre-order':
            fn(self.value)
            if self.left:
                self.left.for_each(fn, method)
            if self.right:
                self.right.for_each(fn, method)

        elif method == 'post-order':
            if self.left:
                self.left.for_each(fn, method)
            if self.right:
                self.right.for_each(fn, method)
            fn(self.value)

        elif method == 'iter-dft':
            pending_stack = []
            pending_stack.append(self)
            while len(pending_stack) > 0:
                node = pending_stack.pop()
                if node.left:
                    pending_stack.append(node.left)
                if node.right:
                    pending_stack.append(node.right)
                fn(node.value)

        elif method == 'iter-bft':
            pending_queue = []
            pending_queue.append(self)
            while len(pending_queue) > 0:
                node = pending_queue.pop(0)
                if node.left:
                    pending_queue.append(node.left)
                if node.right:
                    pending_queue.append(node.right)
                fn(node.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if node == None:
            node = self
        node.for_each(print, 'order')

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        if node == None:
            node = self
        node.for_each(print, 'iter-bft')

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        if node == None:
            node = self
        node.for_each(print, "iter-dft")

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # if node == None:
        #     node = self
        node.for_each(print, "pre-order")

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node == None:
            node = self
        node.for_each(print, "post-order")



start_time = time.time()
names_1 = []
names_2 = []
bst1 = BSTNode('')
with open('names_1.txt', 'r') as f:
    names_1 = f.read().split("\n")  # List containing 10000 names
    for item in names_1:
        bst1.insert(item)

with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names

duplicates = []  # Return the list of duplicates in this data structure


# Replace the nested for loops below with your improvements
for name in names_2:
    if bst1.contains(name):
        duplicates.append(name)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


