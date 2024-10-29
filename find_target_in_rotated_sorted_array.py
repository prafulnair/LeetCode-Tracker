class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        def findIt(p, q):

            if p > q:
                return -1
            
            mid = p + (q -p) // 2

            if nums[mid] == target:
                return mid
            findItLeft = findIt(p, mid-1)
            if findItLeft != -1:
                return findItLeft
            findItRight = findIt(mid+1, q)
            return findItRight

        return findIt(0, len(nums)-1)