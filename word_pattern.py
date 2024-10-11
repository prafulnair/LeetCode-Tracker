class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:       
        pat = {}
        for i in range(len(pattern)):
            pat[pattern[i]] = str(i) if pattern[i] not in pat else pat[pattern[i]] + str(i)


        string = {}
        s_list = s.split(" ")
        print(s_list)
        for i in range(len(s_list)):  # Corrected loop to iterate over indices
            string[s_list[i]] = str(i) if s_list[i] not in string else string[s_list[i]] + str(i)
        for val in pat.values():
            print(val)

        for val in string.values():
            print(val)

        if len(pat)!=len(string):
            return False
        for val1,val2 in zip(string.values(),pat.values()):
            if val1!=val2:
                return False
        return True
            
"""

290. Word Pattern
Solved
Easy

Topics
Companies
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""