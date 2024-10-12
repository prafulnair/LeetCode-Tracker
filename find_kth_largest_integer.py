import heapq 

class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:

        nums = [-int(num) for num in nums]
        heapq.heapify(nums)

        count = 0 
        while (count < k-1):
            heapq.heappop(nums)
            count += 1
        
        return str(-heapq.heappop(nums))
    
