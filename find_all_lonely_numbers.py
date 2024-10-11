"""
Solution to find lonely numbers in a list.

Approach:
1. Use a hashmap to count occurrences of each number in the list.
2. Convert the list to a set for O(1) average-time complexity checks.
3. Iterate through the unique numbers in the set:
   - A number is considered lonely if:
     - It appears exactly once in the hashmap.
     - Neither its predecessor nor successor exists in the set.
4. Append the lonely numbers to the result list.

Time Complexity:
- O(n) for counting and set operations.

Space Complexity:
- O(n) for storing counts in hashmap and unique numbers in the set.
"""


class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        lonely = []

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        set_nums = set(nums)
        for num in set_nums:
            if hashmap[num] == 1 and num + 1 not in set_nums and num - 1 not in set_nums:
                lonely.append(num)

        return lonely

"""
You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers 
(i.e. x + 1 and x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.

Example 1:

Input: nums = [10,6,5,8]
Output: [10,8]
Explanation: 
- 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
- 5 is not a lonely number since 6 appears in nums and vice versa.
Hence, the lonely numbers in nums are [10, 8].
Note that [8, 10] may also be returned.

Example 2:

Input: nums = [1,3,5,3]
Output: [1,5]
Explanation: 
- 1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums.
- 5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums.
- 3 is not a lonely number since it appears twice.
Hence, the lonely numbers in nums are [1, 5].
Note that [5, 1] may also be returned.

"""