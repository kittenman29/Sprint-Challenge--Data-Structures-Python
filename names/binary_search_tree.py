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
          

# bst = BinarySearchTree(5)
# bst.insert(5)
# bst.insert(8)
# bst.insert(2)
# bst.insert(14)
# print(f"bst: {bst.value}")
# print(f"left: {bst.left.value}")
# print(f"right: {bst.right.value}")
# print(f"left contains: {bst.contains(8)}")