class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 1

        for i in range(0, len(word)):
            if i == len(word) - 1:
                if word[i] == word[i-1] and count <= 9:
                    comp += str(count) + word[i]
                else:
                    comp += "1" + word[i]
                continue
            if word[i] == word[i+1] and count < 9:
                count += 1
            else:
                comp = comp + str(count) + word[i]
                count = 1


        return comp