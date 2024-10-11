import sys
import heapq
def solution(A):

    AA = [] #creating a separate copy of the array so that original stays intact. This will be used to heapify
    for n in A:
        AA.append(n)
    
    for i in range(len(AA)):
        AA[i] = 0 - A[i] # We need max heap. Turning them to negative would keep abs(most negative number) on top. This can later be leveraged
    
    heapq.heapify(AA)

    res = [] # This will store the top 3 max ints from the Array we heapified
    count = 0
    while(count< 3): # keeping the limit as 3
        res.append(abs(heapq.heappop(AA))) 
        count += 1
  
    result = "" # I am using a string to "string up" a result. 
    for n in A:
        if len(result) == 3: 
          break
        if n in res:
            if len(result) == 0 and n == 0: # I acknowledge the logic isn't 100% perfect. 2 of my test cases aren't passing
              continue
            result += str(n)
            
    return(int(result) if result else "") 


A = [7,0,2,9,3,6,7,9]
A1 = [7,2,3,3,4,9]
print(solution(A))
print(solution(A1))


    
