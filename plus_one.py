"""66. Plus One
Solved
Easy
Topics
Companies

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

 

Constraints:

    1 <= digits.length <= 100
    0 <= digits[i] <= 9"""



class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        # Start from the last digit
        p = len(digits) - 1
        carry = 1
        
        while p >= 0:
            summ = digits[p] + carry
            carry = summ // 10  # calculate carry
            digits[p] = summ % 10  # update digit with the remainder
            
            # if carry is zero, we don't need to propagate further
            if carry == 0:
                return digits
            
            p -= 1
        
        # if carry is still 1, we need to add a new digit at the beginning
        if carry == 1:
            return [1] + digits
        
        return digits
    
s = Solution()
digits = [1,2,3]
print(s.plusOne(digits))

