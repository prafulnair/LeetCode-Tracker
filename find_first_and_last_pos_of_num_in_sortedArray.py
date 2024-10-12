class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Base Case
        if not nums: return [-1, -1]  # handle empty list case

        # Find the leftmost one
        result = []
        start, end = 0, len(nums) - 1
        leftmost = -1
        while start <= end:
            mid = start + (end - start) // 2  # Correct mid calculation
            if nums[mid] == target:
                leftmost = mid
                end = mid - 1  # continue searching on the left side
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if leftmost == -1:  # if target is not found at all
            return [-1, -1]

        # Find the rightmost one
        start, end = 0, len(nums) - 1
        rightmost = -1
        while start <= end:
            mid = start + (end - start) // 2  # Correct mid calculation
            if nums[mid] == target:
                rightmost = mid
                start = mid + 1  # continue searching on the right side
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return [leftmost, rightmost]