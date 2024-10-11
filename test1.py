class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # this is another clever approach that you thought by yourself :)
        # return (len(nums) != len(set(nums)))

        # but conventially, the following way is the way to go
        seen = set() # create a hashset

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
        

"""
Valid Anagram
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """the below is of time complexity O(n log n) we can do better with hashmap"""
        # if len(s) != len(t):
        #     return False
        # slist = list(s)
        # tlist = list(t)

        # slist.sort()
        # tlist.sort()

        # for i in range(len(slist)):
        #     if slist[i] != tlist[i]:
        #         return False
        
        # return True

        if len(s) != len(t):
            return False
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1

        for c in t:
            if c not in hashmap or hashmap[c] == 0:
                return False
            else:
                hashmap[c] -= 1

        return True  
        
"""
TWO SUM
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}
        # Store the number and the index in the hashmap 
        # hashmap[number] = index. 
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            else:
                map[nums[i]] = i

        return []
    

"""  
GROUP ANAGRAM
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        for element in strs:
            key = ''.join(sorted(element))
            if key not in my_map:
                my_map[key] = [str(element)]
            else:
                my_map[key].append(str(element))

        result_list = []
        for val in my_map.values():
            result_list.append(val)

        return result_list