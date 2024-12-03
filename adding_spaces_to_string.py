class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        
        result = ""
        if not spaces:
            return s
        startIndex = 0
        for sp in spaces:
            result = result + s[startIndex:sp]+" "
            startIndex = sp  

  

        return result + s[spaces[-1]:]        