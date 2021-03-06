class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    if self.value:
      cb(self.value)
    if self.left:
      self.left.depth_first_for_each(cb)
    if self.right:
      self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    q = []
    # add start node to queue
    q.append(self)
    # while queue, explore node at front and remove
    while len(q) > 0:
      current = q.pop(0)
    #check level below, if left add to queue
      if current.left:
        q.append( current.left )
      if current.right:  
        q.append(current.right)
      cb(current.value)  
    # this_level = [self]
    # while this_level:
    #   next_level = list()
    #   for item in this_level:
    #     cb(item.value)
    #     if item.left: 
    #       next_level.append(item.left)
    #     if item.right:
    #       next_level.append(item.right)
    #   this_level = next_level    
    # pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
