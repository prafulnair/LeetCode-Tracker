import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        """
        Intuition:
        The goal is to minimize the maximum number of products assigned to any store. 
        We can use binary search to efficiently find the smallest possible maximum (`x`).

        - Start by assuming `x` could range from 1 (minimum possible value) to the maximum quantity in the array.
        - For a given value of `x`, check if it's feasible to distribute all products such that no store gets more than `x` products.
        - If it's possible to distribute with `x`, try smaller values of `x` (to minimize it further).
        - If not, increase `x` and try again.

        The function `can_distribute(x)` checks whether it's feasible to distribute all products to `n` stores such that no store gets more than `x` products.
        """

        def can_distribute(x):
            """
            Check if we can distribute all quantities to `n` stores 
            such that no store has more than `x` products.
            """
            stores = 0  # Count of stores needed
            for quantity in quantities:
                # Divide the products of this type into groups of size at most `x`
                # and count how many groups (stores) are needed.
                stores += math.ceil(quantity / x)
            # Check if the total number of stores needed is within the available stores `n`.
            return stores <= n

        # Binary search for the minimum possible maximum value
        l, r = 1, max(quantities)  # Minimum and maximum bounds for `x`
        res = r  # Store the result (initially the upper bound)

        while l <= r:
            mid = (l + r) // 2  # Calculate the midpoint of the current range

            if can_distribute(mid):
                # If feasible with `mid`, try a smaller value
                res = mid  # Update the result to the current midpoint
                r = mid - 1  # Narrow the search to smaller values
            else:
                # If not feasible, increase the lower bound
                l = mid + 1

        return res