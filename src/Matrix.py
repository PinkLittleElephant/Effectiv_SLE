import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from typing import Tuple
import re

class Matrix():
    def __init__(self, values = list(), columns = list(), points = list(), n = 0, m = 0):
        self.values = values
        self.columns = columns
        self.points = points
        self.n = n
        self.m = m

    def parse(self, string):
        string = string[1:-1]
        rows = re.split(r'\],\[', string)
        rows[0] = rows[0][1::]
        rows[-1] = rows[-1][0:-1]

        float_values = list()
        columns = list()
        points = list()
        for r in rows:
            flag_zero = True
            items = re.split(r',', r)
            items_float = list()
            flag = False
            for item, col in zip(items, range(len(items))):
                i = float(item)
                if i != 0.0:
                    float_values.append(i)
                    columns.append(col)
                    if not(flag): points.append(len(float_values)-1)
                    flag = True
                    flag_zero = False
                else: flag_zero = flag_zero and True
            if flag_zero:
                if len(points) == 0:
                    points.append(0)
                else:
                    points.append(len(float_values))
        points.append(len(float_values))
        matrix_sparse = Matrix(float_values, columns, points, len(rows), len(items))
        return matrix_sparse

    def add(self, A, B):
        assert (A.n == B.n)&(A.m == B.m), "Matrix dimensions do not match"

        self.n = A.n
        self.m = A.m

        values = list()
        columns = list()
        points = list()
        l = 0
        points.append(l)
        for i in range(self.n):
            columns_out = {}
            for j in range(A.points[i], A.points[i+1]):
                columns_A = A.columns[j]
                columns_out[columns_A] = A.values[j]

            for j in range(B.points[i], B.points[i+1]):
                columns_B = B.columns[j]
                if columns_B in columns_out:
                    columns_out[columns_B] = columns_out[columns_B] + B.values[j]
                else: columns_out[columns_B] = B.values[j]
            l = l + len(columns_out)
            points.append(l)
            for v in columns_out:
                columns.append(v)
                values.append(columns_out[v])
        points.append(len(values))
        matrix = Matrix(values, columns, points, A.n, A.m)

        return matrix

    def write_matrix(self):
        out_matrix = [ [0] * self.m for _ in range(self.n)]
        for i in range(len(self.points) - 1):
            for element_i in range(self.points[i], self.points[i+1]):
                j = self.columns[element_i]
                out_matrix[i][j] = self.values[element_i]
        return out_matrix
