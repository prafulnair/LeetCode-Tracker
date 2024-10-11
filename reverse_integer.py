class Solution:
    def reverse(self, x: int) -> int:
        # Constants for the 32-bit integer limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Handle negative sign
        negative = x < 0
        if negative:
            x = -x
        
        # Reverse the number
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        # Apply the negative sign if necessary
        if negative:
            reversed_num = -reversed_num
        
        # Check for overflow after applying sign
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        
        return reversed_num
    

"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

 

Constraints:

    -231 <= x <= 231 - 1


"""