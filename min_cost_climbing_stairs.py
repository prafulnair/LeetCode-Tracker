class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        n = len(cost)
        memo = [-1] * n
        
        def minCost(i):
            if i >= n:  # Base case
                return 0
            if memo[i] != -1:  # Check if already computed
                return memo[i]
            
            # Compute the minimum cost of taking 1 step or 2 steps
            one_step = minCost(i + 1)
            two_step = minCost(i + 2)
            
            memo[i] = min(one_step, two_step) + cost[i]
            return memo[i]
        
        # You can start from either step 0 or step 1
        return min(minCost(0), minCost(1))
