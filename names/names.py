import time
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        # recursive to keep going until we find an empty spot
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        # recursive to keep going until we find an empty spot
        self.right.insert(value)

  def contains(self, target):
    # if the target matches the root, return true
    if target == self.value:
      return True
    # if the target is less than the root
    elif target < self.value:
      # if there is a subtree node to the left, recursive search
      if self.left:
        return self.left.contains(target)
      else:
        return False
    elif target > self.value:
      if self.right:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    # if nothing to the right of root, return self.value as max
    if not self.right:
      return self.value
    # else keep going to the right of the root until 
    else:
      return self.right.get_max()


  def for_each(self, cb):
    if self.value:
      cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

bst2 = BinarySearchTree(names_2[0])
for x in names_2:
    bst2.insert(x)
# print(bst2)

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
duplicates = []
for name_1 in names_1:
    if bst2.contains(name_1):
        duplicates.append(name_1)
        

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

