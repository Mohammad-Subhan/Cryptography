import math
from checkplace import CheckPlace


def Encrypt(text, Pairs, KeyMatrix):
    num = math.ceil(len(text) / 2)
    i = 0
    r = [0 for n in range(2)]
    c = [0 for m in range(2)]
    encrypted = ""
    decrypted = ""

    while i < num:
        for j in range(2):
            letter = Pairs[i][j]
            r[j], c[j] = CheckPlace(KeyMatrix, letter)

        if r[0] == r[1]:
            for j in range(2):
                if c[j] + 1 > 4:
                    encrypted += KeyMatrix[r[j]][0]
                else:
                    encrypted += KeyMatrix[r[j]][c[j] + 1]

        elif c[0] == c[1]:
            for j in range(2):
                if r[j] + 1 > 4:
                    encrypted += KeyMatrix[0][c[j]]
                else:
                    encrypted += KeyMatrix[r[j] + 1][c[j]]

        else:
            encrypted += KeyMatrix[r[0]][c[1]]
            encrypted += KeyMatrix[r[1]][c[0]]

        i += 1

    return encrypted
