class Solution:
    """
    This code only works for neetcode interface. Does not pass all test in Leetcode
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1 and s1 in s2:
            return True
        elif len(s1)==1 and s1 not in s2:
            return False
        theset = set(s1)
        size = len(theset)/[iu 8
        p = 0
        q = size
        
        while(q<=len(s2)):
            curr =  s2[p:q]
            curr = sorted(curr)
            s1 = sorted(s1)

            if curr == s1:
                return True
            p+=1
            q+=1
        

        
        return False
    

s = Solution()

print(s.checkInclusion("adc","dcda"))