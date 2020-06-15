class Vector:
    def __init__(self, args=None):
        if type(args) is list:
            self.values = args
        elif type(args) is int:
            self.values = [float(i) for i in range(args)]
        elif type(args) is tuple and len(args) == 2:
            self.values = [float(i) for i in range(args[0], args[1])]
        else:
            self.values = []
        self.size = len(self.values)

    def __add__(self, other):
        if type(other) is list \
                and len(other) == len(self.values):
            return Vector([i + j for i, j in zip(self.values, other)])
        elif type(other) == type(self) \
                and len(other.values) == len(self.values):
            return Vector([i + j for i, j in zip(self.values, other.values)])
        else:
            return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) is list \
                and len(other) == len(self.values):
            return Vector([i - j for i, j in zip(self.values, other)])
        elif type(other) == type(self) \
                and len(other.values) == len(self.values):
            return Vector([i - j for i, j in zip(self.values, other.values)])
        else:
            return self

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, a):
        if type(a) == (int or float) and a != 0:
            return Vector([i / a for i in self.values])
        else:
            return self

    def __rtruediv__(self, a):
        return self

    def __mul__(self, other):
        if type(other) == (int or float):
            return Vector([i * other for i in self.values])
        elif type(other) is list and len(other) == len(self.values):
            return sum([i * j for i, j in zip(self.values, other)])
        elif type(other) == type(self) \
                and len(other.values) == len(self.values):
            return sum([i * j for i, j in zip(self.values, other.values)])
        else:
            return self

    def __rmul__(self,other):
        return self.__mul__(other)

    def __str__(self):
        return "Vector = {0} of size {1}".format(self.values, self.size)

    def __repr__(self):
        return "Vector(values={},size={})".format(self.values, sel.size)
