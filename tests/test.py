import unittest
import numpy as np
from Matrix import Matrix


class TestMatrix(unittest.TestCase):

    def test_add1(self):
        str_a_test = "[[1,-4.5, -7.99],[0,5.3,1],[3,3,0]]"
        # [1.0, -4.5, -7.99]
        # [0.0,  5.3,   1.0]
        # [3.0,  3.0,   0.0]
        str_b_test = "[[0,-0.5, -0.01],[0,-2.3,0.0],[1,1,1]]"
        # [0.0, -0.5, -0.01]
        # [0.0, -2.3,   0.0]
        # [1.0,  1.0,   1.0]

        matrix_a = Matrix()
        matrix_a.parse(str_a_test)

        matrix_b = Matrix()
        matrix_b.parse(str_b_test)

        out_matrix = Matrix()
        sum = out_matrix.add(matrix_a, matrix_b)
        sum_list = sum.write_matrix()
        print(np.array(sum.write_matrix()))
        # [1.0, -5.0, -8.0]
        # [0.0,  3.0,  1.0]
        # [4.0,  4.0,  1.0]
        # sum_actual = np.array(matrix_a.write_matrix()) + np.array(matrix_b.write_matrix())
        sum_actual = [[1.0, -5.0, -8.0],[0.0, 3.0, 1.0],[4.0, 4.0, 1.0]]

        # self.assertTrue(np.allclose(np.array(sum_list), np.array(sum_actual), rtol=1e-3))

if __name__ == '__main__':
    unittest.main()
