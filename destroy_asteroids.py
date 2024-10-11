"""
Solution to determine if all asteroids can be destroyed given initial mass.

Approach:
1. Sort the asteroids in ascending order. This allows you to destroy smaller asteroids first, increasing your mass gradually.
2. Iterate over each asteroid:
   - If the asteroid's mass is greater than your current mass, return False (since you can't destroy it).
   - Otherwise, absorb the asteroid's mass by adding it to your current mass.
3. If all asteroids are absorbed, return True.

Time Complexity:
- Sorting the asteroids takes O(n log n).
- Iterating through the sorted list is O(n).
- Overall complexity is O(n log n).

Space Complexity:
- O(1) additional space (in-place sorting and simple iteration).

Notes:
- This greedy approach is correct because absorbing the smallest possible asteroids first ensures that 
your mass increases progressively, maximizing your chances of destroying larger asteroids.

Is there an O(n) solution?
- Given that sorting is required to handle asteroids optimally, reducing the complexity below O(n log n) 
isn't feasible for this problem. The sorting step is necessary for the greedy approach to work.
"""

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        ## O(n log n) Solution. 
        
        asteroids.sort()

        for astd in asteroids:
            if astd > mass:
                return False
            else:
                mass = mass + astd

        return True 
    