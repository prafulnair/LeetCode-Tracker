import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        """
        Intuition:
        This solution leverages a min-heap to efficiently find the k-th smallest element in a sorted matrix. 
        Since each row in the matrix is sorted in ascending order, we can initialize the min-heap with the 
        first element of each row. The smallest element among these will give us a starting point, 
        and then we progressively extract the minimum (smallest) element from the heap k times.
        """
        
        # Step 1: Initialize a min-heap with the first element from each row.
        # Each element is a tuple containing the value, row index, and column index.
        minHeap = []
        
        # We only need to consider up to 'k' rows, as the k-th smallest element cannot be beyond that.
        for r in range(min(k, len(matrix))):
            # Insert the first element of each row into the heap.
            # The tuple format is (value, row_index, column_index).
            heapq.heappush(minHeap, (matrix[r][0], r, 0))

        # Step 2: Extract the smallest element from the heap k times.
        # After popping the smallest k-1 times, the next smallest element is the k-th smallest.
        count = 0
        
        while minHeap:
            # Pop the smallest element from the heap.
            val, r, c = heapq.heappop(minHeap)
            count += 1
            
            # If we've popped the k-th smallest element, return it.
            if count == k:
                return val
            
            # Step 3: If there are more elements in the current row, push the next element from the row.
            if c + 1 < len(matrix[r]):
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))
