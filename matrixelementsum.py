def matrixElementsSum(matrix):
    new = []
    c = 0
    for i in range(len(matrix[0])):
        col = []
        for j in range(len(matrix)):
            col.append(matrix[j][i])
        new.append(col)
    for a in range(len(new)):
        for b in range(len(new[a])):
            if new[a][b]==0: break
            c += new[a][b]
    return c
matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

print(matrixElementsSum(matrix))