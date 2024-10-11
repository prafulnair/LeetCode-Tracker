class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # remove all spaces
        s = s.replace(" ", "")

        # make all character to lower (or upper, does not matter)
        s = s.lower()

        # remove all non alpha numeric character 
        s = ''.join(ch for ch in s if ch.isalnum())

        # classic double pointer method
        p, q = 0, len(s) - 1

        while(p < q):
            if s[p] != s[q]: return False
            p += 1
            q -= 1

        return True







class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        
        s = s.lower()
        
        res = ""
        for c in s:
            if c.isalnum():
                res += c
        p, q = 0, len(res)-1
        
        while(p < q):
            if res[p]!=res[q]:
                return False
            p += 1
            q -= 1
            
        return True
    

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.


"""