import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import numpy as np
from src.Matrix import Matrix

def read(filenameIN):
    with open(filenameIN, 'r') as f:
        text = f.read()
    return text

def write(content, filenameOUT):
    with open(filenameOUT, 'w') as f:
        f.write(content)

def main():
    ### Test case 0
    print(' ### Test case 0 ### \n')

    test_str = "[[1,-4.5,-7.99],[0,5,1],[3,3,0]]"
    print('string in: ', test_str)

    matrix_sparse = Matrix()
    matrix_sparse = matrix_sparse.parse(test_str)
    print('\nin matrix form: \n', np.array(matrix_sparse.write_matrix()))
    print('\nvalues: ', matrix_sparse.values)
    print('columns number: ', matrix_sparse.columns)
    print('points index: ',matrix_sparse.points)

    ### Test case 1
    print('\n\n ### Test case 1 ### \n')

    test_str1 = "[[1,0],[0,1]]"
    print('string in: ', test_str1)

    matrix_sparse1 = Matrix()
    matrix_sparse1 = matrix_sparse1.parse(test_str1)
    print('\nmatrix A = \n', np.array(matrix_sparse1.write_matrix()))
    print('\nvalues: ', matrix_sparse1.values)
    print('columns number: ', matrix_sparse1.columns)
    print('points index: ',matrix_sparse1.points)

    test_str2 = "[[0,0],[3,2]]"
    print('\nstring in: ', test_str2)

    matrix_sparse2 = Matrix()
    matrix_sparse2 = matrix_sparse2.parse(test_str2)
    print('\nmatrix B = \n', np.array(matrix_sparse2.write_matrix()))
    print('\nvalues: ', matrix_sparse2.values)
    print('columns number: ', matrix_sparse2.columns)
    print('points index: ',matrix_sparse2.points)

    matrix_sparse_result = Matrix()
    matrix_sparse_result = matrix_sparse_result.add(matrix_sparse1, matrix_sparse2)

    print('A + B = \n', np.array(matrix_sparse_result.write_matrix()))

    ### Test case 2
    print('\n\n ### Test case 2 ### \n')

    test_str1 = "[[0,0,0,0],[0,0,0,0],[1,1,1,1]]"
    print('string in: ', test_str1)

    matrix_sparse1 = Matrix()
    matrix_sparse1 = matrix_sparse1.parse(test_str1)
    print('\nmatrix A = \n', np.array(matrix_sparse1.write_matrix()))
    print('\nvalues: ', matrix_sparse1.values)
    print('columns number: ', matrix_sparse1.columns)
    print('points index: ',matrix_sparse1.points)

    test_str2 = "[[1,1,1,1],[0,0,0,0],[0,0,0,0]]"
    print('\nstring in: ', test_str2)

    matrix_sparse2 = Matrix()
    matrix_sparse2 = matrix_sparse2.parse(test_str2)
    print('\nmatrix B = \n', np.array(matrix_sparse2.write_matrix()))
    print('\nvalues: ', matrix_sparse2.values)
    print('columns number: ', matrix_sparse2.columns)
    print('points index: ',matrix_sparse2.points)

    matrix_sparse_result = Matrix()
    matrix_sparse_result = matrix_sparse_result.add(matrix_sparse1, matrix_sparse2)

    print('A + B = \n', np.array(matrix_sparse_result.write_matrix()))

    ### Test case 3
    print('\n\n ### Test case 3 ### \n')

    test_str1 = "[[1,1,0,0],[1,1,0,0],[1,1,0,0]]"
    print('string in: ', test_str1)

    matrix_sparse1 = Matrix()
    matrix_sparse1 = matrix_sparse1.parse(test_str1)
    print('\nmatrix A = \n', np.array(matrix_sparse1.write_matrix()))
    print('\nvalues: ', matrix_sparse1.values)
    print('columns number: ', matrix_sparse1.columns)
    print('points index: ',matrix_sparse1.points)

    test_str2 = "[[0,0,1,1],[0,0,1,1],[0,0,1,1]]"
    print('\nstring in: ', test_str2)

    matrix_sparse2 = Matrix()
    matrix_sparse2 = matrix_sparse2.parse(test_str2)
    print('\nmatrix B = \n', np.array(matrix_sparse2.write_matrix()))
    print('\nvalues: ', matrix_sparse2.values)
    print('columns number: ', matrix_sparse2.columns)
    print('points index: ',matrix_sparse2.points)

    matrix_sparse_result = Matrix()
    matrix_sparse_result = matrix_sparse_result.add(matrix_sparse1, matrix_sparse2)

    print('A + B = \n', np.array(matrix_sparse_result.write_matrix()))


    ### Test case 4
    print('\n\n ### Test case 4 ### \n')

    test_str1 = "[[1,-4.5, -7.99],[0,5.3,1],[3,3,0]]"
    print('string in: ', test_str1)

    matrix_sparse1 = Matrix()
    matrix_sparse1 = matrix_sparse1.parse(test_str1)
    print('\nmatrix A = \n', np.array(matrix_sparse1.write_matrix()))
    print('\nvalues: ', matrix_sparse1.values)
    print('columns number: ', matrix_sparse1.columns)
    print('points index: ',matrix_sparse1.points)

    test_str2 = "[[0,-0.5, -0.01],[0,-2.3,0.0],[1,1,1]]"
    print('\nstring in: ', test_str2)

    matrix_sparse2 = Matrix()
    matrix_sparse2 = matrix_sparse2.parse(test_str2)
    print('\nmatrix B = \n', np.array(matrix_sparse2.write_matrix()))
    print('\nvalues: ', matrix_sparse2.values)
    print('columns number: ', matrix_sparse2.columns)
    print('points index: ',matrix_sparse2.points)

    matrix_sparse_result = Matrix()
    matrix_sparse_result = matrix_sparse_result.add(matrix_sparse1, matrix_sparse2)

    print('A + B = \n', np.array(matrix_sparse_result.write_matrix()))

if __name__=='__main__':
    main()
