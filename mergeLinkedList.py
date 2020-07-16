class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
llist = LinkedList()
def merge_sorted(self,list):

    p = self.head
    q = llist.head
    s = None
    #checks if any of the lists are empty
    if not p:
        return q
    if not q:
        return p
    if p and q:
        # if p is less than or equal to q, then s will point to p
        if p.data <= q.data:
            s = p
            p = s.next
        #On the other hand, if q.data is less than p.data, s will point to q
        else:
            s = q
            q = s.next
        # will be the first node of our merged linked list
        # the node with the lesser value of p and q will be the first node of our merged linked list
        new_head = s 
      #until either p or q becomes None
    while p and q:
        #then we want to point s to what p is pointing to and move p along its respective linked list
        if p.data <= q.data:
            # #we update the value of s to p because p.data is less than or equal to q.data
            s.next = p
            s = p
            #Now we make p move along by pointing it to the next node of s
            p = s.next
    
        else:
            s.next = q
            s = q
            q = s.next
     # after the while loop terminates which implies either p or q or both p and q have become None       
    if not p:
        s.next = q
    if not q:
        s.next = p
    #the head node of our merged linked list made from llist and the linked list 
    # on which this class method is called.
    return new_head
llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()