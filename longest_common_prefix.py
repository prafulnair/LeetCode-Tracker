class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        first_word = list(strs[0])
        last_word = list(strs[len(strs)-1])



        n = 0
        for c in first_word:
            if c == last_word[n]:
                n+=1
            else:
                break
        
        result = ''.join(first_word[:n])
        
        return result
    
print(Solution.longestCommonPrefix(Solution, ["flower","flow","Zebra"]))

"""
Its farily simple solution. I sorted the array using inbuilt sorting function, O( n log n) time complexity.
Then All I am doing is comparing the smallest and largest word, each of their letter, sequentially, to see how many of them
matches. I just need to worry about two words to be honest, the smallest, and the largest. I dont need to worry 
about every single element. Infact, I think I can make this more efficient by just finding the largest 
"""

"""
This is another solution that I found I have submitted but I have no recall when
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        first_word = strs[0] if strs else ""

        for currword in strs:
            maxlength = max(len(first_word), len(currword))

            while(first_word != currword[:maxlength]):
                maxlength = maxlength - 1
                first_word = first_word[:maxlength]
                if(first_word == ""):
                    return ""

        return first_word