# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for l in range(len(haystack)):
            if haystack[l] == needle[0]:
                ok = True
                i = 1
                cont = l + 1
                while i < len(needle):
                    if cont >= len(haystack):
                        return -1
                    if haystack[cont] != needle[i]:
                        ok = False
                        break
                    i += 1
                    cont += 1
                if ok:
                    return l
        return -1
                