# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        

        dummy = ListNode(0)
        current = dummy

        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
            
        ## at this point one of the list has been exhausted
        ## we need to attached the remaining elements

        if head1 is not None:
            current.next = head1
        else:
            current.next = head2

        return dummy.next
    
    """
    The code wont run here due to the internal structure of leetcode supporting the execution of the program,
    but here is the simple breakdown of how you solved the problem. 
    You just needed a simple hint. creating that dummy node. You created a dummy node with val 0 with next pointing to null
    then you basically appointed two pointers to the start of each list, head1 and head2, and then compared each element, deciding 
    which should be the next element to the dummy. So to make sure we retain the head, we added another pointer named current, that
    would do the work of moving through. 

    once either one list is exhausted, we have to just add the remaining list to the current node, which has moved through the end
    """
        
"""
Another attempt
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Base Case
        if not list1:
            return list2
        elif not list2:
            return list1
        
        # Creating a dummy Node.
        # The idea is, depending on which node has lesser value, curr's next would be that node. 
        # Then curr would be that node while that node (p or q) moves on to their respective next node
        # Always p and q node values are being compared
        
        dummy = ListNode()
        curr = dummy 
        p = list1
        q = list2
        
        while(p and q):
                
            if p.val <= q.val:
                curr.next = p
                curr = p
                p = p.next
            else:
                curr.next = q
                curr = q
                q = q.next
                
        # To make sure that if p ends soon and there is still q's nodes, attach all curr's node to q
        # This works for us as curr would always point to the node of that list that has been exhausted 
        if not p:
            curr.next = q
        else:
            curr.next = p
            
        return dummy.next


