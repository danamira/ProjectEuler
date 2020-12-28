def next(current):
    if current % 2 == 0:
        return current / 2
    else:
        return 3 * current + 1


def checkSequence(start):
    current = start
    count = 0
    while current != 1:
        count += 1
        current = next(current)
    count += 1
    return count


most = 0
result = 0
for i in range(1, 1000001):
    print(i)
    print(checkSequence(i))
    print('-------------------------------')
    if checkSequence(i) > most:
        most = checkSequence(i)
        result = i
print(result)
