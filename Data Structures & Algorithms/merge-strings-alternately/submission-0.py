class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        i = 0
        while i < len(word1) and i < len(word2):
            s = s + word1[i] + word2[i]
            i += 1

        while i < len(word1):
            s = s + word1[i]
            i += 1
        
        while i < len(word2):
            s = s + word2[i]
            i += 1
        return s
        