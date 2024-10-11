nums= [0,0,1,1,1,1,2,3,3]

# [0,0,1,1,2,2,3]
"""
0 0 1 1 2 3 3 3 3
              p i 
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # Start from the third element in the array
        pos = 2
        
        for i in range(2, len(nums)):
            # If the current element is not the same as the element two positions back
            if nums[i] != nums[pos - 2]:
                # Place it in the position and increment the position
                nums[pos] = nums[i]
                pos += 1
        
        # The length of the array with allowed duplicates
        return pos

# Example usage
s = Solution()
nums = [1,1,1,2,2,3]
"""
1 1 1 2 2 3
    2 i
"""
print(s.removeDuplicates(nums))  # Output should be 5
print(nums[:5])  # Output should be [1, 1, 2, 2, 3]


