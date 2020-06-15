class TinyStatistician:
    def mean(self, x):
        if type(x) is list:
            add = 0
            for a in x:
                add += a
            return (add / len(x))
        else:
            return None
    
    def median(self, x):
        """mediane c'est le point qui coupe le vecteur en deux"""
        s = sorted(x)
        middle = int(len(s) / 2)
        return float(s[middle])

    def quartile(iself, x, percentile):
        s = sorted(x)
        quartile = int(len(s) / 100 * percentile)
        return float(s[quartile])

    def var(self, x):
        mean = self.mean(x)
        add = 0
        for xi in x:
            add += (xi - mean) ** 2
        return add / len(x)

    def std(self, x):
        var = self.var(x)
        return var ** (1/2)



