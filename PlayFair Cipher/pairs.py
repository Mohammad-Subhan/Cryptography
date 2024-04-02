def Pairs(text):
    a = 0
    j = 0
    pairs = ["" for x in range(6)]

    while a < len(text):
        for i in range(2):
            if a >= len(text):
                pairs[j] += 'x'
                break

            pairs[j] += text[a]
            a += 1

        j += 1

    return pairs
