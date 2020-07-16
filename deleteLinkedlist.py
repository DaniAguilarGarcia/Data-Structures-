#deleting the head node
# key as an input parameter
def delete_node(self, key):
    # starting point to traverse the linked lis
    cur_node =  self.head
    if cur_node and cur_node.data == key:
        self.head = cur_node.next
        cur_node = None
        return
    #we have a while loop which will run until cur_node becomes None
    #This implies that key doesn’t exist in our linked list
    prev = None
    while cur_node  and cur_node.data != key:
        #keep track of the previous node while cur_node is updated to the next node in the next line
        prev = cur_node
        cur_node = cur_node.next
#whether or not it’s because of cur_node being None, which will imply that key did not match any of the data of the current node
#if true then there is no node to delete.  
    if cur_node is None:
        return
#if cur_node is not None and its data matches with the key, we proceed to
#As we kept track of the previous node of the node to be deleted
    prev.next = cur_node.next
    cur_node =  None