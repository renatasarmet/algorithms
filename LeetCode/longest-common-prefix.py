# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        size = len(strs[0])
        for word in strs[1:]:
            if len(word) < size:
                size = len(word)
        prefix = ""
        for i in range(size):
            letter = strs[0][i]
            for word in strs[1:]:
                if word[i] != letter:
                    return prefix
            prefix += letter
        return prefix
        