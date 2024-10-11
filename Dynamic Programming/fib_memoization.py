
"""
Write a function fib(n) that takes in a nnumber as an argument
The function should return the n-th  number of the fib sequence
"""

def fib(n):
    if n <=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)





"""
SO this is very basic recrusive approach to solving the
problem
Time complexity - O(2^n) and O(n) space complexity. 
"""

"""
Lets try to do better.  
Answer to this is Memoization 

so for memoization, we have to use some kind of fast access data structure
We gonna use Hashmap for this
the keys would be the argument to the functions, and value would be 
the return value

"""
def fib_mem(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <=2:
        return 1
    else:
        memo[n] = fib_mem(n-1, memo) + fib_mem(n-2, memo)
        return memo[n]

"""
Now lets see how have we improved
on the first call of this function,a map 'memo' will be created that
stores the result of some fib calculations
so if we have already a calculation done for a ffunction call we can
directly access it and use it for further calculation

- if n is in memo, fetch the result
- else if n is less than or equal to 2, simply return 1.
- else calculate the function call fib(n-1, memo) + fib(n-2, memo) and 
return memo[n]

Time complexity = O(2n) = O(n)
Space complexity = O(n)
"""


for i in range(1,51):
    print(f'{i}: {fib_mem(i)}')


