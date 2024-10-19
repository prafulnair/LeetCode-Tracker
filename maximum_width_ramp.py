class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
         
         # Lets try sliding window approach
         # But for accuracy and efficiency, we gotta do preprocessing.
         # create an array that for each num[i] determines max value to the right of that value.

        max_right = [0] * len(nums)
        prev_max = 0
        for i in range(len(nums)-1, -1, -1):
            max_right[i] = max(nums[i], prev_max)
            prev_max = max_right[i]

        res = 0
        i, j = 0, 0
        while(j < len(nums)): # Can use a for loop instead of this, this looks like O(n2) but it isnt. 
            while nums[i] > max_right[j]:
                i += 1
            
            res = max(j - i, res)
            j += 1
        return res