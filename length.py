#iterative implementation
def len_iterative(self):
    #We keep a count of how many nodes by setting a count variable 
    # equal to zero at the beginning of the method on 
    count = 0
    # we start from the beginning of the linked list,
    #  we set cur_node equal to the head of the linked list
    cur_node = self.head
    #Then we go through each of the nodes until we hit None
    while cur_node:
        #as long as the cur_node is not None by incrementing itself 
        count += 1
        cur_node = cur_node.next
    return count