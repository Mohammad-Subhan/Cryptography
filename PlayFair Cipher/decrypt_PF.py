import math
from checkplace import CheckPlace


def Decrypt(text, Pairs, KeyMatrix):
    num = math.ceil(len(text) / 2)
    i = 0
    r = [0 for n in range(2)]
    c = [0 for m in range(2)]
    decrypted = ""

    while i < num:
        for j in range(2):
            letter = Pairs[i][j]
            r[j], c[j] = CheckPlace(KeyMatrix, letter)

        if r[0] == r[1]:
            for j in range(2):
                if c[j] - 1 < 0:
                    decrypted += KeyMatrix[r[j]][4]
                else:
                    decrypted += KeyMatrix[r[j]][c[j] - 1]

        elif c[0] == c[1]:
            for j in range(2):
                if r[j] - 1 < 0:
                    decrypted += KeyMatrix[4][c[j]]
                else:
                    decrypted += KeyMatrix[r[j] - 1][c[j]]

        else:
            decrypted += KeyMatrix[r[0]][c[1]]
            decrypted += KeyMatrix[r[1]][c[0]]

        i += 1

    return decrypted
