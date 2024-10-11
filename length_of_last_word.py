class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """ THe following is the easiest way/ 
        Strip first to remove unneccessary spaces
        Then create a list of words using the split func() based on valid space
        then just return the lenghth of last word"""
        
        # s = s.strip()
        # words = s.split(" ")
        # return len(words[-1])

        """s
        In this approach, I am traversing from the last character and finding the first 
        occurence of alphanumeric character, and from there I am counting. In case there 
        is antoher black space now, which mean our word ended, return the length of the word
        else if its the last word itself (only word with space before or after that word in the original string)
        in that case final return will just return the count. 
        """

        wordFlag = False
        count = 0
        for i in range(len(s)-1,-1,-1):
            print(s[i])
            if not s[i].isalnum() and wordFlag == False:
                print("Case 1")
                continue
            elif s[i].isalnum():
                count+=1
                wordFlag = True
                print("Case 2")

            elif not s[i].isalnum() and wordFlag == True:
                print("Case 3")
                return count
        
        return count
            

"""
58. Length of Last Word
Solved
Easy
Topics
Companies

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

 

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.


"""