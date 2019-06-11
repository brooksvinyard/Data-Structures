"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    self.length += 1
    if self.head:
      old_head = self.head
      new_head = ListNode(value, None, old_head)
      old_head.prev = new_head
      self.head = new_head
    else: # It was an empty list
      self.head = ListNode(value, None, None)
      self.tail = self.head

  def remove_from_head(self):
    old_head = self.head.value
    if self.head is self.tail: # The node was the only one in the list
      self.head = None
      self.tail = None
      self.length = 0
    elif self.head:
      self.length -= 1
      self.head = self.head.next
      if self.head.prev is not None:
        self.head.prev = None
    return old_head

  def add_to_tail(self, value):
    self.length += 1
    if self.tail:
      old_tail = self.tail
      new_tail = ListNode(value, old_tail, None)
      old_tail.next = new_tail
      self.tail = new_tail
    else: # It was an empty list
      new_tail = ListNode(value, None, None)
      self.tail = new_tail
      self.head = new_tail

  def remove_from_tail(self):
    old_tail = self.tail.value
    if self.tail is self.head: # It is a list on one
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.length -= 1
      old_tail = self.tail
      new_tail = old_tail.prev
      new_tail.next = None
    return old_tail

  def move_to_front(self, node):
    if node.prev:
      node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev
    old_head = self.head
    old_head.prev = node
    self.head = node
    node.prev = None
    node.next = old_head
    
  def move_to_end(self, node):
    old_tail = self.tail
    old_tail.next = node
    if node.prev:
      node.prev.next = node.next
    else: #node was head
      self.head = node.next
    
    if node.next:
      node.next.prev = node.prev

    self.tail = node
    node.next = None
    node.prev = old_tail

  def delete(self, node):
    if node is self.head: # Node was head
      self.remove_from_head()
    elif node is self.tail: # Node was tail
      self.remove_from_tail()
    else:
      self.length -= 1
      if node.prev:
        node.prev.next = node.next
      if node.next:
        node.next.prev = node.prev
    
  def get_max(self):
    if not self.head and not self.tail: #If empty list
      return False

    max_value = self.head.value
    current = self.head

    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.next
    return max_value
