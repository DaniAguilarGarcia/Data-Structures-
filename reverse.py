# previous and current node strategy in the Node swap lesson.
def reverse_iterative(self):
    prev = None
    cur = self.head
    # will run until cur is not equal to None
    while cur:
        #which help us to iterate through the linked list while keeping track of 
        # the previous and current nodes
        #nxt is used as a temporary variable to store the value of cur.next
        nxt = cur.next
        #flipping of the arrows
        #we point the next of the current node to the previous node
        cur.next = prev
        prev = cur
        cur = nxt
        #equal to the last node in the linked list.
    self.head = prev