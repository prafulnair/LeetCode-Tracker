"""
Write a function 'howSum(targetSum, numbers)' that takes in a 
targetSum and an array of numbers as arguments.

The function should return an array containing any combination of 
elements that add upto exactly the targetSum. If there is no combination
that adds up to the targetSum, then return null.

if there are multiple combinations possible, you may return any single one
"""

def howSum(targetSum, nums, memo=None):
    if memo == None: memo = {}

    if targetSum in memo: return memo[targetSum]
    
    if targetSum < 0: 
        memo[targetSum] = None
        return None
    
    if targetSum == 0: 
        memo[targetSum] = []
        return []

    for n in nums:
        reminder = targetSum - n
        res = howSum(reminder, nums, memo)
        if res!= None:
            memo[targetSum] = res + [n]
            return res + [n]
        
print(howSum(300,[2]))