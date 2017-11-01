# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
import numpy as np
import math as m

class DFT:

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        (rows, columns) = matrix.shape
        tempmatrix = np.zeros((rows, columns), dtype = complex)
        for u in range(matrix.shape[0]) :
            for v in range(matrix.shape[1]) :
                for i in range(matrix.shape[0]) :
                    for j in range(matrix.shape[1]) :
                        tempmatrix[u][v] = tempmatrix[u][v] + matrix[i][j] * complex(m.cos((2 * np.pi / rows )* (u * i + v * j)),
                                                                         -m.sin((2 * np.pi / columns) * (u * i + v * j)))

        matrix = tempmatrix
        return matrix

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        matrix: a 2d matrix (DFT) usually complex
        takes as input:
        returns a complex matrix representing the inverse fourier transform"""
        (rows, columns) = matrix.shape
        tempmatrix = np.zeros((rows, columns), dtype=complex)
        for u in range(matrix.shape[0]):
            for v in range(matrix.shape[1]):
                for i in range(matrix.shape[0]):
                    for j in range(matrix.shape[1]):
                        tempmatrix[u][v] = tempmatrix[u][v] + matrix[i][j] * complex(m.cos((2 * np.pi / rows )* (u * i + v * j)),
                                                                         m.sin((2 * np.pi / columns) * (u * i + v * j)))

        matrix = tempmatrix
        return matrix


    def discrete_cosine_tranform(self, matrix):
        """Computes the discrete cosine transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing discrete cosine transform"""
        (rows, columns) = matrix.shape
        #print(rows, columns)
        tempmatrix = np.zeros((rows, columns), dtype=complex)
        for u in range(matrix.shape[0]):
            for v in range(matrix.shape[1]):
                for i in range(matrix.shape[0]):
                    for j in range(matrix.shape[1]):
                        tempmatrix[u][v] = tempmatrix[u][v] + matrix[i][j] * m.cos((2 * np.pi /rows) * (u * i + v * j))
        matrix = tempmatrix
        return matrix


    def magnitude(self, matrix):
        """Computes the magnitude of the DFT
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the dft"""
        tempmatrix = np.zeros((matrix.shape[0], matrix.shape[1]))
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                tempmatrix[i][j] = m.sqrt(m.pow(np.real(matrix[i][j]), 2) + m.pow(np.imag(matrix[i][j]), 2))
        matrix = tempmatrix
        return matrix