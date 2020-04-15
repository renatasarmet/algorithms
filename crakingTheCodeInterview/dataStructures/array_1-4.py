# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome. 
#A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.
#EXAMPLE
#Input: Tact Coa
#Output: True (permutations: "taco cat", "atco cta", etc.)

def is_permutation_palindrome(string):
    dic = {}

    for i in string:
        dic[i] = dic.get(i,0) + 1

    size = len(string)

    if " " in dic:
        size -= dic[" "]
        del dic[" "]

    is_odd = size % 2 != 0

    for i in dic:
        if dic[i] % 2 != 0:
            if is_odd: #if it is odd, one time is allowed
                is_odd = False
            else:
                return False

    return True



string = input("String:")
print(is_permutation_palindrome(string))
