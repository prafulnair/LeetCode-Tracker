# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
The following is the naive approach where I convert the linkedList to a string and then basically check if the string is palindrome or not
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        result = ""
        
        curr = head
        
        while(curr):
            result += str(curr.val)
            curr = curr.next
            
        p, q = 0, len(result) - 1
        
        while(p < q):
            if result[p] == result[q]:
                p += 1
                q -= 1
            else:
                return False
        
        return True
    
"""
But the time complexity of this solution, while is OK, is O(n) and space complexity O(n). Can we do this in space complexity of O(1)? Yes
The idea is to get to the mid point of the linkedlist, and then reverse it. 
Then we can easily compare
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        # Finding the middle node. Slow will be in the middle when fast.next is None
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            
        # Now reversing the linkedList. 
        prev = None
        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        
        # Checking for palindrom now. Just start comparing from the head and slow. Go until right
        left, right = head, prev
        
        while(right):
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
            
        return True
