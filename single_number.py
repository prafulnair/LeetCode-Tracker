"""
An optimal solution would use a linear time complexity approach. 
A common and efficient approach is to use bitwise XOR. 
The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, and it is both commutative and associative. 
This means that all numbers that appear twice will cancel each other out, leaving the single number.
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


