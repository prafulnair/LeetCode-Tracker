class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        forward = []
        backward = []

        prod = 1
        for i in range(0, len(nums)):
            if i == 0:
                prod = prod * 1
            else:
                prod = prod * nums[i-1]
            forward.append(prod)
       
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums) -1:
                prod = prod * 1
            else:
                prod = prod * nums[i+1]
            backward.append(prod)

        backward = backward[::-1]
        
        result = []
        for i in range(0, len(nums)):
            res = backward[i]* forward[i]
            result.append(res)

        print(forward)
        print(backward)
        
        return result
        
s = Solution()
print(s.productExceptSelf([1,2,3,4]))