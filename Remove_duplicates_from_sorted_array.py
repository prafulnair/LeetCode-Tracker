"""
26. Remove Duplicates from Sorted Array
Solved
Easy

Topics
Companies

Hint
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order."""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
            return 1
        k= 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i += 1
                nums[i] = nums[j]
            
        return i + 1
                
        

s = Solution()
s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])


""" Was not able to solve with my method where I overcomplicated it a bit. Following was my initial approach
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        end = len(nums) - 1
        p = 0
        q = 0

        while (q!= end - 1):
            q+=1
            if nums[p] == nums[q]:
                nums[q] = '_'
            else:
                p = q

        p = 0 
        q = 0
        while(q<= len(nums) - 1):
            if type(nums[q]) is int and p != q:
                nums[p] = nums[q]
                nums[q] = '_'
                p = q
                q+=1
            elif type(nums[q]) is int and p == q:
                p+=1
                q+=1
            elif nums[q]=='_':
                q+=1
        
        print(nums)

Chat gpt proposed the correct method. Heree is the explanation
Your approach to solving the problem has the right idea, but it's a bit overcomplicated. 
You don't need to use two separate passes and placeholders ('_') to solve this problem. 
Instead, you can use a more straightforward two-pointer technique to remove duplicates in place efficiently.

Here's a more concise and correct approach using the two-pointer method:

Initialize two pointers: i which will track the position of unique elements and j which will iterate through the list.
Iterate through the list with j: For each element, check if it is different from the previous element (to handle duplicates). 
If it is different, assign it to nums[i] and increment i.

Explanation:
Initialization:

Check if nums is empty. If it is, return 0 since there are no elements to process.
Initialize i to 0. This pointer will track the position of the last unique element.
Iterate Through the List:

Start from the second element (index 1) and iterate through the list using j.
If nums[j] is not equal to nums[i], it means nums[j] is a new unique element.
Increment i and update nums[i] to be nums[j].
Return the Number of Unique Elements:

i + 1 will be the number of unique elements because i is the index of the last unique element.
"""