

class Solution:
## DYNAMIC PROGRAMMING

    def countWays(n, reached = {}, ways=0):
        if n in reached:
            # print(f"No need to calculate {n} , we already have data which is {reached[n]}")
            return reached[n]
        if n == 0:
            ways+=1

            return ways
        if n < 0:
            ways+=0
        
            return ways
        else:
            # print(f'for {n}: reached here')
            reached[n] = Solution.countWays(n-1, reached, ways) + Solution.countWays(n-2, reached, ways)
        

        return reached[n]
 

    def climbStairs(self, n: int) -> int:

        ans = Solution.countWays(n)
        return ans
    
print(Solution.climbStairs(Solution.climbStairs,99))

"""
class Solution:
           
    
    def climbStairs(self, n: int) -> int:
        
        def countWays(n, memo=None, ways = 0):
            if memo == None:
                memo = {}

            if n in memo:
                return memo[n]

            if n == 0:
                ways += 1
                return ways

            if n < 0:
                ways += 0
                return ways

            else:
                memo[n] = countWays(n-1, memo, ways) + countWays(n-2, memo, ways)

            return memo[n]
        
        result = countWays(n)
        return result
        
        
"""