class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        jindices = []
        sett = set()
        for j in range(0, len(nums)):
            if nums[j] == key:
                jindices.append(j)

        for i in range(0, len(nums)):
            for j in jindices:
                if abs(i - j) <=k and nums[j] == key:
                    sett.add(i)

        return sett
    
""" The question does not make much sense and I did not enjoy doing it"""
"""Link to the problem: 
https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/"""