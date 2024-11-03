import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        factor = math.floor(n/3)
        print(factor)
        hashmap = {}

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1

        result = []
        for key, value in hashmap.items():
            if value > factor:
                result.append(key)
        
        return result
    

"""
The above was my own solution. 
you can also do it with boyer moore voting algorithm
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Step 1: Find potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if candidate1 is not None and num == candidate1:
                count1 += 1
            elif candidate2 is not None and num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify the candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        result = []
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)

        return result