"""
You are given a list 'numbers' containing positive integers and a 'target'. 
You have to tell if the numbers in the list 'numbers' add upto the target. You can reuse the numbers in numbers multiple times ( i dont know how this makes any sense but yeah)
"""
def canSum(targetSum, numbers, memo=None):
    if memo == None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for n in numbers:
        remainder = targetSum - numbers.pop() ## originally its remainder = targetSum - n, considering how we can use the numbers multiple times, 
                                                #but it never made sense to me so I am like, if I consider first number, in the next recurrsive calls, I can only use all other numbers except the one I just chose
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


print(canSum(7, [2, 3])) # True
print(canSum(7, [5, 3, 4, 7])) # True
print(canSum(7, [2, 4])) # False
print(canSum(8, [2, 3, 5])) # True
print(canSum(3000, [7, 14])) # False -> Works fast with large inputs!
