def diagonalSum(mat):
    sum_of_diagnol = 0
    len_of_mat = len(mat[0])
    for i in range(0, len_of_mat):
        sum_of_diagnol += mat[i][i]
        sum_of_diagnol += mat[i][len_of_mat - i - 1]
    if len_of_mat % 2 != 0:
        j = int((len_of_mat - 1) / 2)
        sum_of_diagnol -= mat[j][j]
    return sum_of_diagnol

mat = [[5]]
print(diagonalSum(mat))
    