import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
         # compare the value to the root's value to determine which direction 
         # we're gonna go in
         # if the value < root's value
            if value < self.value:
             # go left
             # how do we go left
             # we have to check if there is another node on the left side
                if self.left:
                    # then self.left is a Node
                    # now what?
                    self.left.insert(value)
                else:
                    #then we can park the value here
                    self.left = BSTNode(value)
        # else the value >= root's value
            else:
            # go right
            # how do we go right?
            # we have to check if there is another node on the right side
                if self.right:
                    # then self.right is a Node
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when search start, self becomes root
        # compare target against self
        # return false when there's nothing in left or right direction
        if target == self.value:
            return True
        if target < self.value:
        # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
        # go right if right is a BSTNode
            if not self.right:
                return False
            return  self.right.contains(target)
        
# Replace the nested for loops below with your improvements

tree = BSTNode(names_1[0])

for i in range(1, len(names_1)):
   tree.insert(names_1[i])
    
for j in names_2:
    if tree.contains(j):
        duplicates.append(j)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
