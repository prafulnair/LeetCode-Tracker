import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Negate stones to use a min-heap as a max-heap
        stones = [-stone for stone in stones]

        # Create a heap from the stones
        heapq.heapify(stones)

        # Continue smashing stones until one or none remains
        while len(stones) > 1:
            x = -heapq.heappop(stones)  # Largest stone
            y = -heapq.heappop(stones)  # Second largest stone
            if x != y:
                # If they are not the same, push the difference back
                heapq.heappush(stones, -(x - y))

        # Check if there is any stone left
        if stones:
            last_stone = -stones[0]  # The last remaining stone
        else:
            last_stone = 0  # No stones left

        return (last_stone)

        
                