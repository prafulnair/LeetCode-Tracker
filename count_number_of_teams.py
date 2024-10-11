class Solution:
    def numTeams(self, rating: list[int]) -> int:
        
        # Initialize the result to count the number of valid teams
        result = 0 
        
        # Iterate over each soldier's rating as a potential middle soldier in the team
        for i in range(1, len(rating) - 1):
            
            # Initialize counters for smaller ratings on the left and larger ratings on the right
            small_left = large_right = 0

            # Count how many soldiers on the left have a smaller rating than the current soldier
            for p in range(i):
                if rating[p] < rating[i]:
                    small_left += 1
            
            # Count how many soldiers on the right have a larger rating than the current soldier
            for p in range(i + 1, len(rating)):
                if rating[p] > rating[i]:
                    large_right += 1

            # Calculate the number of increasing sequences with the current soldier as the middle one
            result += large_right * small_left

            # Calculate how many soldiers on the left have a larger rating than the current soldier
            large_left = i - small_left

            # Calculate how many soldiers on the right have a smaller rating than the current soldier
            small_right = len(rating) - i - 1 - large_right
            
            # Calculate the number of decreasing sequences with the current soldier as the middle one
            result += large_left * small_right

        # Return the total number of valid teams found
        return result

"""
This function calculates the number of valid teams of 3 soldiers
that can be formed based on their ratings.

A valid team is defined by either increasing or decreasing ratings,
such that for a team (i, j, k):
- rating[i] < rating[j] < rating[k] (increasing)
- rating[i] > rating[j] > rating[k] (decreasing)

The approach is to iterate through each soldier's rating as the
potential middle soldier of a team. For each middle soldier:
- Count how many soldiers on the left have a smaller rating.
- Count how many soldiers on the right have a larger rating.
- Multiply these counts to find the number of increasing sequences. // combination thingy. 

- Count how many soldiers on the left have a larger rating.
- Count how many soldiers on the right have a smaller rating.
- Multiply these counts to find the number of decreasing sequences.

The result is the sum of all valid increasing and decreasing teams.
"""