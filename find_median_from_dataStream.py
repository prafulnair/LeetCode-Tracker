import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []  # Max-Heap (inverted to use min-heap)
        self.minHeap = []  # Min-Heap

    def addNum(self, num):
        # Add to maxHeap (inverted)
        heapq.heappush(self.maxHeap, -num)

        # Balance the heaps
        if self.maxHeap and self.minHeap and (-self.maxHeap[0] > self.minHeap[0]):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        # Ensure maxHeap has at most one more element than minHeap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2