import math

class Solvability:

    def __init__(self, dim, values, solution):
        self.val = values
        self.slt = solution
        self.dim = dim
        self.solvable = self.find_d() % 2 == self.find_p() % 2


    def find_d(self):
        cln = 0
        line = 0
        for i in self.val:
            if i == 0:
                xi = cln
                yi = line
                break
            if cln > self.dim - 2:
                cln = 0
                line += 1
            else:
                cln += 1
        if self.dim % 2 != 0:
            xf = math.ceil(self.dim / 2)
            yf = math.ceil(self.dim / 2)
        else:
            xf = self.dim / 2 - 1
            yf = self.dim / 2
        d = math.fabs(xf - xi) + math.fabs(yf - yi)
        return d

    def find_p(self):
        tab = self.val.copy()
        slt_to_flat_list = list(self.slt.flatten())
        model_tab = [x for x in slt_to_flat_list if x != -1]
        p = 0
        for i in range(len(tab)):
            for j in range(i, len(tab)):
                if model_tab.index(tab[i]) > model_tab.index(tab[j]):
                    tab[j], tab[i] = tab[i], tab[j]
                    p += 1
        return p
