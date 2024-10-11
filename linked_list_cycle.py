# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # BaseCase 0: There is no Node
        if not head:
            return False
        
        # BaseCase 1: There is only One node
        if head.next == None:
            return False
        
        slow, fast = head, head
        
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            
        return False
        
"""
Question - we have to find if the linkedlist have cycle in it.

Intuition: basically ,we start with 2 pointers, fast and slow (just like we did for palindrome linked list)
Fast is progressed as fast.next.next (skipping one node) and slow is progressed as slow.next. Both fast and slow initialized as head
if ever, slow == fast, it means that there is cycle. In a linkedlist without cycle, fast will always be ahead (and different) than slow and will terminate when fast.next is None
But if there is cycle, fast will come behind slow and after a point slow and fast will land at same node. That indicates a cycle. 
"""