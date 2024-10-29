class Solution:
    def findMin(self, nums: list[int]) -> int:

        minn = float("inf")

        def findMin(p, q):

            if p > q:
                return minn

            mid = p + (q-p) // 2

            minLeft = findMin(p, mid-1)
            minRight = findMin(mid+1, q)

            return min(nums[mid], minLeft, minRight)

        return findMin(0, len(nums)-1)
        