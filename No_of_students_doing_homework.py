class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        
        counter = 0
        for i in range(0, len(startTime)):
            if startTime[i] <=queryTime and queryTime <= endTime[i]:
                counter += 1
        
        return counter


        # 1, 2, 3
        # 3, 5, 7  queryTime = 4. In that case, 


## Fumbled around like an idiot for good solid 5 minutes, before figuring out how 
## trivial this problem is. 