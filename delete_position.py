#takes in pos as one of the input parameters.
def delete_node_at_pos(self, pos)
# if the linked list is an empty list or no
    if self.head:
        cur_node = self.head
        #If pos equals 0, it essentially means that we want to delete the head node.
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        #if we are deleting a node at a position other than the head node
        prev =  None
        count = 0 
        while cur_node and count != pos:
            prev = cur_node
            # The while loop will terminate if cur_node becomes None 
            # or count becomes equal to pos which will imply that cur_node will be the node that we want to delete.
            cur_node = cur_node.next
            cound += 1
        #is precisely the same as in the delete_node class method.    
        if cur_node is None:
            return
        prec.next =  cur_node.next
        cur_node = None