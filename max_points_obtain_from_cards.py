class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k   # Initializing pointers to define the window that we are excluding
        total = sum(cardPoints[r:])      # Initial sum of the last `k` cards (right end of the array)
        res = total                      # Set `res` to be the sum of the last `k` cards

        while r < len(cardPoints):       # Slide the window until the right pointer `r` reaches the end of the array
            total += (cardPoints[l] - cardPoints[r])  # Add the left card to the total, subtract the right card
            res = max(res, total)        # Keep track of the maximum possible sum
            l += 1                       # Move the left pointer one step to the right
            r += 1                       # Move the right pointer one step to the right

        return res                       # Return the maximum score found
