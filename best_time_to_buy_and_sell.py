class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        l = 0
        r = 1
        max_prof = 0 
        
        while(l < r):
            if r >= len(prices):
                break
            if prices[l] < prices[r] : 
                curr_profit = prices[r] - prices[l]
                max_prof = curr_profit if curr_profit > max_prof else max_prof
                r += 1
            elif prices[r] <= prices[l]:
                l = r
                r+=1
        
        return max_prof
    
s = Solution()

print(s.maxProfit([7,1,5,3,6,4]))

"""
SOLVING THIS USING DYNAMIC PROGRAMMING

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Initialize variables
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through each price
        for price in prices:
            
            # Update the minimum price encountered so far
            min_price = min(min_price, price)
            
            # Calculate the profit if we sell at the current price
            profit = price - min_price
           
        # Update the maximum profit
            max_profit = max(max_profit, profit)
        
        # Return the maximum profit
        return max_profit
    
"""
Imagine you have a list of prices for a toy on different days, and you want to buy the toy at the lowest price and sell it at the highest price after buying it. Your goal is to find out the most money you can make from this buy-sell transaction.
Step-by-Step Explanation

    Initialize Variables:
        We start by saying the min_price is a really big number (infinity). This is like starting with a super high price that any real price will be lower than.
        We also start with max_profit as 0 because we haven't made any transactions yet, so we can't have any profit.

    Iterate Through Prices:
        We look at each price one by one.
        For each price, we do two things:
            We check if this price is lower than our current min_price. If it is, we update min_price to this price because it's the new lowest price we've seen.
            We calculate the profit we would make if we bought at the min_price and sold at the current price. This is done by subtracting the min_price from the current price.
            We then check if this profit is higher than our current max_profit. If it is, we update max_profit to this new profit.

    Return the Result:
        After we've looked at all the prices, the max_profit will hold the highest profit we can achieve from one buy-sell transaction.

Example Walkthrough

Let's say the prices on different days are [7, 1, 5, 3, 6, 4].

    We start with min_price as infinity and max_profit as 0.

    Day 1:
        Price: 7
        min_price becomes 7 (since 7 is less than infinity).
        Profit if sold today: 7 - 7 = 0
        max_profit remains 0 (since 0 is not greater than 0).

    Day 2:
        Price: 1
        min_price becomes 1 (since 1 is less than 7).
        Profit if sold today: 1 - 1 = 0
        max_profit remains 0 (since 0 is not greater than 0).

    Day 3:
        Price: 5
        min_price remains 1 (since 1 is less than 5).
        Profit if sold today: 5 - 1 = 4
        max_profit becomes 4 (since 4 is greater than 0).

    Day 4:
        Price: 3
        min_price remains 1 (since 1 is less than 3).
        Profit if sold today: 3 - 1 = 2
        max_profit remains 4 (since 2 is not greater than 4).

    Day 5:
        Price: 6
        min_price remains 1 (since 1 is less than 6).
        Profit if sold today: 6 - 1 = 5
        max_profit becomes 5 (since 5 is greater than 4).

    Day 6:
        Price: 4
        min_price remains 1 (since 1 is less than 4).
        Profit if sold today: 4 - 1 = 3
        max_profit remains 5 (since 3 is not greater than 5).

After looking at all the prices, the best profit we could make is 5, which is the result
"""

"""
121. Best Time to Buy and Sell Stock
Solved
Easy

Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""