class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage)-1
    self._bubble_up(index)

  def delete(self):
    #Removes the [0] element, bubble up the max value
    if len(self.storage) == 0:
      return
    elif len(self.storage) == 1:
      return self.storage.pop(0)
    elif len(self.storage) > 1:
      old_max = self.storage[0]
      self.storage.pop(0)
      new_max = max(self.storage)
      max_index = self.storage.index(new_max)
      self._bubble_up(max_index)
      for i in range(len(self.storage)):
        self._sift_down(i)
      return old_max

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # keep bubbling up until we've either reached the top of the heap
    # or we've reached a point where the parent is higher prio
    while index > 0:
    # on a single bubble up iteration
    # get the parent index 
      parent = (index - 1) // 2
    # compare the child against the value of the parent
    # if the child's value is higher prio than its parent's value
      if self.storage[index] > self.storage[parent]:
      # swap them
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      # update the child's index to be the new index it is now at
        index = parent
    # otherwise, child is at a valid spot
      else:
      # stop bubbling up
        break

  def _sift_down(self, index):
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    # Test if both left_child and right_child exist: _sift_down if needed
    if left_child in range(len(self.storage)) and right_child in range(len(self.storage)):
      if self.storage[index] < self.storage[left_child] or self.storage[index] < self.storage[right_child]:
        if self.storage[left_child] > self.storage[right_child]:
          self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
        else:
          self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]

    # Test if left_child exists: _sift_down if needed
    elif left_child in range(len(self.storage)):
      if self.storage[index] < self.storage[left_child]:
        self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]

    # Test if right_child exists: _sift_down if needed
    elif right_child in range(len(self.storage)): 
      if self.storage[index] < self.storage[right_child]:
        self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
