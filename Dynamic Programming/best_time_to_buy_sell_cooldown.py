from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Intuition:
        This problem uses recursion with memoization to decide the maximum profit at each step. 
        - The "buying" state determines whether you're allowed to buy or must sell.
        - At each index, we can either:
          1. Buy/sell, which changes the state and affects the profit.
          2. Skip the day, keeping the current state.
        - After selling, we add a cooldown (i.e., skip the next day).
        - The recursive function explores all possible decisions and memoizes results 
          to avoid recomputation.
        """

        cache = {}  # Memoization cache: key = (i, buying), value = maxProfit

        def dfs(i, buying):
            # Base case: If out of bounds, return 0 (no profit possible)
            if i >= len(prices):
                return 0

            # If this state is already computed, return the cached result
            if (i, buying) in cache:
                return cache[(i, buying)]

            # Buying state: Decide whether to buy or skip
            if buying:
                # Again, if we have the option of buying, we can do two things, either buy, or skip the day. 
                # Idea is to check which would yield the best result (max profit)
                buy = dfs(i + 1, not buying) - prices[i]  # Buy and move to "selling" state
                skip = dfs(i + 1, buying)  # Skip the day
                cache[(i, buying)] = max(buy, skip)  # Maximize profit
            else:  # Selling state: Decide whether to sell or skip
                # Same here with selling. If we have the option to sell the stock, we can either sell it, or skip the day.
                # idea  is to check which maximizes the profit
                sell = dfs(i + 2, not buying) + prices[i]  # Sell and move to "buying" after cooldown
                skip = dfs(i + 1, buying)  # Skip the day
                cache[(i, buying)] = max(sell, skip)  # Maximize profit

            return cache[(i, buying)]  # Return cached result for this state

        return dfs(0, True)  # Start from index 0, with the ability to buy