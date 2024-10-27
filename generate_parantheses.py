class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of valid parentheses for a given 'n'.
        
        Parameters:
        - n (int): Number of pairs of parentheses.
        
        Returns:
        - List[str]: A list containing all valid combinations of 'n' pairs of parentheses.
        
        Approach:
        - This problem can be visualized as building combinations step-by-step.
        - We use a recursive approach (backtracking) to construct each combination by making
          choices about whether to add an opening '(' or a closing ')' at each step.
        - The constraints we use:
            - We can only add an opening '(' if we haven't yet reached 'n' total open brackets.
            - We can only add a closing ')' if there are unclosed opening brackets in the combination.
        - This approach ensures that every generated string is valid, as each closing bracket
          is paired with an opening one.
        """

        # Edge case: If n is 1, the only valid result is a single pair of parentheses.
        if n == 1: 
            return ["()"]

        # Stack is used here to build up each combination of parentheses.
        # We'll reset this stack as we explore each recursive branch.
        stack = [] # Holds the current parentheses combination being constructed
        result = [] # Will store all valid combinations once found

        # Recursive function for backtracking through possible parentheses combinations
        def backtrack(openn, close):
            """
            A recursive helper function to build all valid parentheses combinations.
            
            Parameters:
            - openn (int): The count of '(' used so far.
            - close (int): The count of ')' used so far.
            
            - Base Case: If both `openn` and `close` reach `n`, it means we have used up all
              parentheses and built a valid combination, so we add it to `result`.
            - Recursive Case: At each call, try to add '(' if we still have an allowance
              for more opens, or ')' if there are opens that need closing.
            """
            # Base case: We have formed a complete and valid parentheses combination
            if openn == close == n:
                # ''.join(stack) creates a single string from the stack list, which we add to the result
                result.append("".join(stack))
                return
            
            # Recursive case: Add an opening parenthesis if we haven't reached `n` yet
            if openn < n:
                stack.append("(")  # Place '(' in our current stack
                backtrack(openn + 1, close)  # Recurse with incremented open count
                stack.pop()  # Backtrack by removing the last added '('
            
            # Recursive case: Add a closing parenthesis if `close` count is less than `openn` count
            # Ensures we only close open brackets, maintaining balance
            if close < openn:
                stack.append(")")  # Place ')' in our current stack
                backtrack(openn, close + 1)  # Recurse with incremented close count
                stack.pop()  # Backtrack by removing the last added ')'
        
        # Begin the recursive backtracking with 0 open and 0 close
        backtrack(0, 0)

        return result