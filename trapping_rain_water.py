from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        p, q = 0, len(height) - 1

        leftMax, rightMax = height[p], height[q]
        res = 0

        while (p < q):
            if leftMax < rightMax:
                p += 1
                leftMax = max(leftMax, height[p])
                res += leftMax - height[p]
            else:
                q -= 1
                rightMax = max(rightMax, height[q])
                res += rightMax - height[q]

        return res