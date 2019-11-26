import numpy as np
def solver(matrix):

    values=np.zeros(matrix.shape[1],matrix.shape[1]+2)
    values[:,:]=-1e100

    for i in range(1,matrix.shape[1]+1):
        for j in range(i+1,matrix.shape[1]+1):
            values[i][j]=matrix[0][i-1]+matrix[0][j-1]
    for k in range(1,len(matrix)):
        for i in range(1,matrix.shape[1]+1):
            for j in range(i+1,matrix.shape[1]+1):
                values[i,j]=matrix[k][i-1]+matrix[k][j+1]+max([values[i-1][j-1],values[i-1][j],values[i-1][j+1],values[i][j-1],values[i][j],values[i][j+1],values[i+1][j],values[i+1][j+1],values[i+1][j-1]])
    
    return values[1][matrix.shape[1]+1]






                     



