"""
THis is the solution that I came up by myself, but it takes additional O(n) space. 
There are other method that rotates the array "In place"
"""
def rotate(self, nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    i = 0
    result = [0] * len(nums)
    result = [nums[j] for j in range(0,len(nums))]
    
    while(i < len(nums)):
        if i >= len(nums):
            break
        calculatedIndex = (i + k) % len(nums)

        nums[calculatedIndex] = result[i]
        i+=1


print(rotate([1,2,3,4,5,6,7],3))

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # this is because k can be bigger than the length of num
        
        # Step 1 : is to reverse the entire Array
        # Step 2: is to reverse the first k elements
        # Step 3 is to reverse the remaining elements 
        
        # Step 1:
        l, r = 0, len(nums) - 1
        while (l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
        # Step 2: just change the range
        l, r = 0, k - 1
        while (l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
            
        # Step 3: again, just chane the range
        l, r = k, len(nums) - 1
        
        while (l<r):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
            
        return nums