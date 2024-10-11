class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # finding the longer and shorter string

        short = str2 if len(str2) < len(str1) else str1
        long = str1 if len(str1) > len(str2) else str2

        for i in range (len(short)+1, 0, -1):

            print("Inside Else")
            mult1 = len(short) // i
            mult2 = len(long) // i
            # print(short[:i])
            # print(short[:i]*mult1)
            # print(short[:i]*mult2)
            if short[:i] * mult1 == short and short[:i] * mult2 == long:
                return short[:i]
            
        return ""
    

"""
THE INTUITION
Basically ,we want to find the length of the substring of the shorter string that is a factor of longer and shorter string both
for example. in str1 = ABCABC and str2 = ABC...we start from reverse (because we want the biggest string, the largest x)
so we start with length = 3 with ABC, ABC - 3  and we need exactly 1 * ABC to get shorter string
len(long=6)//3 = 2. We get 2 * ABC = longer string. SO this is the answer. It should satisfy both condition

in case of second example
ABABAB and ABAB
we start with i = 4 so ABAB
we need 1 * ABAB to get shorter length
6//4 = 1 but 1 & ABAB is not equal to ABABAB
so we do 3 - ABA
but 3 does not divide 4 fully, so no need to check again
then we got 2. AB
2*AB is ABAB - shorter string
3 * AB is ABABAB which is longer string, so return that
"""
"""
1071. Greatest Common Divisor of Strings
Solved
Easy
Topics
Companies
Hint

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

 

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.


"""