class Matrix:
    def __init__(self, *args):
        self.data = []
        len_col = 0
        if type(args[0]) is list and len(args) == 1:
            len_row = len(args[0][0])
            for v in args[0]:
                if type(v) is not list or len(v) != len_row:
                    self.data = []
                    self.shape = (0, 0)
                    return
                else:
                    self.data.append(v)
                    len_col += 1
            self.shape = (len_col, len_row)
        elif type(args[0]) is tuple and len(args) == 1 and len(args[0]) == 2:
            row = []
            if type(args[0][0]) is int and type(args[0][1]) is int:
                for i in range(args[0][0]):
                    row.append(0)
                for j in range(args[0][1]):
                    self.data.append(row)
            self.shape = args[0]
        elif type(args[0]) is list and len(args) == 2 and type(args[1]) is tuple:
            len_row = len(args[0][0])
            for v in args[0]:
                if type(v) is not list or len(v) != len_row or len(args[1]) != 2:
                    self.data = []
                    self.shape = (0, 0)
                    return
                else:
                    self.data.append(v)
                    len_col += 1
            self.shape = (len_col, len_row)
            if len_col != args[1][0] and len_row != args[1][1]:
                self.data = []
                self.shape = (0, 0)

    def __add__(self, other):
        matrix = []
        if type(other) is list:
            len_col = 0
            len_row = len(other)
            for v in other:
                if type(v) is not list and len(v) != len_row :
                    return self
                len_col += 1
            if len_col != self.shape[0] and len_row != self.shape[1]:
                return self
            else:
                i = 0
                for row in other:
                    matrix.append([x + y for x, y in zip(row, self.data[i])])
                    i += 1
                return Matrix(matrix)
        elif type(other) == type(self) and other.shape[0] == self.shape[0] \
                and other.shape[1] == self.shape[1]:
            i = 0
            for row in other.data:
                matrix.append([x + y for x, y in zip(row, self.data[i])])
                i += 1
            return Matrix(matrix)
        else:
            return self

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        matrix = []
        tmp = []
        if type(other) == (int or float):
            for row in self.data:
                matrix.append([x * other for x in row])                    
            return Matrix(matrix)
        elif type(other) == type(self) and self.shape[1] == other.shape[0]:
            i = 0
            for row in other.data:
                for elem in row:
                    tmp.append(sum



            


















        
