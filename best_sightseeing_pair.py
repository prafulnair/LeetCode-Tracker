#Greedy
#Dynamic Programming
#Arrays

"""
Intuition:
The problem revolves around finding the maximum score for a sightseeing pair. 
To achieve this, we need to maximize the expression `values[i] + values[j] + i - j`. 
Rewriting this as `(values[i] + i) + (values[j] - j)` reveals that we can split the problem:
1. Maintain the best possible value of `values[i] + i` seen so far (`bestSeen`).
2. Iterate through the array and calculate the score for each `values[j]` with the current `bestSeen`.
3. Keep updating the `bestScore` with the maximum value of `values[j] + bestSeen - j`.
4. Simultaneously update `bestSeen` to ensure it always represents the maximum value of `values[i] + i` up to the current index.

By breaking the problem into these steps, we avoid the need for a brute-force O(n^2) solution and achieve an O(n) solution by processing the array in a single pass.
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        bestSeen = values[0] + 0
        bestScore = 0 

        for i in range(1, len(values)):
            score = values[i] + bestSeen - i
            bestScore = max(bestScore, score)
            bestSeen = max(bestSeen, values[i]+i)
        
        return bestScore