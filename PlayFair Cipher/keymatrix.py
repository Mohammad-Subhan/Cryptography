def KeyMatrix(key):
    matrix = [['0' for m in range(5)] for n in range(5)]

    a = 0
    c = 96

    for i in range(5):
        j = 0
        while j < 5:

            if a < len(key):
                matrix[i][j] = key[a]
                j += 1

            a += 1

            if a > len(key):
                c += 1
                if chr(c) == 'j':
                    c += 1

                present = False

                for d in key:
                    if chr(c) == d:
                        present = True
                        break

                if present:
                    continue

                matrix[i][j] = chr(c)
                j += 1

    return matrix
