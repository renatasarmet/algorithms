'''
Rotate Matrix: Given an image represented by an NxN matrix, 
where each pixel in the image is 4 bytes, write a method to 
rotate the image by 90 degrees. Can you do this in place?
'''
import copy

class Matrix:

    # It is a squared matrix
    def __init__(self, value=[[]]):
        self.value = value
        self.size = len(value)


    def __str__(self):

        if self.size == 0: 
            return ''

        answer_list = []
        for i in range(self.size):
            for j in range(self.size):
                answer_list.extend([str(self.value[i][j]), ' '])
            answer_list.append('\n')

        return ''.join(answer_list)


    def rotate_matrix(self):

        if self.size == 0 or self.value[0] != self.size:
            return False
            
        # row turns to column
        aux_matrix = copy.deepcopy(self.value)

        for i in range(self.size):
            count = self.size-1
            for j in range(self.size):
                self.value[count][i] = aux_matrix[i][j]
                count -= 1




m = Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(m)
# 1 2 3
# 4 5 6
# 7 8 9

m.rotate_matrix()
print(m)
# 3 6 9
# 2 5 8
# 1 4 7

# [0][0] -> [2][0]
# [0][1] -> [1][0]
# [0][2] -> [0][0]

# [1][0] -> [2][1]
# [1][1] -> [1][1]
# [1][2] -> [0][1]

# [2][0] -> [2][2]
# [2][1] -> [1][2]
# [2][2] -> [0][2]
