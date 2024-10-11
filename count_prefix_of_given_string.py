class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        
        count = 0
        for w in words:
            if s.startswith(w):
                count += 1
        
        return count
    

"""
Solution for the "Count Prefixes of a Given String" problem.

This implementation iterates through a list of words and counts how many of them are prefixes of the given string `s`.
For each word in the list, the `startswith()` method is used to check if it is a prefix of `s`.
The total count of such prefixes is returned as the result.

Time Complexity: O(n * m) - Where 'n' is the number of words and 'm' is the average length of the words. 
Space Complexity: O(1) - Only a counter variable is used for tracking.

"""