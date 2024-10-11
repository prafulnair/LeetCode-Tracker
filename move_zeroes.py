class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.\
        """
        if 0 not in nums or len(nums) == 1:
            return nums
        
        p, q = 0, 0
        
        while(p<=len(nums)-1):

            if nums[p] != 0:
                nums[p], nums[q] = nums[q], nums[p]
                q += 1
                
            p += 1
                
        return nums
    

"""
So the concept is pretty neat and clever. You took some time to figure out ..you almost had 90% of it figured out
and last me you had to take gpts help
basically you maintain two pointers p and q, p iterating through the array while q marked all the zeroes
if your nums[p] is a nonzeroe number, swap it with nums[q](which is zero)
"""

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

 
Follow up: Could you minimize the total number of operations done?
    """