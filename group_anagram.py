"""
Leetcode 49 - GROUP ANAGRAMS, Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        """This Approach is a Good initial attempt, it solved about 96 out 126 test cases, you solved this in about 40 mins. 
        But this does not work for cases like car and caar, as they fall into same set - c, a, r, but are obviously not ANAGRAM.
        We need a different Appraoch"""
        my_map = {}
        for elements in strs:
            key = tuple(set(elements))
            if key not in my_map:
                my_map[key] = [elements]
            else:
                my_map[key].append(elements)
                
        # for key, value in my_map.items():
        #     print(f'{key}: {value}')

        result_list = []

        for value in my_map.values():
            result_list.append(value)
        
        print(result_list)

    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        """
        instead of using set as key, we use sorted word itself as key. if the sorted word matches, then its in the same group
        so car would be acr
        rac would also be acr. But caar would be aacr, which is different. 
        """
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


strs = ["eat","tea","tan","ate","nat","bat"]
#Solution.groupAnagrams(Solution, strs)
print(Solution.groupAnagrams2(Solution,strs))