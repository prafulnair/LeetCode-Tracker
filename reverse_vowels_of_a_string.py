class Solution:
    def reverseVowels(self, s: str) -> str:
        
        p, q = 0, len(s) - 1
        vowels = {'a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        while (p < q):
            if s[p] in vowels and s[q] in vowels:
                s[p], s[q] = s[q], s[p]
                p += 1
                q -= 1
            else:
                if s[p] not in vowels:
                    p += 1
                if s[q] not in vowels:
                    q -= 1

        s = "".join(s)
        return s
"""
Simple Two pointer approach. if both are vowels, swap. Else, increment if s[p] is not vowel, and decrement 
s[q] if its not vowel. 
using {} set instead of [] for faster access and lookup
"""
"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

"""