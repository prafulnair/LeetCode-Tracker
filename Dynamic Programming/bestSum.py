def bestSum(target, nums, memo=None):
    if memo == None:
        memo = {}
    if target == 0:
        return []
    if target < 0:
        return None
    
    if target in memo:
        return memo[target]

    shortestCombination = None

    for n in nums:
        remainder = target - n
        remainderCombination = bestSum(remainder, nums, memo)
        
        if remainderCombination is not None:
            combination = remainderCombination + [n]

            if shortestCombination == None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    memo[target] = shortestCombination
    return shortestCombination

print(bestSum(100, [5,3,4,7]))