class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """
        Problem: Car Fleet
        
        Intuition:
        - We need to determine how many groups (or fleets) of cars will arrive at the target.
        - Each car has a starting position and speed. A car can either drive solo or catch up to 
          another car ahead if it's slower, forming a fleet. Once caught up, cars cannot pass each other.
        - To solve this, we first sort the cars based on their position. Then, we process the cars
          from the farthest to the closest to the target.
        - The key observation is to compute the time each car requires to reach the target. If a car 
          takes more time than the one ahead, it will form a new fleet. If it takes less or equal time, 
          it will join the existing fleet ahead.
        - We keep track of the number of fleets by comparing each car's time with the `last_time` 
          (the time of the car ahead). If the current car's time is greater, a new fleet is formed.
        
        Time Complexity: O(n log n) due to sorting the cars by position.
        """

        # Pair each car's position and speed, then sort by position
        for i in range(0, len(speed)):
            position[i] = [position[i], speed[i]]
        
        position.sort(key=lambda x: x[0])  # Sort by position in ascending order
        
        fleets, last_time = 0, 0  # Initialize number of fleets and last_time to 0

        # Traverse from the farthest car to the closest one
        for i in range(len(position)-1, -1, -1):
            pos = position[i][0]
            spd = position[i][1]
            timeReq = (target - pos) / spd  # Time required for the car to reach the target

            # If the current car can't catch up to the fleet ahead, form a new fleet
            if timeReq > last_time:
                fleets += 1
                last_time = timeReq  # Update last_time to the time of this car's fleet

        return fleets  # Return the total number of fleets