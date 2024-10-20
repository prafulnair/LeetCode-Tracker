import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        # We define our search space between 1 (minimum speed) and the largest pile (maximum speed),
        # since Koko must eat at least 1 banana per hour, and no more than the size of the largest pile.
        l, r = 1, max(piles)
        
        # We initialize 'result' to the maximum speed (max pile size) as a possible answer.
        result = r

        # Binary search to find the optimal eating speed
        while l <= r:
            # We calculate the middle value of the current search space as the potential eating speed.
            k = (l + r) // 2
            
            # We calculate how many hours Koko would take to finish all piles if she eats at speed 'k'.
            hours = 0 

            # For each pile, we compute how many hours it takes to eat that pile.
            # Use math.ceil to ensure any leftover bananas in a pile are accounted for as an extra hour.
            for p in piles:
                hours += math.ceil(p / k)
            
            # If Koko can finish eating all the bananas within 'h' hours at speed 'k',
            # then 'k' is a valid solution, but we try to minimize the speed.
            if hours <= h:
                result = min(result, k)  # Update result with the minimum valid speed found so far.
                r = k - 1  # Search the left half for a potentially smaller valid speed.
            else:
                # If Koko can't finish within 'h' hours, increase the speed (search the right half).
                l = k + 1

        # Return the minimum eating speed that allows Koko to finish within 'h' hours.
        return result
