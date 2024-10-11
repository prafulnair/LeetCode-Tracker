"""
MAKE ARRAY ZERO BY SUBTRACTING EQUAL AMOUNTS
You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

Example 1:

Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
Example 2:

Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

class Solution:

    def get_smallest_nonZero(nums):
        nonZelements = []
        for n in nums:
            if n != 0:
                nonZelements.append(n)
        
        minimum = min(nonZelements)
        if minimum > 0:
            return minimum-1
        return minimum

    def minimumOperations(self, nums: list[int]) -> int:
        maximum  = max(nums)
        operations = 0
        while(maximum != 0):
            operations+=1 
            #minimum = min(nums)
            minimum = Solution.get_smallest_nonZero(nums)
            next_min = minimum + 1
            print(f"next min is {next_min}")

            for i in range(0, len(nums)):
                if nums[i] > 0:
                    nums[i] = nums[i] - next_min

            print(nums)
            
            maximum = max(nums)
        
        return(operations)



nums = [1,5,0,3,5]

print(Solution.minimumOperations(Solution, nums))


"""
Another possible solution as follows
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        seen = set()
        seen.add(0)
        count = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                count += 1
        
        return count

    
"""