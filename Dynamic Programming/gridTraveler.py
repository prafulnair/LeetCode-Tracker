"""
Say that you are a traverler on a 2D grid. You begin in the top-left corner
and your goal is to travel to the bottom-right corner
You may only move down or right. 

In how many ways can you travel to the goal on a grid with dimensions m * n
Write a function 'gridTraveler(m, n)' that calculates this. 
"""


def gridTraveler(m, n, ways = {}):

    # lets hashout the base cases:
    if m == 0 or n == 0:
        return 0
    elif m == 0 and n == 0:
        return 0 
    if m == 1 and n == 1:
        return 1
    
    if (m,n) in ways:
        return ways[(m,n)]

    else:
        ways[(m,n)] = gridTraveler(m-1,n,ways) + gridTraveler(m,n-1,ways)
    
    return ways[(m,n)]


print(gridTraveler(18,18))


"""
EXPLANATION
So this is basically overglorified fibo problem, i mean we can say that.
but the idea is that we can only increase / decrease m or n 1 at a time. 
so in this case, I am saying I am travelling from m,n to reach 1,1
But we can ofcourse program this the other way around which is more intuitive and looks sound logically where we start at 1,1 and try to reach m,n
    In that case of course, we will do the increment, instead of m-1 or n-1

so yeah. The base case is if either of the dimension is 0, it does not make senes (aka its not valid) so return 0
If both are 1, then we found our target destination, so return 1. 
Check if we already have cached data in the hashmap that we are using (ways = {})
else, ways[(m,n)] = gridTraveler(m-1,n,ways) + gridTraveler(m,n-1,ways). 
    and then we finally return ways[(m,n)]
"""


