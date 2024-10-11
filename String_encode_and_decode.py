"""
String Encode and Decode

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

Constraints:

    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains only UTF-8 characters.
"""


class Solution:

    def encode(self, strs: list[str]) -> str:
        
        """Input : is a list of words, words may have any sort of character"""
        result_string = ""
        for word in strs:
            result_string += str(len(word))+"$"+word

        return result_string

    # def decode(self, s: str) -> list[str]:
    #       """Now the input here is a string of format 5$Fives6$Prafuls"""
    #       result_list = []
          
    #       for i in range(0,len(s)):
    #            if s[i].isnumeric() == True:
    #                 num = int(s[i])
    #                 word = s[i+2:i+num+2]
    #                 result_list.append(word)

    #       return result_list

    def decode(self, s: str) -> list[str]:
        """Now the input here is a string of format 5$Fives6$Prafuls"""
        result_list = []
        i = 0
        
        while i < len(s):
            num = ''
            # Extract the length of the next string
            while i < len(s) and s[i] != "$":
                num += s[i]
                i += 1
            # Convert the length to an integer
            num = int(num)
            i += 1  # Skip the "$" character
            # Extract the string of the given length
            word = s[i:i+num]
            result_list.append(word)
            i += num  # Move to the start of the next length indicator
        
        return result_list

                
                
             
         
    

    

strs = ["neet","code","love","you"]
strs = ["we","say",":","yes","!@#$%^&*()"]
s = Solution()
encoded_string = s.encode(strs)
print(encoded_string)

decoded_string = s.decode(encoded_string)
print((decoded_string))