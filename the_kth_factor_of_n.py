#AMAZON

# Leetcode 1429 The Kth Factor of n
# This has the time complexity of O(N)


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        # Brute force solution

        fac = 0
        for i in range(1, n+1):
            if n % i == 0:
                fac += 1
            if fac == k:
                return i
        
        return -1

import math
## This has time complexity of (root(n) log  (root (n)))
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

        # Collect factors up to sqrt(n)
        for i in range(1, math.isqrt(n) + 1):
            if n % i == 0:
                factors.append(i)  # Add the smaller factor
                if i != n // i:    # Avoid duplicate for perfect squares
                    factors.append(n // i)  # Add the larger factor

        # Sort factors to get them in order
        factors.sort()

        # Return the k-th factor or -1 if not enough factors
        return factors[k - 1] if k <= len(factors) else -1