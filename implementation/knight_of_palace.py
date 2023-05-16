alphaDict = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h':8}

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

pos = input()
result = 0


if pos[0] in alphaDict:
    cx = int(alphaDict[pos[0]])
    cy = int(pos[1])

    for step in steps:
        nx = cx + step[0]
        ny = cy + step[1]

        if nx > 0 and nx <= 8 and ny > 0 and ny <= 8:
            result += 1

print(result)