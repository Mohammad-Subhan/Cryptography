def CheckPlace(matrix, letter):
    row = 0
    col = 0

    for i in range(5):
        for j in range(5):
            if letter == matrix[i][j]:
                row = i
                col = j
                break

    return row, col
