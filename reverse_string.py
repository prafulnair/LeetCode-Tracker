class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p, q = 0, len(s) - 1
        
        while(p<q):
            s[p],s[q] = s[q], s[p]
            p += 1
            q -= 1
            
        return s