"""
BETTER SOLUTION IS THE SECOND SOLUTION ...
Leetcode #347 - Top K frequent elements (MediuM)
347. Top K Frequent Elements
Solved
Medium


Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


"""

import heapq 
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        heap = []

        map = {}

        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
        
        for key, value in map.items():
            element = [key, value]
            heap.append(element)
        print(heap)
        heapq.heapify(heap)
        result = []

        while (k!=0):
            ele = heapq.heappop(heap)
            result.append(ele[0])
            k -= 1

        return result

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        my_maps = {}
        for n in nums:
            if n not in my_maps:
                my_maps[n] = 1
            else:
                my_maps[n]+=1

        frequency_list = [(num,freq) for num, freq in my_maps.items()]
        frequency_list.sort(key = lambda x: x[1], reverse = True)

        final_list = [num for num, freq in frequency_list[:k]]
        
        return final_list
    
"""The game is defined after we create the hashmap. That is, we want to create a list that stores key value pair as 
tuples, and sort them on the basis of value
for that we used list comprehension, the first line is pretty straightforward and self explainatory
the second line does the job. sort the list based on second element of each tuple

Here is the explanation provided by GPT
Components
frequency_list.sort():

This is the method used to sort the list frequency_list in place. This means that the list is modified directly, and no new list is created.
key=lambda x: x[1]:

key Parameter: The key parameter specifies a function that will be called on each element in the list to determine the value used for sorting.

lambda x: x[1]: This is a lambda function, which is an anonymous function defined using the lambda keyword.

x: Each element of frequency_list (which is a tuple like (1, 3)).
x[1]: The second item in the tuple, which is the frequency of the element. In the tuple (1, 3), x[1] would be 3.
This lambda function tells the sort method to sort the list based on the second element of each tuple (i.e., the frequency).

reverse=True:

This parameter tells the sort method to sort the list in descending order. By default, sort arranges elements in ascending order. Setting reverse=True changes this to descending order.
"""

nums = [1,1,1,2,2,3]
k = 2
print(Solution.topKFrequent(Solution,nums,k ))
    

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Create a hashmap to store value and its frequence
        map = {}

        # Store the elements of nums and its freq
        for n in nums:
            map[n] = map.get(n,0) + 1

        # One way to sort the hashmap by its value. 
        map = dict(sorted(map.items(), key=lambda item: item[1], reverse = True))

        # Final list to store the result
        result = []
        for key in map.keys():
            result.append(key)

        # just represent the last 
        # result = result[-k:]    # If reverse is not set as True, you have to use this   
        result = result[:k]  
        return result

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hashmap to store value and its frequence
        map = {}

        # Store the elements of nums and its freq
        for n in nums:
            map[n] = map.get(n,0) + 1

        # One way to sort the hashmap by its value. 
        map = dict(sorted(map.items(), key=lambda item: item[1], reverse = True))

        # Final list to store the result
        result = []
        for key in map.keys():
            result.append(key)

        # just represent the last 
        # result = result[-k:]    # If reverse is not set as True, you have to use this   
        result = result[:k]  
        return result
"""