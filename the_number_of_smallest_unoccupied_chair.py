import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Assign indices to friends to track targetFriend
        for i in range(len(times)):
            times[i].append(i)
        
        # Sort times by the arrival time
        times.sort(key=lambda x: x[0])
        
        available_chairs = []  # Min-heap of available chairs
        heapq.heapify(available_chairs)
        for i in range(len(times)):
            heapq.heappush(available_chairs, i)  # Initially, we have all chairs available
        
        occupied = []  # Min-heap of (leave time, chair number)
        
        # Iterate over each friend's arrival and leaving times
        for time in times:
            arrival, leave, friend_idx = time
            
            # Free chairs of friends who have left before the current friend arrives
            while occupied and occupied[0][0] <= arrival:
                leave_time, chair_number = heapq.heappop(occupied)
                heapq.heappush(available_chairs, chair_number)
            
            # Assign the smallest available chair to the current friend
            chair = heapq.heappop(available_chairs)
            
            # If the current friend is the target friend, return the chair number
            if friend_idx == targetFriend:
                return chair
            
            # Add the leave time and the chair to the occupied heap
            heapq.heappush(occupied, (leave, chair))

        return -1
