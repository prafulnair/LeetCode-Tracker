
"""
55. Jump Game
Attempted
Medium
Topics
Companies

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105


"""
"""
the following is an initial attempt. I used dynamic programming but it only passed the first 
few test cases. WE have to use a GReedy Approach in solving this. 
"""

def canJump(nums: list[int], currIndex, targetIndex, memo = None) -> bool:
    if memo == None:
        memo = {}
    if currIndex in memo:
        return memo[currIndex]
    if not nums:
        return True
    if currIndex == targetIndex:
        memo[currIndex] = True
        return True
    if currIndex > targetIndex:
        return
    
    jump_val = nums[currIndex]
    while(jump_val!=0):
        if canJump(nums[jump_val:],currIndex, targetIndex, memo) == True:
            return True
        jump_val-=1

    return False
        


"""
This the greedy approach. 
Basically, we start backwards. our goal is index 4 for the example [2,3,1,1,4]
so we start at 4 and say is the jump value here more than enough to reach to my goal.
At index 4, we have jump value of 4. Of course we can reach our goal because are at thge goal
so we shift goal to i, which is 4.
now we go to the next index, that is index 3. the jump val here is 1. Is index 3 + jumpval 1 >= 4? 
Yes. So now new goal is 3. 

So we continue like this. 
if our goal value is at 0, we suceeded, else return False. 
"""
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):

            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False


nums = [2,3,1,1,4]
print(canJump(nums,0,len(nums)-1))

