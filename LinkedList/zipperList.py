class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def zipp_lists(self, list1, list2):


        tail = list1
        current1 = list1.next
        current2 = list2 

        count = 0

        while(current1 and current2):

            if count % 2 == 0:
                tail.next = current2
                current2 = current2.next
                tail = tail.next
                
            else:
                tail.next = current1
                current1 = current1.next
                tail = tail.next

            count += 1

        if not current1:
            tail.next = current2
        if not current2:
            tail.next = current1
    


    