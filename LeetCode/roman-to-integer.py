# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i < len(s) -1:
                    if s[i+1] == 'V':
                        number += 4
                        i += 1
                    elif s[i+1] == 'X':
                        number += 9
                        i += 1
                    else:
                        number += 1
                else:
                    number += 1
            elif s[i] == 'V':
                number += 5
            elif s[i] == 'X':
                if i < len(s) -1:
                    if s[i+1] == 'L':
                        number += 40
                        i += 1
                    elif s[i+1] == 'C':
                        number += 90
                        i += 1
                    else:
                        number += 10
                else:
                    number += 10
            elif s[i] == 'L':
                number += 50
            elif s[i] == 'C':
                if i < len(s) -1:
                    if s[i+1] == 'D':
                        number += 400
                        i += 1
                    elif s[i+1] == 'M':
                        number += 900
                        i += 1
                    else:
                        number += 100
                else:
                    number += 100
            elif s[i] == 'D':
                number += 500
            elif s[i] == 'M':
                number += 1000
            i += 1
        return number
        