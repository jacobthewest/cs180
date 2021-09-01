#############################---Exercise 4 Start---####################################
import numpy as np

a = [[1, 2], [2, 1]]
b = [[3], [1]]

def matMulWithoutVectorization():
    newMatrixRows = len(a)
    newMatrixCols = len(b[0])
    resultMatMulMatrix = []

    for i in range(len(a)):  # every row in a
        for j in range(len(b[0])):  # every col in b
            runningTally = 0
            for k in range(len(b)):  # every row in b
                runningTally += a[i][k] * b[k][j]
            resultMatMulMatrix.append([runningTally])

    print("---Matrix Multiplication Without Vectorization---")
    print(resultMatMulMatrix)


def matMulWithVectorization():
    a_matrix = np.array(a)
    b_matrix = np.array(b)
    matrixMultiplicationResult = np.matmul(a_matrix, b_matrix)
    print("---Matrix Multiplication With Vectorization---")
    print(matrixMultiplicationResult)


matMulWithoutVectorization()
matMulWithVectorization()

######################################################################################