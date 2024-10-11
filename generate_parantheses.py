"""
22. Generate Parentheses
Medium
Topics
Companies

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8

"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        open = 0
        close = 0

        stack = []
        result = []

        def backtrack(open, close):
            if open == close == n:
                ele = "".join(stack)
                result.append(ele)
                return
            if open < n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()

        backtrack(open,close)
        return result
    

print(Solution.generateParenthesis(Solution, 3))
