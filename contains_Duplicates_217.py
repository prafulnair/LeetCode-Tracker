"""
Leetcode 217 - Contians Duplicate (EASY)
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

1 <= nums.length <= 10^5
-109 <= nums[i] <= 10^9
"""
def containsDuplicate(nums: list[int]) -> bool:

    map = {}

    for i in nums:
        if i in map:
            map[i]+=1
        else:
            map[i] = 1

    for key, val in map.items():
        if val>=2:
            return True

    return False


nums = [1, 2, 3, 4]
print(containsDuplicate(nums))



"""
Another solution that I thought on my own (I am pretty proud of myself now, i came to this problem after some days)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        return True if len(nums)!= len(set(nums)) else False
