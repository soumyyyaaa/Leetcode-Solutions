def setZeroes(matrix):
    is_0_found = False
    index_of_0 = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                is_0_found = True
                index_of_0.append(i)
                index_of_0.append(j)
    if is_0_found:
        for i in range(0, len(index_of_0)):
            if i % 2 == 0:
                row = index_of_0[i]
                for j in range(0, len(matrix[0])):
                    matrix[row][j] = 0
            else:
                col = index_of_0[i]
                for j in range(0, len(matrix)):
                    matrix[j][col] = 0


matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
setZeroes(matrix)
print(matrix)
