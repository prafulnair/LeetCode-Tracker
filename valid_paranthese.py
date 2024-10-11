"""20. Valid Parentheses
Solved
Easy
Topics
Companies
Hint

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

"""


class Solution:
    def isValid(self, s: str) -> bool:
        forward = ['(','{','[']
        backward = [')','}',']']

        if len(s) == 1:
            return False

        stack1 = []
        stack2 = []
        for char in s:
            if char in forward:
                stack1.append(char)
            else:
                if len(stack1) == 0:
                    return False
                if stack1[-1] == forward[backward.index(char)]:
                    stack1.pop()
                else:
                    return False
        return True if len(stack1)==0 else False
        
"""This code can be optimized further with clean and sharp coding
First thing that we can do is use a map instead of two lists. And secondly, handle ifs and else logic more elgantly 
Here is what chatGPT suggested. 


class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing parentheses to their corresponding opening ones
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping.values():  # If the character is an opening bracket
                stack.append(char)
            elif char in mapping:  # If the character is a closing bracket
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False  # Invalid character
        
        return not stack

# Example usage
s = Solution()
print(s.isValid("()[]{}"))  # Output: True
print(s.isValid("([)]"))    # Output: False
print(s.isValid("{[]}"))    # Output: True


"""
        


"""
previously submitted code
class Solution:
    def isValid(self, s: str) -> bool:
        forward = ['(','{','[']
        backward = [')','}',']']

        if len(s) == 1:
            return False

        stack1 = []
        stack2 = []
        for char in s:
            if char in forward:
                stack1.append(char)
            else:
                if len(stack1) == 0:
                    return False
                if stack1[-1] == forward[backward.index(char)]:
                    stack1.pop()
                else:
                    return False
        return True if len(stack1)==0 else False
        

        


        
"""