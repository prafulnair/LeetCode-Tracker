class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for sent in sentences:
            word_count = len(sent.split())
            if word_count > count:
                count = word_count

        return count