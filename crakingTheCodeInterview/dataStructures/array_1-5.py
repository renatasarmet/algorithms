#One Away: There are three types of edits that can be performed on strings: 
#insert a character, remove a character, or replace a character. 
#Given two strings, write a function to check if they are one edit (or zero edits) away.

#EXAMPLE
#pale, ple -> true 
#pales, pale -> true 
#pale, bale -> true 
#pale, bake -> false

def one_edit(str1, str2):


    if len(str1) == len(str2): # check replace
        return check_replace(str1,str2)
    elif len(str1)+1 == len(str2): # check insert and remove
        return check_insert(str1,str2)
    elif len(str2)+1 == len(str1): # check insert and remove
        return check_insert(str2,str1)
    else:
        return False
       

def check_replace(str1,str2):
    edit_one = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if edit_one == True:
                return False
            edit_one = True

    if edit_one == True:
        return True


def check_insert(str1,str2):
    edit_one = False
    i = 0
    j = 0
    while(i < len(str1) and j < len(str2)):
        if str1[i] != str2[j]:
            if edit_one:
                return False
            edit_one = True

            j += 1
        else:
            i += 1
            j += 1

    return True


str1 = input("String 1:")
str2 = input("String 2:")
print(one_edit(str1, str2))
