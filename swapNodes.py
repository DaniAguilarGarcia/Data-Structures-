def swap_nodes(self, key_1, key_2):

    if key_1 == key_2:
        return
    #First of all, we check if key_1 and key_2 are the same element, if they are return to line 3
    # we declare prev_1 and curr_1 to None and self.head respectively
    prev_1 = None
    curr_1= self.head
    #runs while curr_1 is not at the end of the linked list or it is not equal to the key_1 that we seek.
    while curr_1 and curr_1.data != key_1:
        #we keep updating the prev_1 node equal to the curr_1 
        #and the curr_1 to the next node in the linked list.
        prev_1 = curr_1
        curr_1 = curr_1.next
    #In the same way, we try to find if key_2 exists in the linked list or not
    prev_2 = None
    curr_2= self.head
    while curr_2 and curr_2.data != key_2:
        prev_2 = curr_2
        curr_2 = curr_2.next
    #we check to make sure that the elements we found do exist
    # If both of the current nodes have a previous node, it implies that neither is a head nod
    if not curr_1 or not curr_2:
        return
    #If it exists, we set the next of prev_1 to curr_2 to swap it
    if prev_1:
    #prev1.next was pointing to curr_1 but now, we set it to point to curr_2. 
        prev_1.next = curr_2
    else:
    #On the other hand, if prev1 does not exist, it implies that curr_1 is the head node and we set self.head to its new value
        self.head = curr_2
        
    if prev_2:
        prev_2.next = curr_1
    else:
        self.head = curr_1
    curr_1.next, curr_2.next, = curr_2.next, curr_1.next
    