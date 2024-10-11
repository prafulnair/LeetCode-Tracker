
class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        hashmap = {}
        min_distance = float('inf')

        for i, card in enumerate(cards):
            if card in hashmap:
                distance = i - hashmap[card] + 1
                min_distance = min(min_distance, distance)
            hashmap[card] = i

        return min_distance if min_distance != float('inf') else -1
    
"""
Solution for the "Minimum Consecutive Cards to Pick Up" problem.

This implementation uses a hash map to track the last seen index of each card while iterating 
through the list. 
Whenever a duplicate card is found, it calculates the distance between the current index and 
the last seen index.
The minimum distance across all duplicates is recorded, 
and if no duplicates are found, the function returns -1.

Time Complexity: O(n) - We iterate through the list once.
Space Complexity: O(n) - The hash map stores the last seen index of each card.

"""