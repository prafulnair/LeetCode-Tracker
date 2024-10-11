class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        maxx = 0
        for i in range(0, len(nums)):
            
            left_n = nums[i] - 1
            if left_n not in seen:
                count =0
                right_n = nums[i] + 1
                while(right_n in seen):
                    count+=1
                    right_n+=1
                maxx = max(maxx,count)
            
        
        return maxx + 1
    
"""
128. Longest Consecutive Sequence
Solved
Medium
Topics
Companies

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109


"""

"""
EXPLANATION OF THE SOLUTION
This is a leetcode medium problem but if you think about it, its pretty straightforward

so first we create a set with all the numbers of list nums
then, we check which element is the start of a new sequence
    so a number is a start of a sequence, if that number - 1 is not in seen (the set we created)
    so if the longest common sequence is 1, 2, 3 and 4, you would see that 1's left neighbour 0 is not in the set seen

so then once we find that element, start a while loop, and see if that element + 1 is in the set or not, if yes, continue adding 1 to it and 
check how long the sequence goes. 
SIMPLE.
"""
