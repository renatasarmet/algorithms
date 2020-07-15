'''
Zero Matrix: Write an algorithm such that if an element in an 
MxN matrix is 0, its entire row and column are set to 0.
'''

class Matrix:

    # It is a squared matrix
    def __init__(self, value=[]):
        self.value = value


    def __str__(self):

        n_rows = len(self.value)
        if n_rows == 0: 
            return ''

        n_cols = len(self.value[0])

        answer_list = []
        for i in range(n_rows):
            for j in range(n_cols):
                answer_list.extend([str(self.value[i][j]), ' '])
            answer_list.append('\n')

        return ''.join(answer_list)


    def zero_matrix(self):
        n_rows = len(self.value)
        if n_rows == 0: 
            return False

        n_cols = len(self.value[0])

        zero_rows = set()
        zero_cols = set()

        for i in range(n_rows):
            for j in range(n_cols):
                if self.value[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in zero_rows:
            for j in range(n_cols):
                self.value[i][j] = 0


        for j in zero_cols:
            for i in range(n_rows):
                self.value[i][j] = 0


    def zero_matrix_less_space(self):
        n_rows = len(self.value)
        if n_rows == 0: 
            return False

        n_cols = len(self.value[0])

        firstRowHasZero = False
        firstColHasZero = False

        for i in range(n_rows):
            for j in range(n_cols):
                if self.value[i][j] == 0: 
                    # I can store it at the beggining of the row/column because when I'm here, I have already checked there
                    if i == 0:
                        firstRowHasZero = True
                    if j == 0:
                        firstColHasZero = True

                    self.value[0][j] = 0
                    self.value[i][0] = 0


        for i in range(1,n_rows):
            if self.value[i][0] == 0:
                for j in range(1,n_cols):
                    self.value[i][j] = 0


        for j in range(1,n_cols):
            if self.value[0][j] == 0:
                for i in range(1,n_rows):
                    self.value[i][j] = 0


        if firstRowHasZero:
            for j in range(n_cols):
                self.value[0][j] = 0

        if firstColHasZero:
            for i in range(n_rows):
                self.value[i][0] = 0


m = Matrix([[1,0,3],[4,5,6],[7,8,9]])
print(m)
# 1 0 3
# 4 5 6
# 7 8 9


# m.zero_matrix()
m.zero_matrix_less_space()
print(m)
# 0 0 0
# 4 0 6
# 7 0 9

