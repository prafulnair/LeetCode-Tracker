class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        curr_profit = 0
        max_prof = 0
        l, r = 0, 1
 
    
        while(l < r):
            if r >= len(prices):
                break
            if prices[l] < prices[r] : 
                print(prices[l], prices[r])
                curr_profit = prices[r] - prices[l]
                max_prof = curr_profit + max_prof
            
                l = r
                r += 1
                
            elif prices[r] <= prices[l]:
                l = r
                r+=1
                
        return max_prof
    
s = Solution()

print(s.maxProfit([7,1,5,3,6,4]))

"""
Its really important to understand why this solution works. 
You did not get this at first try. You almost started the solution video and you did this by trial and error
Which means you had a basic intuition and you were just trying to get it right
You could not also recall how you solve the Buy and sell stock I, you were not able to
come to a conclusion that you had to use two pointer approach and solve this. You had to look back at your submitted
solution, then you got some idea, and you somehow solved it

Now, in this case, we can do multiple transaction. We dont have to wait for the best time to sell a bought stock
We can sell it as soon as we see a rise in the stock price. for example we bought the stock on day 2 (val = 1), and then we immediately sell it on next day, at val = 5.
then we continue , by bringing l pointer to current r pointer and and incrementing r by 1, and continuing this comparison process.

"""

"""
ou are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

"""