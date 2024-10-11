

"""
0,1,3,0,4,0,4,2
          k 
"""

nums = [0,1,2,2,3,0,4,2]
val = 2
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        k =0
        count = 0 
        for i in range(0,len(nums)):
            if nums[i] == val:
                continue
            if nums[i]!= val:
                nums[k] = nums[i]
                count+=1
                k = k + 1
        
        return count

"""
Moral Breaker Alert ! While its tagged easy, since I was out of practice at the time I was solving the problem it was really difficult for me to crack
My first approach was to find the first occurence of the element to be removed and then going and iterating from their, finding the
element that we dont want to be removed, swapping it with the index of the element we wanted to remove and ...soemthign like that
That did not go well

The correct approach is this:
initialize k at 0. Then we iterate through the array and say
1. if the value is valid (the one not to be removed) - swap it with the number at index k. k keeps track of the number that we want to be removed
2. If its the value that is to be removed, continue
it works elegantly even when there is no occurence of the element that we want to be removed
for example it starts by initializing at 0. so nums[0] = 0 which is not 2, that we want to remove
according to the algo, we swap it with nums[k]. nums[k] becomes nums[i], basically itself and increment k

when we finally reach 2, we leave k there, without incrementing. And next time we find a element that's valid, put it in nums[k].


I did not crack this on my own, but I coded it on my own/. I had to here the explanation of neetcode
"""