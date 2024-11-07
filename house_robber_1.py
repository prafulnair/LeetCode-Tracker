class Solution:
    def rob(self, nums: List[int]) -> int:
        
        max1, max2 = 0, 0

        temp = 0

        for n in nums:
            temp = max(n+max1, max2)
            max1 = max2
            max2 = temp

        return max2