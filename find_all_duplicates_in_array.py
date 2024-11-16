"""
Keep in mind that the constraint is writing of O(n) solution with only constant aux space, excluding the space to store result 
"""
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []
        
        # Iterate through each number in nums
        for num in nums:
            # Calculate the index to mark
            index = abs(num) - 1
            
            # If the number at this index is negative, it’s a duplicate
            if nums[index] < 0:
                result.append(abs(num))
            else:
                # Otherwise, mark this index by making the element negative
                nums[index] = -nums[index]
        
        return result