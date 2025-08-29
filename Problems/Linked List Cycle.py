class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def hasCycle(head):
  visited_nodes = set()

  current_node = head
  while current_node is not None:
    if current_node in visited_nodes:
      return True  # Cycle detected

    visited_nodes.add(current_node)
    current_node = current_node.next

  return False
