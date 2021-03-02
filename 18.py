x = [1, 2, 3]
import time
rows = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]


def solve(pyramid):
    if (len(pyramid) == 1):
        return pyramid[0][0]
    if len(pyramid) == 2:
        if (pyramid[1][0] >= pyramid[1][1]):
            return pyramid[0][0] + pyramid[1][0]
        else:
            return pyramid[0][0] + pyramid[1][1]
    else:
        count = 0

        x = []
        for i in pyramid[2]:
            count += 1
            l = [[i]]
            j = 0
            for t in range(3, len(pyramid)):
                l.append(pyramid[t][count - 1:t + count - 2])
            j += solve(l)
            x.append(j)

        a = [
            pyramid[0][0] + pyramid[1][0] + x[0],
            pyramid[0][0] + pyramid[1][0] + x[1],
            pyramid[0][0] + pyramid[1][1] + x[1],
            pyramid[0][0] + pyramid[1][1] + x[2],
        ]
        return max(a)


print(solve(rows))
print(time.process_time())