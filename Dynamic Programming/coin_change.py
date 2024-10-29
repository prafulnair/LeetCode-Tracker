class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        # a dp array containing max (it could be amt + 1, for us thats max. ) it's
        # lenght would be as big as amout, so we calculating howmany coins
        # for 0 , 1, 2 ..to amount.
        dp = [amount + 1] * (amount + 1)

        #base case
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        return dp[amount] if dp[amount]!= amount + 1 else -1 