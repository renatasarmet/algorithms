# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            sentence = self.countAndSay(n-1)
            result = ""
            l = 0
            while l < len(sentence):
                if l == len(sentence) -1:
                    result += "1" + sentence[l]
                else:
                    cont = 1
                    while l < (len(sentence) -1) and sentence[l+1] == sentence[l]:
                        cont += 1
                        l += 1
                    result += str(cont) + sentence[l]
                l += 1

            return(result)
        