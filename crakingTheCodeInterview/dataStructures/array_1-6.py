'''
String Compression: Implement a method to perform basic string compression 
using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the original string, 
your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a - z).
'''

def string_compression(original):
    original_size = len(original)

    str_list = []
    current_letter = original[0]
    count = 1

    for i in range(1,original_size):
        if original[i] == current_letter:
            count += 1
        else:
            str_list.extend([current_letter, str(count)])
            current_letter = original[i]
            count = 1

    if count > 0:
        str_list.extend([current_letter, str(count)])

    return ''.join(str_list) if len(str_list) < original_size else original


print(string_compression('aabcccccaaa'))
print(string_compression('abcd'))
