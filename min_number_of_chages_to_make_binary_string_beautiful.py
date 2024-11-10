class Solution:
    def minChanges(self, s: str) -> int:
        if ("1" in s and "0" not in s) or ("0" in s and "1" not in s):
            return 0

        def checkBeauty(chunk):
            if chunk in {"11", "00"}:
                return True
            return False

        chunks = []

        for i in range(0, len(s)-1, 2):
            chunk = s[i:i+2]
            chunks.append(chunk)

        print(chunks)
        count =0 
        
        for chunk in chunks:
            if checkBeauty(chunk) == False:
                count += 1

        
        return count