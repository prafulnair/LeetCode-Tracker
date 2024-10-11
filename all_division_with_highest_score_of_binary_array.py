"""
This solution calculates the highest possible score at different indices where a division 
can be made in a binary array. 

1. **Left and Right Scores**: 
   - The `left_score` tracks the cumulative count of zeroes from the beginning up to each index.
   - The `right_score` tracks the cumulative count of ones from the end to each index.
   - We use two loops: one to build the `left_score` and another to build the `right_score`.
     We append the cumulative scores at each step.

2. **Final Score Calculation**:
   - After calculating the left and right scores, we iterate through each potential division index.
   - For each index `i`, the `stage_score` is calculated as the sum of `left_score[i]` and 
        `right_score[i]`.
   - If the `stage_score` is higher than the current `highest_score`, we update `highest_score` 
        and reset the `distinct_indices` list to only contain the current index.
   - If the score equals the `highest_score`, we append the current index to `distinct_indices`.

3. **Efficiency Consideration**: 
   - This approach effectively uses two-pass traversal and achieves the goal with O(n) time 
        complexity and O(n) space, which is optimal given the problem constraints.
   
4. **Resetting Distinct Indices**:
   - A key step in the solution is resetting `distinct_indices` whenever a new highest score is found, 
        ensuring only the indices with the maximum score are kept.

This method avoids extra complexity and solves the problem cleanly with concise logic.
"""
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        distinct_indices = []

        left_score = []
        right_score= []
        
        left_score.append(0)
        right_score.append(0)
        zeroes = 0
        ones = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zeroes += 1
                left_score.append(zeroes)
            else:
                left_score.append(zeroes)
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 1:
                ones += 1
                right_score.append(ones)
            else:
                right_score.append(ones)

        right_score = right_score[::-1]
        highest_score = 0
        
        for i in range(len(nums) + 1):
            stage_score = left_score[i] + right_score[i]
            if stage_score > highest_score:
                highest_score = stage_score
                distinct_indices = [i]  # Reset the list with the new highest score index
            elif stage_score == highest_score:
                distinct_indices.append(i)  # Append if score is the same as the highest score
        
        return distinct_indices
    
"""
Problem: All Divisions With the Highest Score of a Binary Array

You are given a binary array `nums` (containing only 0's and 1's). 
You are asked to divide the array into two parts at every possible division point and calculate a 
score for each division. 

The score is defined as the number of 0's on the left side of the division plus the number 
of 1's on the right side.

Your task is to return all the indices at which the score is the highest. 
If multiple indices have the same highest score, return all of them in increasing order.

The division indices can range from 0 to `len(nums)`, where:
- Dividing at index `i = 0` means all elements are on the right side (i.e., no elements on the left).
- Dividing at index `i = len(nums)` means all elements are on the left side (i.e., no elements on 
the right).

Example 1:
Input: nums = [0, 0, 1, 0]
Output: [3]

Explanation: 
- Dividing at index 3 gives the highest score of 4 (three 0's on the left and one 1 on the right).

Example 2:
Input: nums = [0, 1, 1, 0, 1]
Output: [2, 4]

Constraints:
- The length of nums is between 1 and 100,000.
- The array contains only 0's and 1's.

The challenge is to calculate the scores efficiently in one pass, using a combination of cumulative counts for the 0's on the 
left and 1's on the right. You then find the maximum score and return the indices where this score occurs.
"""
