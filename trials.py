# # row_list = ['1','2','.','4','5']
# # row_set = set(row_list)

# # print(row_set)

# # second_row_list = list(row_set)
# # print(second_row_list)

# pattern = "abba"
# s = "dog cat cat dog"

# pat = {}
# for i in range(len(pattern)):
#     pat[pattern[i]] = str(i) if pattern[i] not in pat else pat[pattern[i]] + str(i)


# string = {}
# s_list = s.split(" ")
# print(s_list)
# for i in range(len(s_list)):  # Corrected loop to iterate over indices
#     string[s_list[i]] = str(i) if s_list[i] not in string else string[s_list[i]] + str(i)
# # for val in pat.values():
# #     print(val)

# # for val in string.values():
# #     print(val)

# for val1,val2 in zip(string.values(),pat.values()):
#     if val1!=val2:
#         print("False")
#         break
#     else:
#         print("True")


# pattern = "abba"
# s = "dog cat cat dog"

# s = s.split(" ")
# print(s)
# if len(s) != len(pattern):
#     print("False")

# map = {}
# seen = set()
# i = 0
# for word in pattern:
#     if i > len(s):
#         break
#     if word not in map:
#         map[word] = s[i]
#         seen.add(s[i])
    
#     if word in map and map[word] != s[i]:
#         print(False)
    
#     i+=1
        

# for key, val in map.items():
#     print(f'{key} :: {val}')
    

# print(True)

# s = "a good   example"
# s = s.strip()
# print(s)

# words = s.split(" ")
# print(words)

# words = words[::-1]
# print(words)

# s = " ".join(words)
# print(s)

# s = " ".join(s.split())
# print(s)

# reached = []

# reached.append(10)

# print(reached)



# z = 6%10 + 6%10 + 0
# print(z)
# if z>9:
#     carry = z - 10
# print(z//10)
# print(carry)
# string = "praful"
# sorted = ''.join(sorted(string))
# print(sorted)


import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r/ 3, c/3)

        for i in range (0, len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": continue

                if (board[i][j] in rows[i] or 
                    board[i][j] in cols[j] or
                    board[i][j] in squares[(i//3,j//3)]):
                        return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
                

        return True
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        maxx = 0
        for i in range(0, len(nums)):
            
            left_n = nums[i] - 1
            if left_n not in seen:
                count =0
                right_n = nums[i] + 1
                while(right_n in seen):
                    count+=1
                    right_n+=1
                maxx = max(maxx,count)
            
        
        return maxx + 1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        
        s = s.lower()
        
        res = ""
        for c in s:
            if c.isalnum():
                res += c
        p, q = 0, len(res)-1
        
        while(p < q):
            if res[p]!=res[q]:
                return False
            p += 1
            q -= 1
            
        return True
        

#         s = s.lower()

#         result = ""
#         for i in range(0, len(s)):
#             if s[i].isalnum():
#                 result+=s[i]
#         s= result

#         p = 0
#         q = len(s) - 1
#         print(s)
#         for p in range(0,len(s)):
#             if s[p] != s[q]:
#                 return False
#             q-=1
        
#         return True
        



class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = float("inf")
        
        def searchMin(p, q):
            # Base case: if the range is invalid
            if p > q:
                return float("inf")  # Return a value greater than any possible minimum
            
            mid = p + (q - p) // 2
            
            # Check if the middle element is less than the minimum
            minLeft = searchMin(p, mid - 1)
            minRight = searchMin(mid + 1, q)
            
            return min(nums[mid], minLeft, minRight)
            
        
        return searchMin(0,len(nums)-1)
